'use strict';

var _ = require('lodash');

module.exports = [
    function () {
        return {
            restrict: 'E',
            transclude: true,
            scope: {
                fieldName: '@',
                fieldLabel: '@'
            },
            require: '^itaForm',
            template: require('./ita-form-row.html'),
            controller: ['$scope', function ($scope) {
                $scope.hasErrors = function() {
                    var formScope = $scope.$parent.$$prevSibling,
                        form = formScope[formScope.formName],
                        field = form[$scope.fieldName];

                    if (_.has(formScope.errorMessages, $scope.fieldName)) {
                        $scope.errorMessages = formScope.errorMessages[$scope.fieldName];
                    }

                    return formScope.isSubmitted() && !field.$valid;
                };
            }]
        };
    }
];
