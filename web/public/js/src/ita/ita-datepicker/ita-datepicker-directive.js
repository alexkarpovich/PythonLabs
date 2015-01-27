'use strict';

module.exports = [
    function() {
        return {
            restrict: 'E',
            scope: {
                dt:'=ngModel'
            },
            replace: false,
            template: require('./ita-datepicker-template.html'),
            controller: 'ItaDatePickerController'
        }
    }
];
