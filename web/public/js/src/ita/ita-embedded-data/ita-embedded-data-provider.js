'use strict';

module.exports =  function () {
    var embeddedData = {};

    this.embeddedData = function (value) {
        embeddedData = value;
    };

    this.$get = function () {
        return {
            getCurrentUser: function () {
                return embeddedData.currentUser;
            },

            setCurrentUser: function (currentUser) {
                embeddedData.currentUser = currentUser;
            },

            getCsrf: function () {
                return embeddedData.csrf;
            },

            getCurrentLanguageKey: function () {
                return embeddedData.currentLanguageKey;
            },

            setCurrentLanguageKey: function (currentLanguageKey) {
                embeddedData.currentLanguageKey = currentLanguageKey;
            },

            getEnabledLanguages: function () {
                return embeddedData.enabledLanguages;
            },

            setEnabledLanguages: function (enabledLanguages) {
                embeddedData.enabledLanguages = enabledLanguages;
            },

            getDefaultLanguageKey: function () {
                return embeddedData.defaultLanguageKey;
            },

            setDefaultLanguageKey: function (defaultLanguageKey) {
                embeddedData.defaultLanguageKey = defaultLanguageKey;
            },

            getEnvironment: function ()
            {
                return embeddedData.env;
            }
        };
    };
};
