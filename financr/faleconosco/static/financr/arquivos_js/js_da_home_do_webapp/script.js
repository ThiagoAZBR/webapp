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
let max_telas_do_app = telas_do_app.length

let maximo = divs_expansao.length
let dados_usuario = document.querySelector('#dados')
let conf_usuario = document.querySelector('.conf_usuario')

// Imagens Abaixo
let img_saldo = document.querySelector('#img_saldo')
let img_grafico = document.querySelector('#img_grafico')
let img_criar_conta = document.querySelector('#img_criar_conta')
let img_transferencia = document.querySelector('#img_transferencia')

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
        }
    })

})