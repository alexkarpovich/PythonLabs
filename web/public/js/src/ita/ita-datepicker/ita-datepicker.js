'use strict';

var angular = require('angular');

angular
    .module('ItaDatePicker',[])
    .controller('ItaDatePickerController', require('./ita-datepicker-controller'))
    .directive('itaDatepicker', require('./ita-datepicker-directive'));
