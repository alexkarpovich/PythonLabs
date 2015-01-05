'use strict';

var angular = require('angular');

angular
    .module('User.Admin.User', [])
    .config(require('./user-config'))
    .controller('User.Admin.User.ListController', require('./list/list-controller'))
    .controller('User.Admin.User.EditController', require('./edit/edit-controller'));
