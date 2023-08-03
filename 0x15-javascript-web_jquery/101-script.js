$('document').ready(function () {
  const ulList = $('.my_list');
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    ulList.append(newItem);
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    ulList.empty();
  });
});
