//api를 여러개로 할거면 익스포츠만 쓰면 댐
var template = require('./template.js');
let db = require('./db');
var url = require('url');
var qs = require('querystring');


exports.home = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
    var title = 'Welcome';
    var description = 'Hello, Node.js';
    var list = template.list(topics);
    var html = template.HTML(title, list,
      `<h2>${title}</h2>${description}`,
      `<a href="/create">create</a>`
    );
    response.writeHead(200);
    response.end(html);
  });
}

exports.page = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    if (err) throw err;
    db.query(`SELECT * FROM topic LEFT JOIN author ON topic.author_id=author.id WHERE topic.id=?`, [queryData.id], function (err2, topic) { // ?를 주고 두번째 인자에 배열로 담아서 주면 보안적으로 좋다. ?를 치환함.
      if (err2) throw err2;
      var title = topic[0].title;
      var description = topic[0].description;
      var list = template.list(topics);
      var html = template.HTML(title, list,
        `<h2>${title}</h2>${description}
              <p>by ${topic[0].name}</p>
              `,
        `<a href="/create">create</a>
                <a href="/update?id=${queryData.id}">update</a>
                <form action="delete_process" method="post">
                  <input type="hidden" name="id" value="${queryData.id}">
                  <input type="submit" value="delete">
                </form>`
      );
      response.writeHead(200);
      response.end(html);
    });
  });
}

exports.create = function (request, response) {
  db.query(`SELECT * FROM topic`, function (err, topics) {
    db.query(`SELECT * FROM author`, function (err2, authors) {
      var title = 'Create';
      var list = template.list(topics);
      var html = template.HTML(title, list,
        `
        <form action="/create_process" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p>
        <textarea name="description" placeholder="description"></textarea>
      </p>
      <p>
        ${template.authorSelect(authors)}
      </p>
      <p>
        <input type="submit">
      </p>
    </form>
        `, '');
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
            INSERT INTO topic (title, description, created, author_id)
            VALUES(?, ?, NOW(), ?)`,
        [post.title, post.description, post.author], // 포스트로 받는 부분
        function (err, result) {
          if (err) throw err;
          response.writeHead(302, { Location: `/?id=${result.insertId}` }); // 이 메소드는 추가된 데이터의 아이디값을 의미함.
          response.end();
        }
      )
    });
}

exports.update = function(request, response){
  var _url = request.url;
  var queryData = url.parse(_url, true).query;
  db.query(`SELECT * FROM topic`, function (err, topics) {
    if (err) throw err;
    db.query(`SELECT * FROM topic WHERE id=?`, [queryData.id], function (err2, topic) {
      if (err2) throw err2;
      db.query(`SELECT * FROM author`, function (err3, authors) {
        if (err3) throw err3;
        var list = template.list(topics);
        var html = template.HTML(topic[0].title, list,
          `
          <form action="/update_process" method="post">
            <input type="hidden" name="id" value="${topic[0].id}">
            <p><input type="text" name="title" placeholder="title" value="${topic[0].title}"></p>
            <p>
              <textarea name="description" placeholder="description">${topic[0].description}</textarea>
            </p>
            <p>
            ${template.authorSelect(authors, topic[0].author_id)}
            </p>
            <p>
              <input type="submit">
            </p>
          </form>
          `,
          `<a href="/create">create</a> <a href="/update?id=${topic[0].id}">update</a>`
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
            UPDATE topic SET title=?, description=?, author_id=? WHERE id=?`,
        [post.title, post.description, post.author, post.id],
        function (err, result) {
          if (err) throw err;
          response.writeHead(302, { Location: `/?id=${post.id}` });
          response.end();
        }
      )
    });
}

exports.delete = function(request, response){
  var body = '';
  request.on('data', function (data) {
    body = body + data;
  });
  request.on('end', function () {
    var post = qs.parse(body);
    db.query(`
          DELETE FROM topic WHERE id=?`,
      [post.id],
      function (err, result) {
        if (err) throw err;
        // fs.unlink(`data/${filteredId}`, function(error){
        response.writeHead(302, { Location: `/` });
        response.end();
      })
  });
}