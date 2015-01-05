'use strict';

var angular = require('angular');

require('./user/user');

angular
    .module('User.Admin', [
        'User.Admin.User'
    ])
    .config(require('./admin-config'));
