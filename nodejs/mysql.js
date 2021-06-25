let mysql      = require('mysql');
let connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'nodejs',
  password : '11111111',
  database : 'opentutorials'
});
 
connection.connect(); // 접속
 
connection.query('SELECT * FROM topic', function (err, results, fields) {
  if (err) throw err;
  console.log(results);
}); 
 
connection.end();