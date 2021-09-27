//여기저기 쓰일거니까 mysql을 처리해줘야함.
let mysql = require('mysql');
let db = mysql.createConnection({ 
    host     : 'localhost',
    user     : 'nodejs',
    password : '11111111',
    database : 'opentutorials'
  });
  db.connect(); // 실제 접속이 일어남;
  module.exports = db;//외부에서 쓸수있도록 익스포트