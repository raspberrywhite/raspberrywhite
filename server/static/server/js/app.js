function startRaspberryWhite(csfr_token) {
  var app = angular.module( 'Raspiwhite', ['raspiwhite.controllers'] );

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = csfr_token;
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  }]);

  app.config(['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
  }]);
}
