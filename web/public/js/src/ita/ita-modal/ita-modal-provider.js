'use strict';

var angular = require('angular');

module.exports = function () {
    var defaults = this.defaults = {
        titleKey: '',
        content: '',
        buttons: [],
        showCancelButton: true,
        showCloseButton: true,
        showFooter: false,
        show: false,
        backdrop: true,
        destroyOnClose: true,
        width: '50%',
        commonData: {},
        preLoadFunction: null
    };

    this.$get = ['$window', '$rootScope', '$compile',
        function ($window, $rootScope, $compile) {
            return function ItaModal(config) {
                var itaModal = {},
                    options = itaModal.options = angular.extend({}, defaults, config),
                    bodyElement = angular.element($window.document.body),
                    template = require('./ita-modal-template.html'),
                    scope = options.scope && options.scope.$new() || $rootScope.$new(),
                    modalElement,
                    backdropElement;

                scope.titleKey = options.titleKey;
                scope.buttons = options.buttons;
                scope.showCancelButton = options.showCancelButton;
                scope.showCloseButton = options.showCloseButton;
                scope.content = options.content;
                scope.commonData = options.commonData;
                scope.width = options.width;

                scope.onSubmit = function () {
                    scope.$broadcast('onSubmit');
                };

                itaModal.show = function () {
                    if (options.backdrop) {
                        if (!backdropElement) {
                            backdropElement = angular.element('<div class="modal-backdrop"></div>');
                            bodyElement.append(backdropElement);
                        }

                        backdropElement.css({
                            display: 'block'
                        });
                    }

                    if (!modalElement) {
                        modalElement = angular.element(template);
                        $compile(modalElement.contents())(scope);

                        bodyElement.append(modalElement);
                    }

                    if (options.preLoadFunction) {
                        scope.loading = true;

                        options.preLoadFunction().then(function () {
                            scope.loading = false;
                        });
                    }

                    modalElement.css({
                        display: 'block'
                    });

                    scope.$isShown = true;
                };

                itaModal.hide = function () {
                    if (modalElement) {
                        modalElement.css({
                            display: 'none'
                        });
                        scope.$isShown = false;
                    }

                    if (backdropElement) {
                        backdropElement.css({
                            display: 'none'
                        });
                    }

                    if (options.destroyOnClose) {
                        itaModal.destroy();
                    }
                };

                itaModal.toggle = function () {
                    scope.$isShown ? itaModal.hide() : itaModal.show();
                };

                itaModal.destroy = function () {
                    if (modalElement) {
                        modalElement.remove();
                        modalElement = null;
                    }

                    if (backdropElement) {
                        backdropElement.remove();
                        backdropElement = null;
                    }

                    scope.$destroy();
                };

                scope.$hide = function () {
                    scope.$$postDigest(function () {
                        itaModal.hide();
                    });
                };

                scope.$show = function () {
                    scope.$$postDigest(function () {
                        itaModal.show();
                    });
                };

                scope.$toggle = function () {
                    scope.$$postDigest(function () {
                        itaModal.toggle();
                    });
                };

                if (options.show) {
                    itaModal.show();
                }

                return itaModal;
            };
        }
    ];
};
