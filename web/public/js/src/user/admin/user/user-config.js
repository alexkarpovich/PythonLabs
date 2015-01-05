'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('admin.user', {
                url: '/user',
                template: '<ui-view></ui-view>'
            })
            .state('admin.user.list', {
                url: '/list',
                template: require('./list/list.html'),
                controller: 'User.Admin.User.ListController'
            })
            .state('admin.user.edit', {
                url: '/edit/:userId',
                template: require('./edit/edit.html'),
                controller: 'User.Admin.User.EditController'
            });
    }
];
