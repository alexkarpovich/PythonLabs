'use strict';

var angular = require('angular');

module.exports = function () {
    var baseUrl = '',
        defaultConfig = {
            cache: false
        };

    this.baseUrl = function (url) {
        baseUrl = url;
    };

    this.$get = ['$http', '$q', 'itaModal', 'itaMessenger', 'itaEmbeddedData', 'itaLoading',
        function ($http, $q, itaModal, itaMessenger, embeddedData, itaLoading) {
            var respond = function (deferred, callback) {
                return function (data, status, headers) {
                    var contentType = headers('content-type') || '',
                        response;

                    if (contentType.indexOf('application/json') !== 0) {
                        if (embeddedData.getEnvironment() === 'production') {
                            return deferred.reject({
                                meta: {
                                    status: 500,
                                    errors: ['wrong response content type']
                                },
                                data: data
                            });
                        } else {
                            itaModal({
                                titleKey: 'An error occurred',
                                content: '<div>' + data + '</div>',
                                show: true,
                                width: '90%'
                            });
                        }
                    }

                    if (!data) {
                        return callback();
                    }

                    response = data.data || {};
                    response.meta = data.meta || {
                        status: 500,
                        errors: ['wrong response format']
                    };
                    response.meta.headers = headers || null;

                    if (data.meta.status !== 200) {
                        if (data.meta.status === 500 || data.meta.status === 404) {
                            if (embeddedData.getEnvironment() === 'production') {
                                itaMessenger.error('An error occurred');
                            } else {
                                itaModal({
                                    titleKey: 'An error occurred',
                                    content: '<div>' + data.meta.errors.join('<br>') + '</div>',
                                    show: true,
                                    width: '90%'
                                });
                            }
                        }

                        return deferred.reject(response);
                    }

                    itaLoading.hideLoading();

                    callback(response);
                };
            };

            return {
                baseUrl: function () {
                    return baseUrl;
                },

                request: function (config) {
                    var deferred = $q.defer();

                    config = angular.extend({}, defaultConfig, config);
                    config.url = baseUrl + config.url;

                    if (!config.data) {
                        config.data = {};
                    }
                    config.data.csrf = embeddedData.getCsrf();

                    itaLoading.showLoading();

                    $http(config)
                        .success(respond(deferred, deferred.resolve))
                        .error(respond(deferred, deferred.reject));

                    return deferred.promise;
                }
            };
        }
    ];
};
