angular.module('raspiwhite.controllers', ['raspiwhite.services'])

.controller('RaspiWhiteController', function($scope, notifier) {
  $scope.current_space = {
    nav: '',
    title: 'Raspiwhite'
  }
  notifier.configure({
    positionClass: "toast-bottom-right"
  });
})

.controller('RegisterController', function($scope) {
  $scope.current_space.title = 'Register';
})

.controller('LoginController', function($scope) {
  $scope.current_space.title = 'Raspiwhite';
})

.controller('PlaylistController', function ($scope, raspiwhiteclient) {
  $scope.current_space.nav = 'playlist';
  $scope.current_space.title = 'Playlist';
  function load_playlist() {
    raspiwhiteclient.getPlaylist()
    .success(function(data) {
      $scope.songs = data;
    });
  }
  var source = new EventSource("/sse/foo");
  source.addEventListener('newsong', function(e) {
    load_playlist();
  }, false);
  load_playlist();
})

.controller('RequestController', function ($scope, $location, raspiwhiteclient, notifier) {
  $scope.current_space.nav = 'request';
  $scope.current_space.title = 'New request';
  $scope.pages = new Array();
  $scope.current_page = 0;
  $scope.query = '';

  $scope.$on('$locationChangeSuccess', function () {
    var parameters = $location.search();
    if (parameters.page)
      $scope.current_page = parameters.page - 1;
    if (parameters.query)
      $scope.query = parameters.query;

    executeSearchWithPage($scope.query, $scope.current_page + 1);
  });

  function executeSearch(term) {
    executeSearchWithPage($scope.query, 1);
  }

  function executeSearchWithPage(term, page) {
    raspiwhiteclient.searchSong(term, page)
    .success(function(data) {
      $scope.songs = data['results'];
      $scope.pages = new Array();
      for (i = 0 ; i < data.total_pages ; i++) {
        $scope.pages.push({'number' : i + 1, 'active' : false});
      }
      $scope.pages[$scope.current_page]['active'] = true;
    });
  }

  executeSearchWithPage($scope.query, $scope.current_page + 1);

  $scope.firstPage = function() {
    return ($scope.current_page == 0);
  }

  $scope.isSinglePage = function() {
    return ($scope.pages.length == 1);
  }

  $scope.lastPage = function() {
    return ($scope.current_page == $scope.pages.length - 1);
  }

  $scope.search = function() {
    executeSearch($scope.query);
  }

  $scope.sendrequest = function(song) {
    $current_song = song;
    $current_song.is_loading = true;
    raspiwhiteclient.newRequest($current_song.id)
    .success(function(data) {
      $current_song.is_loading = false;
      notifier.success(data.status);
    })
    .error(function(data) {
      $current_song.is_loading = false;
      if (data.status !== undefined)
        notifier.error(data.status);
    });
  }
});
