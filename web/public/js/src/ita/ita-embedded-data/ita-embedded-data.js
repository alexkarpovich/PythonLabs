'use strict';

var angular = require('angular');

angular.module('ItaEmbeddedData', [])
    .provider('itaEmbeddedData', require('./ita-embedded-data-provider'));
