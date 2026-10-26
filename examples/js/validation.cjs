'use strict';
// Public synthetic example, no network or secret inputs.
function isSafeIdentifier(value) {
  return typeof value === 'string' && /^[a-z][a-z0-9_-]{0,31}$/.test(value);
}
module.exports = { isSafeIdentifier };
