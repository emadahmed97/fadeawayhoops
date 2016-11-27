var fadeawayhoops = angular.module('fadeawayhoops',['ngRoute','Controllers'])

fadeawayhoops.config([
  '$routeProvider',
  function($routeProvider) {
    $routeProvider.
        when('/blogposts/:postId') {
          templateUrl: '/templates/blogposts/posts.html',
          controller: 'postController'
        });



  }
]);

fadeawayhoops.config([

    '$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    }


]);
