let check1 = document.querySelector('#check1')
let div_check1 = document.querySelector('.div_check1')

let check2 = document.querySelector('#check2')
let div_check2 = document.querySelector('.div_check2')

let check3 = document.querySelector('#check3')
let div_check3 = document.querySelector('.div_check3')

let div_pontual = document.querySelector('.div_tipo_pontual')
let div_tipo_fixa = document.querySelector('.div_tipo_fixa')
let div_tipo_parcelada = document.querySelector('.div_tipo_parcelada')

let resetar = document.querySelector('#resetar')


resetar.addEventListener('click', function() {

    div_check1.style.display = 'flex'
    div_check2.style.display = 'flex'
    div_check3.style.display = 'flex'

    div_pontual.style.display = 'none'
    div_tipo_fixa.style.display = 'none'
    div_tipo_parcelada.style.display = 'none'



})

check1.onchange = function () {

    if (check1.checked) {

        div_pontual.style.display = 'block'
        div_check2.style.display = 'none'
        div_check3.style.display = 'none'

    }

    else {

        div_pontual.style.display = 'none'
        div_check2.style.display = 'flex'
        div_check3.style.display = 'flex'

    }

}

check2.onchange = function () {

    if (check2.checked) {

        div_tipo_fixa.style.display = 'block'
        div_check1.style.display = 'none'
        div_check3.style.display = 'none'

    }

    else {

        div_tipo_fixa.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check3.style.display = 'flex'

    }

}

check3.onchange = function () {

    if (check3.checked) {

        div_tipo_parcelada.style.display = 'block'
        div_check1.style.display = 'none'
        div_check2.style.display = 'none'
        console.log('Check3 Aqui')

    }

    else {

        div_tipo_parcelada.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check2.style.display = 'flex'
        console.log('Check3 Falso Aqui')

    }

}