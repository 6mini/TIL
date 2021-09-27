module.exports = {
  HTML:function(title, list, body, control){
    return `
    <!doctype html>
    <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB</a></h1>
      <a href="/author">author</a>
      ${list}
      ${control}
      ${body}
    </body>
    </html>
    `;
  },list:function(topics){
    var list = '<ul>';
    var i = 0;
    while(i < topics.length){
      list = list + `<li><a href="/?id=${topics[i].id}">${topics[i].title}</a></li>`;
      i = i + 1;
    }
    list = list+'</ul>';
    return list;
  },authorSelect:function(authors, author_id){
    let tag = '';
    for (let i = 0; i < authors.length; i++) {
      let selected = '';
      if(author_id === authors[i].id){
        selected = ' selected'
      }
    tag += `<option value="${authors[i].id}"${selected}>${authors[i].name} </option>`;
    }
    return `
      <select name="author">
        ${tag}
      </select>
      `
  },authorTable:function(authors){
    let tag = '<table>';
    for (let i = 0; i < authors.length; i++) {
      tag += `
        <tr>
            <td>${authors[i].name}</td>
            <td>${authors[i].profile}</td>
            <td><a href='/author_update?id=${authors[i].id}'>update</a></td>
            <td>
            <form action="author_delete_process" method="post">
                  <input type="hidden" name="id" value="${authors[i].id}">
                  <input type="submit" value="delete">
                </form>
            </td>
        </tr>
    `//삭제는 무조건 폼으로 해야함.
    }
    tag += '</table>'
    return `${tag}`
  }
}
