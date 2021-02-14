let check1 = document.querySelector('#check1')
let div_check1 = document.querySelector('.div_check1')
// Apenas Observação irá aparecer
let observaca = document.querySelector('.div_observacao')

let check2 = document.querySelector('#check2')
let div_check2 = document.querySelector('.div_check2')
// Observação e Regularidade Irão Aparecer
let regularide = document.querySelector('.div_regularidade')

let check3 = document.querySelector('#check3')
let div_check3 = document.querySelector('.div_check3')
// Observação, Regularidade e Parcelas irão Aparecer
let parcelas = document.querySelector('.div_numero_de_parcelas')

let div_forms = document.querySelector('.div_tipo_parcelada')

let resetar = document.querySelector('#resetar')

resetar.addEventListener('click', function() {

    div_check1.style.display = 'flex'
    div_check2.style.display = 'flex'
    div_check3.style.display = 'flex'

    div_forms.style.display = 'none'



})

check1.onchange = function () {

    if (check1.checked) {

        div_forms.style.display = 'block'
        div_check2.style.display = 'none'
        div_check3.style.display = 'none'
        regularide.style.display = 'none'
        parcelas.style.display = 'none'

    }

    else {

        div_forms.style.display = 'none'
        div_check2.style.display = 'flex'
        div_check3.style.display = 'flex'

    }

}

check2.onchange = function () {

    if (check2.checked) {

        div_forms.style.display = 'block'
        div_check1.style.display = 'none'
        div_check3.style.display = 'none'
        regularide.style.display = 'block'
        parcelas.style.display = 'none'

    }

    else {

        div_forms.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check3.style.display = 'flex'

    }

}

check3.onchange = function () {

    if (check3.checked) {

        div_forms.style.display = 'block'
        div_check1.style.display = 'none'
        div_check2.style.display = 'none'
        regularide.style.display = 'block'
        parcelas.style.display = 'block'
        console.log('Check3 Aqui')

    }

    else {

        div_forms.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check2.style.display = 'flex'
        console.log('Check3 Falso Aqui')

    }

}