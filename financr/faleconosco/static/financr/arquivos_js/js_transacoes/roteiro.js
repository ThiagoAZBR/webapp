mostrar = true
revelar = true

const opcoes_icone_usuario = document.querySelector('.opcoes_icone_usuario')
const icone_usuario = document.querySelector('#icone_usuario')

let dados_usuario = document.querySelector('#dados')
let conf_usuario = document.querySelector('.conf_usuario')

icone_usuario.addEventListener('click', () => {

    opcoes_icone_usuario.classList.toggle('on', mostrar)

    mostrar = !mostrar
    

})

dados_usuario.addEventListener('click', () => {

    conf_usuario.classList.toggle('on', revelar)

    revelar = !revelar

})