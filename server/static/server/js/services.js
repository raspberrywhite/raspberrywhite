angular.module('raspiwhite.services', [])
  .service('raspiwhiteclient', function($http) {

    this.searchSong = function (term, page) {
      var url = '/songs/?term=' + term;
      if (page) {
        url += '&page=' + page;
      }
      return $http.get(url);
    };

    this.getPlaylist = function () {
      return $http.get('/playlist/current');
    };

    this.newRequest = function (id) {
      return $http.post('/request/', $.param({ id_song: id }))
    };

  });