'use strict';

const dirname = require('path').dirname;

const npmCliPath = require('npm-cli-path');
const resolveFromSilent = require('resolve-from').silent;

const getNpmCliDir = npmCliPath().then(result => {
  do {
    result = dirname(result);
  } while (resolveFromSilent(result, './package.json') === null);

  return result;
});

module.exports = function npmCliDir() {
  return getNpmCliDir;
};
