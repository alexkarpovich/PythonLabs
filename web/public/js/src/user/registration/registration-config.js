'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('user.registration', {
                url: '/registration',
                template: require('./registration.html'),
                controller: 'User.RegistrationController'
            });
    }
];
