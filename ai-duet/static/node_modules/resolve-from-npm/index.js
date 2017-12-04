'use strict';

const inspectWithKind = require('inspect-with-kind');
const npmCliDir = require('npm-cli-dir');
const resolveFrom = require('resolve-from');

module.exports = function resolveFromNpm(moduleId) {
  return npmCliDir().then(fromDir => {
    if (typeof moduleId !== 'string') {
      return Promise.reject(new TypeError(`Expected a module ID to resolve from npm directory (${fromDir}), but got ${
        inspectWithKind(moduleId)
      }.`));
    }

    const result = resolveFrom.silent(fromDir, moduleId);

    if (result === null) {
      const err = new Error(`Cannot find module \`${moduleId}\` from npm directory (${fromDir}).`);
      err.code = 'MODULE_NOT_FOUND';

      return Promise.reject(err);
    }

    return result;
  });
};
