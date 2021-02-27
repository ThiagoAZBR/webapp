# FINANCR WEBAPP    

<br>
<br>

![Gif-da-home](https://github.com/helionroloff/webapp/blob/Thiago/financr/faleconosco/static/financr/img/imagens_readme/gif.gif)

#
<br>

<h4 align = 'center'>
ARTHUR SPILLERE CORDEIRO<br>
HÉLION ROLOFF<br>
LEONARDO DA SILVA KOSTETZER<br>
MARCUS MORESCO BOENO<br>
THIAGO AUGUSTO ZEFERINO
</h4>


<br>
<br>
<br>
<br>
<br>
<br>
<br>

<h3 margin-left= '2vw' align = 'center'>
    FINANCR
<h3>

<br>
<br>
<h4 align = 'right' text-align = 'justify'>
    Trabalho apresentado no  curso<br> de Python do programa Entra21
</h4>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<h4 align = 'center'>
Blumenau <br>
2020
</h4>

<br>

#

<br>

<h4 align = 'center'> 
INTRODUÇÃO
</h4>

<br>

<h4 align = 'justify'>

&emsp;&emsp;Será visto nesse trabalho conceitos e tecnologias referentes à programação web. Usamos para o back-end o framework Django do Python, junto com o banco de dados SQLite. Para o front-end foram usados HTML5, CSS, JavaScript, e uma das biliotecas do Google chamada Google chart tools.<br>
&emsp;&emsp;O trabalho foi costruído como um site de finanças pessoais, onde o foco foi resolver os problemas que faltam em muitos apps do mesmo ramo, como a falta de personalização e usabilidade.

</h4>

<br>
<br>

#

<h4 align = 'center'>
    COMO USAR?
</h4>

<br>

<h4 align = 'justify'>
&emsp;&emsp;1. Faça Um Git Clone do Projeto.<br><br><br>
&emsp;&emsp;2. Na pasta com o Git Clone crie uma venv:<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Windows - python -m venv yourvenv<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Linux/Mac - python3 -m venv yourvenv<br><br><br>
&emsp;&emsp;3. Ative a Venv:<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Windows: yourvenv\Scripts\activate<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Linux/Mac: source yourvenv/bin/activate<br><br><br>
&emsp;&emsp;4. Instale o Requirements.txt:<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- pip install -r requirements.txt <br><br><br>
&emsp;&emsp;5. Use o comando para rodar o Servidor Local:<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- python manage.py runserver<br><br><br>
&emsp;&emsp;EXTRA - Caso a ativação da venv não funcione, execute como administrador o powershell, e coloque o seguinte código e confirme com 'sim' se perguntar:<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine<br><br><br>
&emsp;&emsp;6. Onde estão nossos arquivos?<br><br>&emsp;&emsp;&emsp;- Arquivos Htmls principais estão na path 'webapp/financr/faleconosco/templates/templates';<br><br>
&emsp;&emsp;&emsp;- Arquivos CSS e JavaScript na path 'webapp/financr/faleconosco/static/financr';<br><br>
&emsp;&emsp;&emsp;- As Funções Python estão nos arquivos 'views.py' das Pastas faleconosco, contasbanco, transacao, users;<br><br>
&emsp;&emsp;&emsp;- A organização do banco de dados estão nos arquivos 'models.py' e 'forms.py' das mesmas pastas mencionadas anteriormente.
</h4>

#
<br>

<h4 align = 'center'>
CONTATO DOS DESENVOLVEDORES
</h4>


<br>
<br>

<table>
<thead>
<tr>
<th align="center"><a href="https://github.com/ArthurSpillere"><img src="https://avatars.githubusercontent.com/u/69689479?s=460&u=c4872eae980aca78b59bc716f19454d1a5358335&v=4" width="115" style="max-width:100%;"><br><sub>@arthurspillere</sub></a><br><a href = 'https://www.linkedin.com/in/arthur-spillere-cordeiro-796592148/'><sub>Linkedin</sub></a></th>
</tr>
</thead>
</table>


<table>
<thead>
<tr>
<th align="center"><a href="https://github.com/helionroloff"><img src="https://media-exp1.licdn.com/dms/image/C4D03AQEcfythRehlcw/profile-displayphoto-shrink_200_200/0/1604596056727?e=1619049600&v=beta&t=zqslUdVqUThrLnXpj5bM3NJRPNErNcH-lJgrFR9DA6A" width="115" style="max-width:100%;"><br><sub>@helionroloff</sub></a><br><a href = 'https://www.linkedin.com/in/helion-roloff-1222a91a4/'><sub>Linkedin</sub></a></th>
</tr>
</thead>
</table>


<table>
<thead>
<tr>
<th align="center"><a href="https://github.com/Leonardo612?tab=repositories"><img src="https://avatars.githubusercontent.com/u/69691083?s=460&v=4" width="115" style="max-width:100%;"><br><sub>@leonardokostetzer</sub></a><br><a href = 'https://www.linkedin.com/in/leonardo-kostetzer-1874621b8/'><sub>Linkedin</sub></a></th>
</tr>
</thead>
</table>


<table>
<thead>
<tr>
<th align="center"><a href="https://github.com/boenomarcus"><img src="https://avatars.githubusercontent.com/u/42239994?s=460&u=6f0c9f8f1b7992fa49cce6c4b96aabd5cbe27f67&v=4" width="115" style="max-width:100%;"><br><sub>@marcusboeno</sub><br></a><a href = 'https://www.linkedin.com/in/boenomarcus/'><sub>Linkedin</sub></a></th>
</tr>
</thead>
</table>


<table>
<thead>
<tr>
<th align="center"><a href="https://github.com/ThiagoAZBR"><img src="https://avatars.githubusercontent.com/u/60245661?s=460&u=77ca2f89bb47ae42b29c88b46a9b96e57f4d891e&v=4" width="115" style="max-width:100%;"><br><sub>@thiagoaz</sub><br></a><a href = 'https://www.linkedin.com/in/thiago-augusto-zeferino-b24b391b8/'><sub>Linkedin</sub></a></th>
</tr>
</thead>
</table>
