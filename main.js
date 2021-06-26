var http = require('http');
var url = require('url');
var qs = require('querystring');
var template = require('./lib/template.js');
let db = require('./lib/db');
let topic = require('./lib/topic');
let author = require('./lib/author');

var app = http.createServer(function (request, response) {
  var _url = request.url;
  var queryData = url.parse(_url, true).query;
  var pathname = url.parse(_url, true).pathname;
  if (pathname === '/') { //본문
    if (queryData.id === undefined) {
      topic.home(request, response);
    } else { //상세보기
      topic.page(request, response);
    } 
  } else if (pathname === '/create') { //생성
    topic.create(request, response);
  } else if (pathname === '/create_process') {
    topic.create_process(request, response);
  } else if (pathname === '/update') {
    topic.update(request, response);
  } else if (pathname === '/update_process') {
    topic.update_process(request, response);
  } else if (pathname === '/delete_process') {
    topic.delete(request, response);
  } else if (pathname === '/author') {
    author.home(request, response);
  } else if (pathname === '/author_create_process') {
    author.create_process(request, response);
  } else if (pathname === '/author_update') {
    author.update(request, response);
  } else if (pathname === '/author_update_process') {
    author.update_process(request, response);
  } else if (pathname === '/author_delete_process') {
    author.delete_process(request, response);
  } else {
    response.writeHead(404);
    response.end('Not found');
  }
});
app.listen(3000);


/*
검색기능을 만들어봐야함
겟 방식으로 전송.
색인기능
페이지기능 : 리미트

*/
