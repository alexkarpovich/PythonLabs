'use strict';

var angular = require('angular');

angular
    .module('ItaLoading', [])
    .directive('itaLoading', require('./ita-loading-directive'))
    .provider('itaLoading', require('./ita-loading-provider'));
