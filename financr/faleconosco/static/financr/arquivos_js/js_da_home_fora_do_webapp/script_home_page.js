// Arquivo Js para auxiliar com a transição de imagens

var imagem_porquinho = document.querySelectorAll('#img_porquinho')
var imagem_laptop_da_esquerda = document.querySelectorAll('#img_laptop')
var imagem_laptop_da_direita = document.querySelectorAll('#img_laptop_2')
var imagem_laptop_central = document.querySelectorAll('#img_laptop_3')

var txt_porquinho = document.querySelectorAll('#txt_porquinho')
var txt_logar = document.querySelectorAll('#txt_logar_porquinho')

var txt_esquerda = document.querySelectorAll('#txt_laptop_da_esquerda')
var txt_registrar = document.querySelectorAll('#txt_registrar_laptop_da_esquerda')

var txt_central = document.querySelectorAll('#txt_laptop_central')
var txt_sobre = document.querySelectorAll('#txt_sobre_laptop_central')

var txt_direita = document.querySelectorAll('#txt_laptop_da_direita')
var txt_contato = document.querySelectorAll('#txt_contato_laptop_da_direita')


let time = 5000,
    currentimageIndex = 0,
    currentTextIndex = 0,
    images = document.querySelectorAll('.bloco_1 img');
    texts = document.querySelectorAll('.bloco_1 h4');
    options = document.querySelectorAll('.bloco_1 h3');

    max = 4;

function nextimage() {

    images[currentimageIndex].classList.remove('selected');
    texts[currentTextIndex].classList.remove('txt_selected');
    options[currentTextIndex].classList.remove('option_selected');
    
    


    currentimageIndex++
    currentTextIndex++


    if (currentimageIndex >= max) 
        currentimageIndex = 0

    if (currentTextIndex >= max) 
        currentTextIndex = 0
        
    images[currentimageIndex].classList.add('selected')
    texts[currentTextIndex].classList.add('txt_selected')
    options[currentTextIndex].classList.add('option_selected')

}



function start() {

    setInterval(() => {
        console.log(currentimageIndex)
        //Troca de Imagem
        nextimage()
    }, time)

}

window.addEventListener('load', start)