'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('user.edit-profile', {
                url: '/edit-profile',
                template: require('./edit-profile.html'),
                controller: 'User.EditProfileController'
            });
    }
];
