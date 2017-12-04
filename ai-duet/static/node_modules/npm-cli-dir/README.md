# npm-cli-dir

[![NPM version](https://img.shields.io/npm/v/npm-cli-dir.svg)](https://www.npmjs.com/package/npm-cli-dir)
[![Build Status](https://travis-ci.org/shinnn/npm-cli-dir.svg?branch=master)](https://travis-ci.org/shinnn/npm-cli-dir)
[![Build status](https://ci.appveyor.com/api/projects/status/e83hdqrnieckmm5c/branch/master?svg=true)](https://ci.appveyor.com/project/ShinnosukeWatanabe/npm-cli-dir/branch/master)
[![Coverage Status](https://img.shields.io/coveralls/shinnn/npm-cli-dir.svg)](https://coveralls.io/github/shinnn/npm-cli-dir)

A [Node.js](https://nodejs.org/) module to resolve the directory path where [npm](https://www.npmjs.com/) CLI is installed

```javascript
const npmCliDir = require('npm-cli-dir');

npmCliDir().then(dir => {
  dir; //=> '/usr/local/lib/node_modules/npm'
});
```

## Installation

[Use npm.](https://docs.npmjs.com/cli/install)

```
npm install npm-cli-dir
```

## API

```javascript
const npmCliDir = require('npm-cli-dir');
```

### npmCliDir()

Return: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) instance

It resolves the base path of globally installed [npm](https://github.com/npm/npm) CLI.

```javascript
const fs = require('fs');
const npmCliDir = require('npm-cli-dir');

npmCliDir().then(dir => {
  fs.readdirSync(dir);
  //=> ['.mailmap', '.npmignore', '.travis.yml', 'AUTHORS', 'CHANGELOG.md', ...]
});
```

## License

[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed)
