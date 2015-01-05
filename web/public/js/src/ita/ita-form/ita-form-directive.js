'use strict';

var angular = require('angular'),
    _ = require('lodash');

module.exports = [function () {
        return {
            restrict: 'E',
            transclude: true,
            scope: {
                formName: '@',
                submit: '&',
                submitSuccess: '&?',
                submitError: '&?'
            },
            template: require('./ita-form.html'),
            controller: ['$scope', function($scope) {
                var submitted = false;

                $scope.isSubmitted = function () {
                    return submitted;
                };

                $scope.onSubmit = function() {
                    submitted = true;

                    if ($scope[$scope.formName].$valid) {
                        $scope.submit().then(
                            function(data) {
                                $scope.errorMessages = {};

                                angular.forEach($scope[$scope.formName], function(field, fieldName) {
                                    if (fieldName[0] !== '$') {
                                        $scope[$scope.formName][fieldName].$valid = true;
                                    }
                                });

                                if ($scope.submitSuccess) {
                                    $scope.submitSuccess({data: data});
                                }
                            },
                            function(data) {
                                if (data.meta.status === 400) {
                                    angular.forEach($scope[$scope.formName], function(field, fieldName) {
                                        if (fieldName[0] !== '$') {
                                            $scope[$scope.formName][fieldName].$valid = true;
                                        }
                                    });

                                    $scope.errorMessages = data.meta.errors;

                                    angular.forEach(data.meta.errors, function(errors, fieldName) {
                                        if (_.has($scope[$scope.formName], fieldName) &&
                                            $scope[$scope.formName][fieldName][0] !== '$') {
                                            $scope[$scope.formName][fieldName].$valid = false;
                                        }
                                    });

                                    if ($scope.submitError) {
                                        $scope.submitError({data: data});
                                    }
                                }
                            }
                        );
                    }
                };
            }]
        };
    }
];
