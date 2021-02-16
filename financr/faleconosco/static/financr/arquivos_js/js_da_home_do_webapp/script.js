mostrar = true

expandir = true

const opcoes_icone_usuario = document.querySelector('.opcoes_icone_usuario')
const icone_usuario = document.querySelector('#icone_usuario')

let tela_saldo = document.querySelector('.tela_saldo')
let tela_graficos = document.querySelector('.tela_graficos')
let tela_criar_conta = document.querySelector('.tela_criar')
let tela_transferencias = document.querySelector('.tela_transferencias')

let divs_expansao = document.querySelectorAll('.telas_e_expansao div')
let maximo = divs_expansao.length
let dados_usuario = document.querySelector('#dados')
let conf_usuario = document.querySelector('.conf_usuario')

// Imagens Abaixo
let img_saldo = document.querySelector('#img_saldo')
let img_grafico = document.querySelector('#img_grafico')
let img_criar_conta = document.querySelector('#img_criar_conta')
let img_transferencia = document.querySelector('#img_transferencia')


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




img_saldo.addEventListener('click', () => {

    for (var i = 0;; i++) {

        if (i >= maximo) break;

        divs_expansao[i].classList.remove('on')

    }

    tela_saldo.classList.toggle('on', expandir)

    expandir = !expandir


})

img_grafico.addEventListener('click', () => {

    for (var i = 0;; i++) {

        if (i >= maximo) break;

        if ($(".tela_graficos").hasClass("on")) {


        }
            divs_expansao[i].classList.remove('on')

    }

    tela_graficos.classList.toggle('on', expandir)

    expandir = !expandir



})

img_criar_conta.addEventListener('click', () => {

    for (var i = 0;; i++) {

        if (i >= maximo) break;

        divs_expansao[i].classList.remove('on')

    }

    tela_criar_conta.classList.toggle('on', expandir)

    expandir = !expandir



})

img_transferencia.addEventListener('click', () => {

    for (var i = 0;; i++) {

        if (i >= maximo) break;

        divs_expansao[i].classList.remove('on')

    }

    tela_transferencias.classList.toggle('on', expandir)

    expandir = !expandir


})






let tela_total = document.querySelector('.telas_e_expansao')




let lista_on = []
let lista_off = []

//  Controlar o tamanho das outras telas ao clicar e expandir

tela_saldo.addEventListener('click', function() {

    divs_expansao.forEach(function (item) {

        if (item.className.indexOf('on') != -1) {

            lista_on.push(item)
            
        }

        else {

            lista_off.push(item)

        }



    if (tela_saldo.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '170px'
            tela.style.height = '15vh'

        })

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'

            for (var i = 0;; i++) {

                if (i >= maximo) break;
        
                divs_expansao[i].classList.remove('on')
        
            }


        })

    }



    lista_on.forEach(function (tela_on) {


    })

    })

})

//                                                         ----     G R Á F I C O S   -----


tela_graficos.addEventListener('click', function() {

    divs_expansao.forEach(function (item) {

        if (item.className.indexOf('on') != -1) {

            lista_on.push(item)
            
        }

        else {

            lista_off.push(item)

        }



    if (tela_graficos.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '170px'
            tela.style.height = '15vh'

        })
        

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'

            for (var i = 0;; i++) {

                if (i >= maximo) break;
        
                divs_expansao[i].classList.remove('on')
        
            }

        })

    }



    lista_on.forEach(function (tela_on) {


    })

    })

})




//                                                         ----     C R I A R  C O N T A   -----



tela_criar_conta.addEventListener('click', function() {

    divs_expansao.forEach(function (item) {

        if (item.className.indexOf('on') != -1) {

            lista_on.push(item)
            
        }

        else {

            lista_off.push(item)

        }



    if (tela_criar_conta.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '170px'
            tela.style.height = '15vh'

        })
        

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'

            for (var i = 0;; i++) {

                if (i >= maximo) break;
        
                divs_expansao[i].classList.remove('on')
        
            }


        })

    }



    lista_on.forEach(function (tela_on) {


    })

    })

})



//                                                         ----     T R A N S F E R E N C I A S   -----



tela_transferencias.addEventListener('click', function() {

    divs_expansao.forEach(function (item) {

        if (item.className.indexOf('on') != -1) {

            lista_on.push(item)
            
        }

        else {

            lista_off.push(item)

        }



    if (tela_transferencias.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '170px'
            tela.style.height = '15vh'

        })
        

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'

            for (var i = 0;; i++) {

                if (i >= maximo) break;
        
                divs_expansao[i].classList.remove('on')
        
            }


        })

    }



    lista_on.forEach(function (tela_on) {


    })

    })

})