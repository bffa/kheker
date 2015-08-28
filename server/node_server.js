var http = require('http');
var fs = require('fs');
var sys = require('sys');
var env = require('./environment');
var ut = require('./util');

http.createServer(function(request, respond){
	console.log("url: "+request.url);
	try{
		if(request.url === "/list"){
			var info = "";
			request.on('data', function(data){
				info = info+data;
			});
			request.on('end', function(){
				info = JSON.parse(info);
			});
			respond.end("{'tasks':'todo'}");
		}
		else if(request.url === "/stressTest"){
			//ut.metrix("stressTest");
			var info = "";
			request.on('data', function(data){
				info = info+data;
			});
			request.on('end', function(){
				try{info = JSON.parse(info);
				//console.log(info);
				ut.stressTest(info, respond);
			}
				catch(err){
					console.log('/stressTest err: '+err);
					respond.end("{'error':'parseFail'}");
				}
			});
		}
		else if(request.url === '/login'){
			var info ="";
			request.on('data', function(data){
				info = info + data;
			});
			request.end('end', function(){
				try{
					info=JSON.parse(info);
					ut.login(info, respond);
				}
				catch(err){
					console.log('/login err: '+err);
					respond.end("{'error':'parseFail'");
				}
			});
		}
		else{
			respond.end("{'message':'Welcome'}");
		}
	}
	catch(err){
		console.log("try1: "+err);
	}
}).listen(env.port, env.access);
console.log("runnding on "+env.port);