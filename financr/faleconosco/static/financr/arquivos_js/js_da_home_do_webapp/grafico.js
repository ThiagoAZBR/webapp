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

let circulo1 = document.querySelector('#circulo_1')
let circulo2 = document.querySelector('#circulo_2')
let circulo3 = document.querySelector('#circulo_3')

let grafico_pizza     =  document.querySelector('#graficopizza')
let grafico_despesas  =  document.querySelector('#graficodespesas')
let grafico_receitas  =  document.querySelector('#graficoreceitas')

let txt_pizza   = document.querySelector('#txt_pizza')
let txt_despesa = document.querySelector('#txt_despesa')
let txt_receita = document.querySelector('#txt_receita')

let lista = [grafico_despesas, grafico_pizza, grafico_receitas]
let lista2 = [txt_pizza, txt_receita, txt_despesa]

let max = lista.length

circulo1.addEventListener('click', function() {


    for (let i = 0;; i++) {

        if (i >= max) break;

        lista[i].style.display = 'none'
        lista2[i].style.display = 'none'

    }

    grafico_pizza.style.display = 'flex'
    txt_pizza.style.display = 'block'

})


circulo2.addEventListener('click', function() {


    for (let i = 0;; i++) {

        if (i >= max) break;

        lista[i].style.display = 'none'
        lista2[i].style.display = 'none'
    
    }

    grafico_despesas.style.display = 'flex'
    txt_despesa.style.display = 'block'

})


circulo3.addEventListener('click', function() {


    for (let i = 0;; i++) {

        if (i >= max) break;


        lista[i].style.display = 'none'
        lista2[i].style.display = 'none'


    
    }

    grafico_receitas.style.display = 'flex'
    txt_receita.style.display = 'block'

})


