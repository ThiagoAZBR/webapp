mostrar = true

expandir = true

const opcoes_icone_usuario = document.querySelector('.opcoes_icone_usuario')
const icone_usuario = document.querySelector('#icone_usuario')

let tela_saldo = document.querySelector('.tela_saldo')
let tela_graficos = document.querySelector('.tela_graficos')
let tela_criar_conta = document.querySelector('.tela_criar')
let tela_transferencias = document.querySelector('.tela_transferencias')

let divs_expansao = document.querySelectorAll('.telas_e_expansao div')

let telas_do_app = [tela_saldo, tela_graficos, tela_criar_conta, tela_transferencias]

let telas_expansionadas = document.querySelector('.telas_e_expansao')

let max_telas_do_app = telas_do_app.length

let maximo = divs_expansao.length
let dados_usuario = document.querySelector('#dados')
let conf_usuario = document.querySelector('.conf_usuario')

// Imagens Abaixo
let img_saldo = document.querySelector('#img_saldo')
let img_grafico = document.querySelector('#img_grafico')
let img_criar_conta = document.querySelector('#img_criar_conta')
let img_transferencia = document.querySelector('#img_transferencia')

let div_titulo_saldo = document.querySelector('#titulo_saldo')
let div_titulo_grafico = document.querySelector('#titulo_grafico')
let div_titulo_conta = document.querySelector('#titulo_conta')
let div_titulo_transferencia = document.querySelector('#titulo_transferencia')

let fechar = document.querySelector('#txt_fechar')
let fechar2 = document.querySelector('#txt_fechar2')
let fechar3 = document.querySelector('#txt_fechar3')
let fechar4 = document.querySelector('#txt_fechar4')


let xiz = document.querySelector('.xiz')



// Transformar de None para Block, ou Block para None

icone_usuario.addEventListener('click', () => {

    opcoes_icone_usuario.classList.toggle('on', mostrar)
    
    if (conf_usuario.className.indexOf('on') != -1) {

        conf_usuario.classList.remove('on')

    }

    mostrar = !mostrar
    

})

revelar = true

// Settings

dados_usuario.addEventListener('click', () => {

    conf_usuario.classList.toggle('on', revelar)

    revelar = !revelar

})


// Clicar E Expandir


img_saldo.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

    tela_saldo.classList.toggle('on', expandir) 
    expandir = !expandir

    telas_do_app.forEach(function (iterador2){
        if ($(iterador2).hasClass("on")) {
            telas_do_app.forEach(function(iterador_interno2) {
                iterador_interno2.style.width = '150px'
                iterador_interno2.style.height = '15vh'
            })
            div_titulo_conta.style.display = 'none'
            div_titulo_grafico.style.display = 'none'
            div_titulo_saldo.style.display = 'none'
            div_titulo_transferencia.style.display = 'none'
            telas_expansionadas.style.gridTemplateRow = '1fr'
        }
    })


})



img_grafico.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

    tela_graficos.classList.toggle('on', expandir) 
    expandir = !expandir

    telas_do_app.forEach(function (iterador2){
        if ($(iterador2).hasClass("on")) {
            telas_do_app.forEach(function(iterador_interno2) {
                iterador_interno2.style.width = '150px'
                iterador_interno2.style.height = '15vh'
            })
            div_titulo_conta.style.display = 'none'
            div_titulo_grafico.style.display = 'none'
            div_titulo_saldo.style.display = 'none'
            div_titulo_transferencia.style.display = 'none'
            telas_expansionadas.style.gridTemplateRow = '1fr'
        }
    })

})

img_criar_conta.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

    tela_criar_conta.classList.toggle('on', expandir) 
    expandir = !expandir

    telas_do_app.forEach(function (iterador2){
        if ($(iterador2).hasClass("on")) {
            telas_do_app.forEach(function(iterador_interno2) {
                iterador_interno2.style.width = '150px'
                iterador_interno2.style.height = '15vh'
            })
            div_titulo_conta.style.display = 'none'
            div_titulo_grafico.style.display = 'none'
            div_titulo_saldo.style.display = 'none'
            div_titulo_transferencia.style.display = 'none'
            telas_expansionadas.style.gridTemplateRow = '1fr'
        }
    })


})

img_transferencia.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'

        }
    })

    tela_transferencias.classList.toggle('on', expandir) 
    expandir = !expandir

    telas_do_app.forEach(function (iterador2){
        if ($(iterador2).hasClass("on")) {
            telas_do_app.forEach(function(iterador_interno2) {
                iterador_interno2.style.width = '150px'
                iterador_interno2.style.height = '15vh'
            })
            div_titulo_conta.style.display = 'none'
            div_titulo_grafico.style.display = 'none'
            div_titulo_saldo.style.display = 'none'
            div_titulo_transferencia.style.display = 'none'
            telas_expansionadas.style.gridTemplateRow = '1fr'
        }
    })


})

fechar.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

})

fechar2.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

})

fechar3.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

})

fechar4.addEventListener('click', () => {

    telas_do_app.forEach( function (iterador){
        if ($(iterador).hasClass("on")) {
            iterador.classList.remove('on')
            telas_do_app.forEach(function(iterador_interno) {
                iterador_interno.style.width = '18vw'
                iterador_interno.style.height = '27vh'
            })
            div_titulo_conta.style.display = 'block'
            div_titulo_grafico.style.display = 'block'
            div_titulo_saldo.style.display = 'block'
            div_titulo_transferencia.style.display = 'block'
            telas_expansionadas.style.gridTemplateRow = '2fr 1fr'
        }
    })

})