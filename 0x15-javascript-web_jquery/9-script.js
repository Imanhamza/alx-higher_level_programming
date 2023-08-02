const helloDiv = $('DIV#hello');
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(url, function (data) {
  const helloTrans = data.hello;

  helloDiv.text(helloTrans);
});
