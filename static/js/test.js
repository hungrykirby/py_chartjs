const my_func = function(d) {
  data = JSON.parse(d)
  console.log(data);
  var barData = {
    labels : data.a,
    datasets : [{
      label: data.title,
      backgroundColor:[
        "aqua",
        "blue",
        "fuchsia",
        "green",
        "maroon",
        "olive",
        "teal",
        "yellow"
      ],
      data :data.a
    }]
  }
  var mychart = document.getElementById("chart2");
  var chart = new Chart(mychart, {
    type:'doughnut',
    data:barData
  });
};

const my_cal = function(data){
  const d = JSON.parse(data);
  const d_a = d.date_answer
  $(document).ready(function() {

    $('#calender').fullCalendar({
      dayClick: function(date, jsEvent, view) {
        for(var i = 0; i < d_a[1].length; i++){
          if(d_a[0][i] == date.format('YYYY-MM-DD')){
            alert(d_a[1][i])
          }
        }
        //$(this).css('background-color', 'red');
      },
      dayRender: function (date, cell) {
        for(var i = 0; i < d_a[1].length; i++){
          //console.log("1", d_a[0][i] == "2017-06-18");
          //console.log("2", date.format('YYYY-MM-DD'), date.isSame("2017-06-18"));
          //console.log("3", d_a[0][i] == date.format('YYYY-MM-DD'));
          if(d_a[0][i] == date.format('YYYY-MM-DD')){
            cell.css("background-color", "yellow");
          }
        }
      }
    });
  });
}
