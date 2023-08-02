const addItem = $('#add_item');
const ulList = $('.my_list');

addItem.click(function () {
  const newItem = $('<li>Item</li>');
  ulList.append(newItem);
});
