'use strict';

var alertify = require('alertify');

module.exports = [function () {
    var errorMessage = 'An error occurred',
        okButton = 'Ok',
        yesButton = 'Yes',
        cancelButton = 'Cancel';

    this.$get = function () {
        return {
            alert: function (message) {
                alertify.set({
                    labels: {
                        ok: okButton
                    }
                });

                alertify.alert(message);
            },

            error: function (message) {
                alertify.error(message || errorMessage);
            },

            confirm: function (message, callback) {
                alertify.set({
                    buttonReverse: true,
                    labels: {
                        ok: yesButton,
                        cancel: cancelButton
                    }
                });

                alertify.confirm(message, callback);
            }
        };
    };
}];