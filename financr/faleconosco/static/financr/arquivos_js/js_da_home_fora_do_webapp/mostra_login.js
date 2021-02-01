let btn = document.getElementById('txt_login');
let fundo = document.querySelector('.barra_topo');
let imagens = document.querySelector('.bloco_1');
let tela_de_login = document.querySelector('.tela_de_login_invisivel');
let xiz = document.querySelector('#x_fechar')
let sobre_1 = document.querySelector('#sobre_o_app')
let sobre_2 = document.querySelector('.funcionalidades2')
let cadastro = document.querySelector('.cadastro')
let contato = document.querySelector('#fale_conosco')

// Aqui Vai Ser onde Vai Clicar Em 'Login' e Vai Aparecer a tela de login na tela
btn.addEventListener('click', function() {
    
  if(tela_de_login.style.display === 'block') {
      tela_de_login.style.display = 'none';
      fundo.style.opacity = '1'
      imagens.style.opacity = '1'
      sobre_1.style.opacity = '1'
      sobre_2.style.opacity = '1'
      cadastro.style.opacity = '1'
      contato.style.opacity = '1'
      document.body.style.overflow = 'initial'

  } else {
      tela_de_login.style.display = 'block';
      fundo.style.opacity = '0.1';
      imagens.style.opacity = '0.1';
      sobre_1.style.opacity = '0.1'
      sobre_2.style.opacity = '0.1'
      cadastro.style.opacity = '0.1'
      contato.style.opacity = '0.1'
      document.body.style.overflow = 'hidden'

      fundo.style.transition = 'opacity 500ms' ;
      imagens.style.transition = 'opacity 300ms' ;
      sobre_1.style.transition = 'opacity 300ms' ;
      sobre_2.style.transition = 'opacity 300ms' ;
      cadastro.style.transition = 'opacity 300ms' ;
      contato.style.transition = 'opacity 300ms' ;
  }

});

// Aqui onde clica no x para poder fechar a aba de login
xiz.addEventListener('click', function() {
    
  if(tela_de_login.style.display === 'block') {
      tela_de_login.style.display = 'none';
      fundo.style.opacity = '1';
      imagens.style.opacity = '1';
      sobre_1.style.opacity = '1'
      sobre_2.style.opacity = '1'
      cadastro.style.opacity = '1'
      contato.style.opacity = '1'
      document.body.style.overflow = 'initial'

  } else {
      tela_de_login.style.display = 'block';
      fundo.style.opacity = '0.1';
      imagens.style.opacity = '0.1';
      sobre_1.style.opacity = '0.1'
      sobre_2.style.opacity = '0.1'
      cadastro.style.opacity = '0.1'
      contato.style.opacity = '0.1'
      document.body.style.overflow = 'hidden'

      fundo.style.transition = 'opacity 500ms' ;
      imagens.style.transition = 'opacity 300ms' ;
      sobre_1.style.transition = 'opacity 300ms' ;
      sobre_2.style.transition = 'opacity 300ms' ;
      cadastro.style.transition = 'opacity 300ms' ;
      contato.style.transition = 'opacity 300ms' ;
  }

});

