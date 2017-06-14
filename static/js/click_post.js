var click_event = function() {
  var textData = JSON.stringify({"text":$("#input-text").val()});
  $.ajax({
    type:'POST',
    url:'/change',
    data:textData,
    contentType:'application/json',
    success:function(data) {
      var result = JSON.parse(data.ResultSet).result;
      $("#hello").text(result);
    }
  });
}
