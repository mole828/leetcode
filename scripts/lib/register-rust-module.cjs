'use strict';

const fs = require('node:fs');
const path = require('node:path');

try {
  const [root, id, filename] = process.argv.slice(2);
  if (!root || !/^\d+$/.test(id) || filename !== 'Solution.rs') {
    throw new Error('Invalid Rust solution module');
  }
  const manifest = path.join(root, 'Cargo.toml');
  if (!fs.existsSync(manifest)) {
    fs.writeFileSync(manifest, '[package]\nname = "leetcode-solutions"\nversion = "0.1.0"\nedition = "2021"\npublish = false\n');
  }
  const library = path.join(root, 'src/lib.rs');
  const name = `p${id}`;
  const block = `#[path = "../problems/${name}/${filename}"]\npub mod ${name};`;
  let content = '';
  try {
    content = fs.readFileSync(library, 'utf8');
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }
  if (content.includes(block)) process.exit(0);
  if (new RegExp(`\\bmod\\s+${name}\\s*[;{]`).test(content)) {
    throw new Error(`Module ${name} is already declared differently in ${library}`);
  }
  fs.mkdirSync(path.dirname(library), { recursive: true });
  fs.writeFileSync(library, content + (content && !content.endsWith('\n') ? '\n' : '') + block + '\n');
} catch (error) {
  console.error(`Register Rust module: ${error.message}`);
  process.exitCode = 1;
}
