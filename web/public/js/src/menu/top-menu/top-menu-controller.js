'use strict';

module.exports = ['$scope', 'itaEmbeddedData', 'itaRequest', '$state',
    function ($scope, itaEmbeddedData, itaRequest, $state) {
        $scope.isLoggedIn = function() {
            $scope.currentUser = itaEmbeddedData.getCurrentUser();

            if ($scope.currentUser) {
                return true;
            } else {
                return false;
            }
        };

        $scope.logout = function () {
            itaRequest.request({
                url: '/user/logout',
                method: 'post'
            }).then(function() {
                $state.go('home');
                itaEmbeddedData.setCurrentUser(null);
            });
        };
    }
];
