'use strict';

var angular = require('angular');

angular
    .module('User.Profile', [])
    .config(require('./profile-config'))
    .controller('User.EditProfileController', require('./edit-profile-controller'));
