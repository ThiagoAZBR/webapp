let show = true

const menuSection = document.querySelector('.menu-section')
const menuHamburguer = document.querySelector('.menu_hamburguer')

let cadastrar = document.querySelector('#txt_cadastre_se')
let fale_conosco = document.querySelector('#txt_fale_conosco')
let sobre = document.querySelector('#txt_sobre')
let logar = document.querySelector('#txt_login')

menuHamburguer.addEventListener('click', () => {
    
    document.body.style.overflow = show ? 'hidden' : 'initial'

    menuSection.classList.toggle('on', show)

    show = !show

})

sobre.addEventListener('click', function() {

    menuSection.classList.remove('on')
    show = !show
    document.body.style.overflow = 'initial'

})

cadastrar.addEventListener('click', function() {

    menuSection.classList.remove('on')
    show = !show
    document.body.style.overflow = 'initial'

})

fale_conosco.addEventListener('click', function() {

    menuSection.classList.remove('on')
    show = !show
    document.body.style.overflow = 'initial'

})

logar.addEventListener('click', function() {

    menuSection.classList.remove('on')
    show = !show
    document.body.style.overflow = 'initial'

})