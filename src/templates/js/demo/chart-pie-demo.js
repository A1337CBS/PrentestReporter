// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var ydata = [0,0,0,0,0];
var ydata1 = []
ydata1.push(parseInt(document.getElementById("severitiesArray0").value))
ydata1.push(parseInt(document.getElementById("severitiesArray1").value))
ydata1.push(parseInt(document.getElementById("severitiesArray2").value))
ydata1.push(parseInt(document.getElementById("severitiesArray3").value))
ydata1.push(parseInt(document.getElementById("severitiesArray4").value))

ydata = ydata1

var severityColors=["purple","red","orange","blue","green"];
var severities=["Critical","High","Medium","Low","Informative"];
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: severities,
    datasets: [{
      data: ydata,
      backgroundColor: severityColors,
      hoverBackgroundColor: severityColors,
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
