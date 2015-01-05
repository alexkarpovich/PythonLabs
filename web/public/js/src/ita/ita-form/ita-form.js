'use strict';

var angular = require('angular');

angular.module('ItaForm', [])
    .directive('itaForm', require('./ita-form-directive'))
    .directive('itaFormRow', require('./ita-form-row-directive'))
    .directive('itaFormRowErrorMessages', require('./ita-form-error-messages-directive'));
