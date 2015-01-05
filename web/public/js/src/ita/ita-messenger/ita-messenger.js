'use strict';

var angular = require('angular');

angular
    .module('ItaMessenger', [])
    .provider('itaMessenger', require('./ita-messenger-provider'));