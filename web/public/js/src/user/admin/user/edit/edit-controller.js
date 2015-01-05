'use strict';

module.exports = ['$scope', 'itaRequest', '$stateParams', '$state',
    function ($scope, itaRequest, $stateParams, $state) {
        itaRequest.request({
            url: '/user/admin/user/get',
            method: 'post',
            data: {
                id: $stateParams.userId
            }
        }).then(function(data) {
            $scope.userData = data.user;
        });

        $scope.edit = function () {
            return itaRequest.request({
                url: '/user/admin/user/save',
                method: 'post',
                data: $scope.userData
            });
        };

        $scope.submitSuccess = function() {
            $state.go('admin.user.list');
        };
    }
];
