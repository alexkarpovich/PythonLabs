'use strict';

module.exports = ['$compile',
    function ($compile) {
        return {
            restrict: 'E',
            scope: false,

            link: function (scope, element) {
                element.html(scope.content);
                $compile(element.contents())(scope);
            }
        };
    }
];
