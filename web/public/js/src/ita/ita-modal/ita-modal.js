'use strict';

var angular = require('angular');

angular.module('ItaModal', [])
    .provider('itaModal', require('./ita-modal-provider'))
    .directive('itaModalContent', require('./ita-modal-content-directive'));

