'use strict';

module.exports = ['$scope', 'itaRequest', 'itaMessenger',
    function ($scope, itaRequest, itaMessenger) {
        $scope.updateUsers = function () {
            itaRequest.request({
                url: '/user/admin/user/list',
                method: 'post'
            }).then(function(data) {
                $scope.users = data.users;
            });
        };

        $scope.updateUsers();

        $scope.delete = function (user) {
            itaMessenger.confirm('Are you sure to delete user?', function(confirm) {
                if (confirm) {
                    itaRequest.request({
                        url: '/user/admin/user/delete',
                        method: 'post',
                        data: {
                            id: user.id
                        }
                    }).then(function() {
                        $scope.updateUsers();
                    });
                }
            });
        };
    }
];
