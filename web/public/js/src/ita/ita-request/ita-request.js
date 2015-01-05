'use strict';

var angular = require('angular');

angular.module('ItaRequest', [])
    .provider('itaRequest', require('./ita-request-provider'))
    .config(require('./ita-request-config'));
