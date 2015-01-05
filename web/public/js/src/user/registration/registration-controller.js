'use strict';

module.exports = ['$scope', 'itaRequest', '$state', function ($scope, itaRequest, $state) {
    $scope.userData = {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: ''
    };

    $scope.submit = function () {
        return itaRequest.request({
            url: '/user/registration',
            method: 'post',
            data: $scope.userData
        });
    };

    $scope.submitSuccess = function() {
        $state.go('user.login');
    };
}];
