# Keylogger-EmailAddress
 Keylogger feito em Python para mandar para o email configurado. <br>
<h1>Configurando servidor gmail</h1>
<p>Em nosso exemplo, veremos como enviar um email utilizando o serviço do gmail (pois ele é o mais utilizado no mundo). Porém, antes de iniciar o desenvolvimento do nosso projeto, precisamos criar um token para ser utilizado como password, caso você utilize o recurso de autenticação em duas etapas (recurso que só permite que seu usuário seja autenticado caso você o libere em seu smartphone) ou não quer que sua senha seja utilizada em aplicações não seguras.</p>

<h2>Criando token</h2>
<p>Para criar um token que será utilizado como senha em nossa aplicação, precisamos ir até o seguinte link:</p><br>
https://security.google.com/settings/security/apppasswords.<br><br>

<p>Na página, vamos selecionar a opção “Outro” para definir um nome para nosso projeto. Em seguida, determinamos o nome da aplicação e geramos o token:</p><br>
<img src="https://dkrn4sk0rn31v.cloudfront.net/2019/07/17105826/image-20190717104049935.png" alt="Imagem-1">

<h2>Criando script para envio de email<h1>
<p>Nosso script será bem simples. Basicamente, vamos informar o email e senha (conforme gerada no tópico anterior) da conta que será usada para enviar o email, o destinatário e o conteúdo do email. Sendo assim, o código será o seguinte:</p>

<code>server.login("seu_email@gmail.com", "senha_gerada_topico_anterior")</code><br>

<h3>Instalando bibliotecas</h3><br>
<p>Obs: se for linux use, pip3.</p><br>

* pynput
  ```sh
  pip install pynput
  ```
<br>

* smtplib
  ```sh
  pip install secure-smtplib
  ```