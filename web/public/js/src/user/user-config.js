'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('user', {
                url: '/user',
                template: '<ui-view></ui-view>'
            });
    }
];
