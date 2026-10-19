'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { parseEnv } = require('node:util');

// Parse dotenv data without executing shell expressions. Existing environment wins.
function loadEnv(repository) {
  const file = path.join(repository, '.env');
  let content;
  try {
    content = fs.readFileSync(file, 'utf8');
  } catch (error) {
    if (error.code === 'ENOENT') return {};
    throw error;
  }
  if (typeof parseEnv !== 'function') {
    throw new Error('Reading .env requires Node.js 20.12+');
  }
  const loaded = {};
  for (const [key, value] of Object.entries(parseEnv(content))) {
    if (process.env[key] === undefined) {
      process.env[key] = value;
      loaded[key] = value;
    }
  }
  return loaded;
}

module.exports = { loadEnv };

// The zsh commands consume NUL-separated assignments, preserving spaces/newlines.
if (require.main === module) {
  try {
    for (const [key, value] of Object.entries(loadEnv(process.argv[2]))) {
      process.stdout.write(`${key}=${value}\0`);
    }
  } catch (error) {
    console.error(`leetcode configuration: ${error.message}`);
    process.exitCode = 1;
  }
}
