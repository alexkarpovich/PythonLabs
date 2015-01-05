'use strict';

var angular = require('angular');

module.exports = ['$scope', 'itaRequest', 'itaEmbeddedData','$state',
    function ($scope, itaRequest, itaEmbeddedData, $state) {
        $scope.userData = angular.copy(itaEmbeddedData.getCurrentUser());
        $scope.userData.password = '';
        $scope.userData.confirmPassword = '';


        $scope.editProfile = function () {
            return itaRequest.request({
                url: '/user/edit-profile',
                method: 'post',
                data: $scope.userData
            });
        };

        $scope.submitSuccess = function() {
            $state.go('home');
        };
    }
];
