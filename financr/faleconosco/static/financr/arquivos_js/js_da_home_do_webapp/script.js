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
let fechar_config = document.querySelector('#fechar_config')



// Transformar de None para Block, ou Block para None


icone_usuario.addEventListener('click', () => {

    opcoes_icone_usuario.classList.toggle('on', mostrar)
    
    if (conf_usuario.className.indexOf('on') != -1) {

        conf_usuario.classList.remove('on')

    }

    mostrar = !mostrar
    

})

fechar_config.addEventListener('click', () => {

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

if (innerWidth > 430) {

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

}

if (innerWidth <= 430) {

    img_saldo.addEventListener('click', () => {
    
        tela_saldo.classList.toggle('on', expandir)
        expandir = !expandir
    
        tela_criar_conta.style.display = 'none'
        tela_graficos.style.display = 'none'
        tela_transferencias.style.display = 'none'

        tela_saldo.style.display = 'block'
        telas_expansionadas.style.gridTemplateRows = '1fr'
        telas_expansionadas.style.gridTemplateColumns = '1fr'

    })

    fechar.addEventListener('click', () => {

        telas_do_app.forEach( function (iterador){
            if ($(iterador).hasClass("on")) {
                iterador.classList.remove('on')
                telas_do_app.forEach(function(iterador_interno) {
                    tela_criar_conta.style.width = '18vw'
                    tela_criar_conta.style.height = '27vh'
                    tela_criar_conta.style.display = 'block'

                    tela_graficos.style.width = '18vw'
                    tela_graficos.style.height = '27vh'
                    tela_graficos.style.display = 'block'

                    tela_transferencias.style.width = '18vw'
                    tela_transferencias.style.height = '27vh'
                    tela_transferencias.style.display = 'block'
                })
            }
            telas_expansionadas.style.gridTemplateRows = '1fr 1fr'
            telas_expansionadas.style.gridTemplateColumns = '1fr 1fr'
            telas_expansionadas.style.marginTop = '3vh'
            img_saldo.style.marginTop = '1vh'
        })
    
    })

    img_grafico.addEventListener('click', () => {
    
        tela_graficos.classList.toggle('on', expandir)
        expandir = !expandir
    
        tela_saldo.style.display = 'none'
        tela_criar_conta.style.display = 'none'
        tela_transferencias.style.display = 'none'

        tela_graficos.style.display = 'block'
        telas_expansionadas.style.gridTemplateRows = '1fr'
        telas_expansionadas.style.gridTemplateColumns = '1fr'
        tela_graficos.style.gridColumn = '1'
        tela_graficos.style.gridRow = '1'

    })

    fechar2.addEventListener('click', () => {

        telas_do_app.forEach( function (iterador){
            if ($(iterador).hasClass("on")) {
                iterador.classList.remove('on')
                telas_do_app.forEach(function(iterador_interno) {
                    tela_saldo.style.width = '18vw'
                    tela_saldo.style.height = '27vh'
                    tela_saldo.style.display = 'block'

                    tela_criar_conta.style.width = '18vw'
                    tela_criar_conta.style.height = '27vh'
                    tela_criar_conta.style.display = 'block'

                    tela_transferencias.style.width = '18vw'
                    tela_transferencias.style.height = '27vh'
                    tela_transferencias.style.display = 'block'
                })
            }
            telas_expansionadas.style.gridTemplateRows = '1fr 1fr'
            telas_expansionadas.style.gridTemplateColumns = '1fr 1fr'
            telas_expansionadas.style.marginTop = '3vh'
            tela_graficos.style.gridColumn = '1'
            tela_graficos.style.gridRow = '2'

        })
    
    })



    img_criar_conta.addEventListener('click', () => {
    
        tela_criar_conta.classList.toggle('on', expandir)
        expandir = !expandir
    
        tela_saldo.style.display = 'none'
        tela_graficos.style.display = 'none'
        tela_transferencias.style.display = 'none'

        tela_criar_conta.style.display = 'block'
        telas_expansionadas.style.gridTemplateRows = '1fr'
        telas_expansionadas.style.gridTemplateColumns = '1fr'
        tela_criar_conta.style.gridColumn = '1'

    })
    
    fechar3.addEventListener('click', () => {

        telas_do_app.forEach( function (iterador){
            if ($(iterador).hasClass("on")) {
                iterador.classList.remove('on')
                telas_do_app.forEach(function(iterador_interno) {
                    tela_saldo.style.width = '18vw'
                    tela_saldo.style.height = '27vh'
                    tela_saldo.style.display = 'block'

                    tela_graficos.style.width = '18vw'
                    tela_graficos.style.height = '27vh'
                    tela_graficos.style.display = 'block'

                    tela_transferencias.style.width = '18vw'
                    tela_transferencias.style.height = '27vh'
                    tela_transferencias.style.display = 'block'
                })
            }
            telas_expansionadas.style.gridTemplateRows = '1fr 1fr'
            telas_expansionadas.style.gridTemplateColumns = '1fr 1fr'
            telas_expansionadas.style.marginTop = '3vh'
            tela_criar_conta.style.gridColumn = '2'
        })
    
    })

    img_transferencia.addEventListener('click', () => {
    
        tela_transferencias.classList.toggle('on', expandir)
        expandir = !expandir
    
        tela_saldo.style.display = 'none'
        tela_graficos.style.display = 'none'
        tela_criar_conta.style.display = 'none'

        tela_transferencias.style.display = 'block'
        telas_expansionadas.style.gridTemplateRows = '1fr'
        telas_expansionadas.style.gridTemplateColumns = '1fr'
        tela_transferencias.style.gridColumn = '1'
        tela_transferencias.style.gridRow = '1'

    })

        
    fechar4.addEventListener('click', () => {

        telas_do_app.forEach( function (iterador){
            if ($(iterador).hasClass("on")) {
                iterador.classList.remove('on')
                telas_do_app.forEach(function(iterador_interno) {
                    tela_saldo.style.width = '18vw'
                    tela_saldo.style.height = '27vh'
                    tela_saldo.style.display = 'block'

                    tela_graficos.style.width = '18vw'
                    tela_graficos.style.height = '27vh'
                    tela_graficos.style.display = 'block'

                    tela_criar_conta.style.width = '18vw'
                    tela_criar_conta.style.height = '27vh'
                    tela_criar_conta.style.display = 'block'
                })
            }
            telas_expansionadas.style.gridTemplateRows = '1fr 1fr'
            telas_expansionadas.style.gridTemplateColumns = '1fr 1fr'
            telas_expansionadas.style.marginTop = '3vh'
            tela_transferencias.style.gridColumn = '2'
            tela_transferencias.style.gridRow = '2'
        })
    
    })

}