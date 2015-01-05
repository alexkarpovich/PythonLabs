'use strict';

var angular = require('angular');

angular
    .module('User.Registration', [])
    .config(require('./registration-config'))
    .controller('User.RegistrationController', require('./registration-controller'));
