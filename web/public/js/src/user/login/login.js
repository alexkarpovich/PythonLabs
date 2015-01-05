'use strict';

var angular = require('angular');

angular
    .module('User.Login', [])
    .config(require('./login-config'))
    .controller('User.LoginController', require('./login-controller'));
