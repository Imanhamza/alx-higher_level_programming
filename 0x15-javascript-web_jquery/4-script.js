const hElement = $('header');
const toggleHeader = $('#toggle_header');
toggleHeader.click(function () {
  hElement.toggleClass('red green');
});
