#!/usr/bin/env node
'use strict';

// Deterministic privacy backstop for outbound model calls.
//
// Loads a gitignored denylist and replaces each entry with a placeholder BEFORE
// any prompt/system text is sent to a third-party model (invoke-gpt / invoke-gemini).
// This is enforcement, complementing the model-applied `privacy-guard` skill.
//
// Denylist: scripts/agents/.redact-denylist.local.json  (gitignored; never committed)
//   Format: [ { "find": "literal" | "/regex/flags", "replace": "[PLACEHOLDER]" }, ... ]
//   - "find" wrapped in /slashes/ is treated as a regex ("g" is forced).
//   - Otherwise "find" is a literal, matched case-insensitively and globally.
// See .redact-denylist.local.json.example for a template. With no denylist present,
// this is a silent no-op (the skill remains the first line of defence).

const fs = require('fs');
const path = require('path');

const DENYLIST_PATH = path.join(__dirname, '.redact-denylist.local.json');

function buildRules() {
  let raw;
  try {
    raw = fs.readFileSync(DENYLIST_PATH, 'utf8');
  } catch (_) {
    return []; // no denylist configured → no-op
  }
  let list;
  try {
    list = JSON.parse(raw);
  } catch (err) {
    process.stderr.write(`[redact] WARNING: could not parse ${path.basename(DENYLIST_PATH)}: ${err.message}\n`);
    return [];
  }
  if (!Array.isArray(list)) return [];
  const rules = [];
  for (const entry of list) {
    if (!entry || typeof entry.find !== 'string' || !entry.find) continue;
    const replace = typeof entry.replace === 'string' ? entry.replace : '[REDACTED]';
    const m = entry.find.match(/^\/(.+)\/([a-z]*)$/is);
    try {
      if (m) {
        const flags = m[2].includes('g') ? m[2] : m[2] + 'g';
        rules.push({ re: new RegExp(m[1], flags), replace });
      } else {
        const escaped = entry.find.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        rules.push({ re: new RegExp(escaped, 'gi'), replace });
      }
    } catch (err) {
      process.stderr.write(`[redact] WARNING: skipping invalid rule "${entry.find}": ${err.message}\n`);
    }
  }
  return rules;
}

const RULES = buildRules();

function redact(text) {
  if (typeof text !== 'string' || text.length === 0 || RULES.length === 0) return text;
  let out = text;
  let hits = 0;
  for (const { re, replace } of RULES) {
    out = out.replace(re, () => { hits++; return replace; });
  }
  if (hits > 0 && process.env.FH_REDACT_QUIET !== '1') {
    process.stderr.write(`[redact] applied ${hits} redaction(s) before sending to the external model\n`);
  }
  return out;
}

module.exports = { redact, DENYLIST_PATH, rulesLoaded: RULES.length };
