
var app = angular.module('ItemLister',['ngRoute']);

app.congif(['$routeProvider', function($routeProvider){
	$routeProvider
	.when('/list',{
		templateUrl:'html/list.html',
		controller:'listController'
	});
}]);

app.run(function ($rootScope){
	$rootScope.lock = false;
	$rootScope.list = [];
	//do a http request to get the shopping list
	
	$rootScope.list = [{"name":"Dish washing soap",
						"info":"I think I like the orange smelling better",
						"price": 1.99},
						{"name":"Toothpast",
						"info":"Always nice to have some",
						"price": 3.99}
					];
	$rootScope.appName = "ItemLister";
	$rootScope.appOptions=[];
	//do a http request to get the possible different options
	$rootScope.appOptions = ["Shopping", "Add To List", "Add Photo"];
});