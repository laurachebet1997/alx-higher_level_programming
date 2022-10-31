$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(),
      dataType: 'text',
      success: function (data) {
        $('DIV#hello').text(JSON.parse(data).hello);
      }
    });
  });
});
