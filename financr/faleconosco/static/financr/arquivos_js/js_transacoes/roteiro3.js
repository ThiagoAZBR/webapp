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

let oitenta_e_sete = 87
let select = document.querySelector('#id_categoria_transacao').value = oitenta_e_sete

let tipo_transacao = document.querySelector('#id_tipo_transacao')



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
        tipo_transacao.value = '1'

    }

    else {

        div_forms.style.display = 'none'
        div_check2.style.display = 'flex'
        div_check3.style.display = 'flex'
        tipo_transacao.value = '0'

    }

}

check2.onchange = function () {

    if (check2.checked) {

        div_forms.style.display = 'block'
        div_check1.style.display = 'none'
        div_check3.style.display = 'none'
        regularide.style.display = 'block'
        parcelas.style.display = 'none'
        tipo_transacao.value = '2'
        


    }

    else {

        div_forms.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check3.style.display = 'flex'
        tipo_transacao.value = '0'

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
        tipo_transacao.value = '3'

    }

    else {

        div_forms.style.display = 'none'
        div_check1.style.display = 'flex'
        div_check2.style.display = 'flex'
        tipo_transacao.value = '0'
        console.log('Check3 Falso Aqui')

    }

}