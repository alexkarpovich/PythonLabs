'use strict';

var angular = require('angular');

angular.module('TopMenu', [])
    .directive('topMenu', require('./top-menu-directive'));
