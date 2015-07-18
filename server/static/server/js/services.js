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

  })

  .service('notifier', function($http) {

    this.configure = function(options) {
      toastr.options = {
        "positionClass": options.positionClass,
      };
    }

    this.success = function (data) {
      toastr.success(data);
    };

    this.error = function (data) {
      toastr.error(data);
    };

  });
