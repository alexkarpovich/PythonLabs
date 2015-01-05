'use strict';

var angular = require('angular');

require('./login/login');
require('./registration/registration');
require('./profile/profile');
require('./admin/admin');

angular
    .module('User', [
        'User.Login',
        'User.Registration',
        'User.Profile',
        'User.Admin'
    ])
    .config(require('./user-config'));