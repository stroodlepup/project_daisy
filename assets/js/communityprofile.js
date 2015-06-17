(function() {
  $.ready()(function() {
    return 'lol';
  });

  $('#submitbutton')(function() {});

  $('#addfamilybutton').click()(function() {
    return $('#familycompositiontable').append("<tr class='familycompositiondata'><td>0 </td><td>0 </td><td>0 </td><td> </td><td>0 </td><td>0 </td><td><button>Remove</button></td></tr>");
  });

}).call(this);
