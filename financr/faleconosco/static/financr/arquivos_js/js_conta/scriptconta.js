let txt_fechar = document.querySelector('#txt_fechar')
let div_erros = document.querySelector('.div_formatacao_erros')


txt_fechar.addEventListener('click', () => {

    div_erros.style.display = 'none'

})

window.onload = function(){
    div_erros.style.display = 'flex'
}