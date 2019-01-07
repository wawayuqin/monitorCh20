var path = require("path");
var ejs = require('ejs');  
var express = require("express");
var app = express();
var routers=require("./routers/mainRouter/router");
app.set('view engine', 'ejs');
//app.set('views',path.jion(__dirname,'views'));
// 3
app.engine('html', ejs.renderFile);
//app.get('/', function(req, res){
//    res.render('index.html');
//});
routers.router(app);
//app.get('/about', function(req, res){
  //  res.render('about.html');
//});
//app.get('/', function(req, res){
//    res.send("Hello World!");
//});
var server = app.listen(8000, function(){
    console.log("Server is running on http://localhost:8000");
});
