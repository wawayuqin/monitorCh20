var getnd=require('./getdatabase');
var router = function(app){
    app.get('/', function(req, res){
        result=getnd.getdata();
        res.render('../views/index.html',{nongdu:result});
    });

    app.get('/about', function(req, res){
        res.render('../views/about.html');
    });
};

exports.router = router;
