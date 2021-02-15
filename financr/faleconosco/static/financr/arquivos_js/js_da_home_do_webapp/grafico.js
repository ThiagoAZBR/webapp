// google.charts.load('current', {packages: ['corechart']});
// google.charts.setOnLoadCallback(drawChart);
// google.charts.setOnLoadCallback(graficodespesas);
// google.charts.setOnLoadCallback(graficoreceitas);

// function drawChart(){

//     let a = ('{{graficobancos | safe}}');

//     const container = document.querySelector('#graficopizza')
//     const data = new google.visualization.arrayToDataTable(JSON.parse(a))
    
//     const options = {
//         title: 'Saldo por banco',
//         height:500,
//         weight:500,
//     }

//     const chart = new google.visualization.PieChart(container)
//     chart.draw(data, options)
// }