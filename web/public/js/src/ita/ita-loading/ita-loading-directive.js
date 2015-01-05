'use strict';

module.exports = [function () {
        return {
            restrict: 'E',
            replace: true,
            template: require('./ita-loading.html'),
            controller: ['$scope', 'itaLoading', function($scope, itaLoading) {
                $scope.getLoading = function () {
                    return itaLoading.getLoading();
                };
            }]
        };
    }
];
