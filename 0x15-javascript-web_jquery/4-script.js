// Write a Javascript script that toggles the class of the HTML tag HEADER to red
// when the user clicks on the tag DIV#toggle_header
$('#toggle_header').click(function () {
  $('HEADER').toggleClass('red green');
});
