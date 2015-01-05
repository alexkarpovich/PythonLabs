'use strict';

module.exports = ['$scope', 'itaRequest', '$state', 'itaEmbeddedData',
    function ($scope, itaRequest, $state, itaEmbeddedData) {
        $scope.loginData = {
            email: '',
            password: ''
        };

        $scope.login = function () {
            return itaRequest.request({
                url: '/user/login',
                method: 'post',
                data: $scope.loginData
            }).then(function(data) {
                itaEmbeddedData.setCurrentUser(data.user);
            });
        };

        $scope.submitSuccess = function() {
            $state.go('home');
        };
    }
];
