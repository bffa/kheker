var fs = require("fs");
var mysql = require('mysql');
var env = require('./environment.js');
var metrixs = {};
var poolInfo = {
				connectionLimit : env.dbc,
                host : env.dbh,
                user : env.dbu,
                password : env.dbp,
                database : env.dbn
				};
var pool = mysql.createPool(poolInfo);
function respond(jsonInfo, response, code){
	response.writeHead(code, {'Content-Type':'text/plain',
							  'Access-Control-Allow-Orgin': '*',
							  'Access-Control-Allow-Headers':'Origin, X-Requested-With, Content-Type, Accept'});
	try{
		response.end(JSON.stringify(jsonInfo));
	}
	catch(err){
		console.log("Error with json.stringify in respond");
		response.end("{'Error': 'error with respond'}");
	}
};

exports.stressTest= function(info, response){
	try{res = {'received':info.val+1};	
		respond(res, response, 200);
	}
	catch(err){
		console.log("stressTest err: "+ err);
		respond({'error':'stressTest fail '}, response, 200);
	}
};

exports.metrix = function(metric){
	try{
		if (metrixs.hasOwnProperty(metric)){
			console.log("added unique metric");
			metrixs[metric] = 0;
		}
		metrixs[metric] = metrixs[metric] + 1;
		fs.writeFile("node_server.log",JSON.stringify(metrixs));
	}
	catch(err){
		console.log(err);

	}	
};

exports.login = function(info, response){
	try{
	}
	catch(err){
		console.log("login err: "+err);
		respond({'Error':'error in login'}, response, 200);
	}
};