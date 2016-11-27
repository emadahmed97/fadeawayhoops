var fadeawayControllers = angular.module('fadeawayControllers', []);


fadeawayControllers.controllers('PostDetailController', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
      $http.get('/blogposts/api/posts/' + $routeParams.postId + '/?format=json').success(function(data)){
      $scope.post = data;
      });
    }
 ])
