//var http = require('http');
//var express = require('express');   //引入express模块
var mysql      = require('mysql');
//var app = express(); 
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'Wawayurdxy-0',
  port:'3306',
  database : 'jiance'
});
 
connection.connect();
 sql='SELECT * FROM test';
var resu;
function getdata(){
  connection.query(sql, function (error, results, fields) {
  if (error)
      {
        console.log('select error',error.message);
        return;
      }
//  console.log('The solution is: ', results);
  resu=results;
//  return resu;
});
 
// connection.end();
return resu;
}
exports.getdata=getdata; 
//app.get('/',function (req,res) {
//str = JSON.stringify(resu);   
// res.send(str);  //服务器响应请求
//});
//connection.end();


