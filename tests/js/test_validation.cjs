'use strict';
const assert = require('node:assert/strict');
const { isSafeIdentifier } = require('../../examples/js/validation.cjs');
assert.equal(isSafeIdentifier('sample_1'), true);
assert.equal(isSafeIdentifier('A'), false);
assert.equal(isSafeIdentifier('../private'), false);
assert.equal(isSafeIdentifier(''), false);
assert.equal(isSafeIdentifier(null), false);
console.log('5 public JavaScript assertions passed');
