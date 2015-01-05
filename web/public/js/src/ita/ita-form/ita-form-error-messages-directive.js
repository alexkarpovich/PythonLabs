'use strict';

module.exports = [
    function () {
        return {
            restrict: 'E',
            scope: {
                messages: '='
            },
            template: require('./ita-form-error-messages.html')
        };
    }
];
