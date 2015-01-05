'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('user.login', {
                url: '/login',
                template: require('./login.html'),
                controller: 'User.LoginController'
            });
    }
];
