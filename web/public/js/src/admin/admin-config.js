'use strict';

module.exports = ['$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('admin', {
                url: '/admin',
                template: require('./admin-layout.html')
            });
    }
];
