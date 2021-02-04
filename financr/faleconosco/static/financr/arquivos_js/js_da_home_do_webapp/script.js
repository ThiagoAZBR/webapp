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

icone_usuario.addEventListener('click', () => {

    opcoes_icone_usuario.classList.toggle('on', mostrar)

    mostrar = !mostrar
    

})

tela_saldo.addEventListener('click', () => {

    for (var i = 0;; i++) {

        console.log(i)
        if (i >= maximo) break;

        divs_expansao[i].classList.remove('on')

    }

    tela_saldo.classList.toggle('on', expandir)

    expandir = !expandir


})

tela_graficos.addEventListener('click', () => {

    for (var i = 0;; i++) {

        console.log(i)
        if (i >= maximo) break;

        divs_expansao[i].classList.remove('on')

    }

    tela_graficos.classList.toggle('on', expandir)

    expandir = !expandir



})




let tela_total = document.querySelector('.telas_e_expansao')




let lista_on = []
let lista_off = []

tela_saldo.addEventListener('click', function() {

    divs_expansao.forEach(function (item) {

        if (item.className.indexOf('on') != -1) {

            lista_on.push(item)
            
        }

        else {

            lista_off.push(item)
            console.log('Entrou')

        }

        console.log(lista_off)
        console.log(lista_on)


    if (tela_saldo.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '200px'
            tela.style.height = '17vh'
            console.log('Lista off Aqui')

        })

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'


        })

    }



    lista_on.forEach(function (tela_on) {

        console.log('Lista on Aqui')

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
            console.log('Entrou')

        }

        console.log(lista_off)
        console.log(lista_on)


    if (tela_graficos.className.indexOf('on') != -1) {

        lista_off.forEach(function (tela) {

            tela.style.width = '200px'
            tela.style.height = '17vh'
            console.log('Lista off Aqui')

        })
        

    }

    else {

        lista_off.forEach(function (tela_off) {

            tela_off.style.width = '18vw'
            tela_off.style.height = '27vh'


        })

    }



    lista_on.forEach(function (tela_on) {

        console.log('Lista on Aqui')

    })

    })

})


revelar = true

let dados_usuario = document.querySelector('#dados')
let conf_usuario = document.querySelector('.conf_usuario')

dados_usuario.addEventListener('click', () => {

    conf_usuario.classList.toggle('on', revelar)

    revelar = !revelar

})