$(document).ready(function () {
  function translate () {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(),
      dataType: 'text',
      success: function (data) {
        $('DIV#hello').html(JSON.parse(data).hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
