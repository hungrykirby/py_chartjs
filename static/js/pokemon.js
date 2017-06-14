alert("pokemon")
var barData = {
  labels : [{% for item in labels %}
            "{{item}}",
        {% endfor %}],
  datasets : [{
    label: 'Sample',
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(200, 150, 200, 0.8)',
      'rgba(10, 255, 200, 1)',
      'rgba(30, 80, 10, 0.3)'],
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
