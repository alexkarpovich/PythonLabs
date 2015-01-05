'use strict';

module.exports = [
    function () {
        return {
            restrict: 'E',
            replace: true,
            template: require('./top-menu.html'),
            controller: require('./top-menu-controller'),
            scope: {}
        };
    }
];
