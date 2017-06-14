console.log("graph");
var display_graph = function(){
  var barData = {
    labels : [{% for item in labels %}
              "{{item}}",
          {% endfor %}],
    datasets : [{
      label: 'Sample',
      /*backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(200, 150, 200, 0.8)',
        'rgba(10, 255, 200, 1)',
        'rgba(30, 80, 10, 0.3)'],*/
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
      data : [{% for item in values %}
                    {{item}},
                  {% endfor %}]
    }]
  }
  var mychart = document.getElementById("chart");
  var chart = new Chart(mychart, {
    type:'doughnut',
    data:barData
  });
}
