/*
var mysql = require('mysql');

var connection = mysql.createConnection({
    host: "localhost",
    user: "viewer",
    password: "youcannotedit-69",
    database: "blog"
});

connection.connect(function(err){
    if (err) throw err;
    connection.query("SELECT * FROM posts", function(err, result, fields) {
        if (err) throw err;
        console.log(result);

    });
});
*/



var article = ""

for (i=0; i<result.length; i++)
{
    article = article + "<tr>";
    for (a=0; a<result[i].length; a++)
    {
        article = article + "<td>" + result[i][a] + "</td>";
    }
    article = article + "</tr>";
}

document.getElementById("blog").innerHTML = article;