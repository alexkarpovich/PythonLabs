'use strict';

var domready = require('domready'),
    angular = require('angular');

require('./ita/ita-request/ita-request');
require('./ita/ita-embedded-data/ita-embedded-data');
require('./ita/ita-form/ita-form');
require('./ita/ita-loading/ita-loading');
require('./ita/ita-messenger/ita-messenger');
require('./ita/ita-datepicker/ita-datepicker');
require('./ita/ita-modal/ita-modal');
require('./menu/top-menu/top-menu');
require('./user/user');
require('./admin/admin');

domready(function () {
    angular
        .module('Main', [
            'ui.router',
            'ui.bootstrap',
            'ItaRequest',
            'ItaEmbeddedData',
            'ItaForm',
            'ItaLoading',
            'ItaMessenger',
            'ItaDatePicker',
            'ItaModal',
            'TopMenu',
            'User',
            'Admin'
        ])
        .config([
            'itaRequestProvider',
            'itaEmbeddedDataProvider',
            '$stateProvider',
            function(itaRequestProvider, itaEmbeddedDataProvider, $stateProvider) {
                itaRequestProvider.baseUrl(window.location.protocol + '//local.italabs.dev');

                itaEmbeddedDataProvider.embeddedData(window.ita);

                $stateProvider
                    .state('home', {
                        url: '/',
                        template: require('./home/home.html')
                    });
            }
        ]);

    angular.bootstrap(document, ['Main']);
});
