var app = angular.module('StickyNotes', [
  'ngRoute','ngTouch'
]).config(['$locationProvider', '$routeProvider',function($locationProvider, $routeProvider){
    // $locationProvider.html5Mode(true);
    ($routeProvider)
        .when('/',{
          // template:"srikanth",
          templateUrl:'/static/notes.html',
            controller:'addNotesToDatabase'
        })
        .when('/viewNotes',{
          templateUrl:'/static/viewNotes.html',
          controller:'getNotesFromDatabase'
        })
        // .otherwise({redirectTo: '/'})
}]);
