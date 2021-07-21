const express = require('express') //모듈로드
const app = express()
const port = 3000;
const fs = require('fs');
const template = require('./lib/template.js');
const path = require('path');
const sanitizeHtml = require('sanitize-html');
const qs = require('querystring');
const bodyParser = require('body-parser');
const compression = require('compression');
const { req } = require('http');
var helmet = require('helmet')
app.use(helmet())

app.use(express.static('public'))
app.use(bodyParser.urlencoded({ extended: false })); //미들웨어가 들어옴
app.use(compression()); //용량을 압축해주는 기능
app.get('*',function(req, res, next){ //겟방식에만 미들웨어가 적용
  fs.readdir('./data', (err, filelist) => {
    req.list = filelist;
    next();
  });
});

//어떻게 라우트하는가

app.get('/', (req, res) => {
    var title = 'Welcome';
    var description = 'Hello, Node.js';
    var list = template.list(req.list);
    var html = template.HTML(title, list,
      `<h2>${title}</h2>${description}
      <img src="/imeges/coding.jpg" style="width:300px; display:block; margin-top:10px;">`,
      `<a href="/create">create</a>`
    );
    res.send(html);
})

app.get('/page/:pageId', (req, res, next) => { //쿼리스트링이 아닌 패쓰방식으로.
    var filteredId = path.parse(req.params.pageId).base;
    fs.readFile(`data/${filteredId}`, 'utf8', function(err, description){
      if(err){
        next(err);
      } else {
        var title = req.params.pageId;
        var sanitizedTitle = sanitizeHtml(title);
        var sanitizedDescription = sanitizeHtml(description, {
          allowedTags:['h1']
        });
        var list = template.list(req.list);
        var html = template.HTML(sanitizedTitle, list,
          `<h2>${sanitizedTitle}</h2>${sanitizedDescription}`,
          ` <a href="/create">create</a>
            <a href="/update/${sanitizedTitle}">update</a>
            <form action="/delete" method="post">
              <input type="hidden" name="id" value="${sanitizedTitle}">
              <input type="submit" value="delete">
            </form>`
        );
      }
      res.send(html);
    });
});

app.get('/create', function(req, res){
    var title = 'WEB - create';
    var list = template.list(req.list);
    var html = template.HTML(title, list, `
      <form action="/create" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p>
          <textarea name="description" placeholder="description"></textarea>
        </p>
        <p>
          <input type="submit">
        </p>
      </form>
    `, '');
    res.send(html);
});

app.post('/create', function(req, res){ //get이 아닌 post로 해야함.
  const post = req.body;
  const title = post.title;
  const description = post.description;
  fs.writeFile(`data/${title}`, description, 'utf8', function(err){
    res.redirect(`/page/${title}`
  )});
});

app.get('/update/:pageId', function(req, res){
    const filteredId = path.parse(req.params.pageId).base;
    fs.readFile(`data/${filteredId}`, 'utf8', function(err, description){
      const title = req.params.pageId;
      const list = template.list(req.list);
      const html = template.HTML(title, list,
        `
        <form action="/update" method="post">
          <input type="hidden" name="id" value="${title}">
          <p><input type="text" name="title" placeholder="title" value="${title}"></p>
          <p>
            <textarea name="description" placeholder="description">${description}</textarea>
          </p>
          <p>
            <input type="submit">
          </p>
        </form>
        `,
        `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`
      );
      res.send(html);
    });
});

app.post('/update', function(req, res){
  const post = req.body;
  const id = post.id;
  const title = post.title;
  const description = post.description;
  fs.rename(`data/${id}`, `data/${title}`, function(err){
    fs.writeFile(`data/${title}`, description, 'utf8', function(err){
      res.redirect(`/page/${title}`);
    })
  });
});

app.post('/delete', function(req, res){
  const post = req.body; // 바디파서
  const id = post.id;
  const filteredId = path.parse(id).base;
  fs.unlink(`data/${filteredId}`, function(error){
    res.redirect('/');
  });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

app.use((req, res, next) => { //에러처리
  res.status(404).send("Sorry can't find that!")
})


//미들웨어 바디파써
