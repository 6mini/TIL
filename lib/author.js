var template = require('./template.js');
let db = require('./db');
var url = require('url');

var qs = require('querystring');


exports.home = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
      db.query(`SELECT * FROM author`, function (err2, authors) {
        var title = 'author';
        var list = template.list(topics);
        var html = template.HTML(title, list,
         `
         ${template.authorTable(authors)}
         <style>
            table{
                border-collapse: collapse;
            }
            td{
                border:1px solid black;
            }
         </style>
         <form action="/author_create_process" method="post">
            <p><input type="text" name="name" placeholder="name"></p>
            <p>
                <textarea name="profile" placeholder="profile"></textarea>
            </p>
            <p>
                <input type="submit" value="create">
            </p>
        </form>
         `,
         ``
        );
     response.writeHead(200);
     response.end(html);
    }); 
  });
}

exports.create_process = function(request, response){
    var body = '';
      request.on('data', function (data) {
        body += data;
      });
      request.on('end', function () {
        var post = qs.parse(body);
        db.query(`
              INSERT INTO author (name, profile)
              VALUES(?, ?)`,
          [post.name, post.profile], // 포스트로 받는 부분
          function (err, result) {
            if (err) throw err;
            response.writeHead(302, { Location: `/author` }); // 이 메소드는 추가된 데이터의 아이디값을 의미함.
            response.end();
          }
        )
      });
  }

  exports.update = function (request, response) {
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    db.query(`SELECT * FROM topic`, function (err, topics) {
        db.query(`SELECT * FROM author`, function (err2, authors) {
            db.query(`SELECT * FROM author WHERE id=?`,[queryData.id], function (err3, author) {
                var title = 'author';
                var list = template.list(topics);
                var html = template.HTML(title, list,
                 `
                 ${template.authorTable(authors)}
                 <style>
                    table{
                        border-collapse: collapse;
                    }
                    td{
                        border:1px solid black;
                    }
                 </style>
                 <form action="/author_update_process" method="post">
                    <p><input type="hidden" name="id" value="${queryData.id}"></p>
                    <p><input type="text" name="name" placeholder="name" value="${author[0].name}"></p>
                    <p>
                        <textarea name="profile" placeholder="profile">${author[0].profile}</textarea>
                    </p>
                    <p>
                        <input type="submit" value="update">
                    </p>
                </form>
                 `,
                 ``
                );
             response.writeHead(200);
             response.end(html);
            });
      }); 
    });
  }

  exports.update_process = function(request, response){
    var body = '';
      request.on('data', function (data) {
        body = body + data;
      });
      request.on('end', function () {
        var post = qs.parse(body);
        db.query(`
              UPDATE author SET name=?, profile=? WHERE id=?`,
          [post.name, post.profile, post.id],
          function (err, result) {
            if (err) throw err;
            response.writeHead(302, { Location: `/author` });
            response.end();
          }
        )
      });
  }

  exports.delete_process = function(request, response){
    var body = '';
    request.on('data', function (data) {
      body = body + data;
    });
    request.on('end', function () {
      var post = qs.parse(body);
      db.query(`
            DELETE FROM author WHERE id=?`,
        [post.id],
        function (err, result) {
          if (err) throw err;
          // fs.unlink(`data/${filteredId}`, function(error){
          response.writeHead(302, { Location: `/author` });
          response.end();
        })
    });
  }