# PES6-patch-stand-alone
 Help you to create easily an standalone patch for PES6

<h1><b>Intro</b></h1>
 
Este programa hace las siguientes cosas

<ul>
 <li>Modifica valores en el PES6.exe y el archivo settings.exe para que estos funcionen de manera independiente al juego original</li>
 <li>Crea backup de los dos archivos antes mencionados haciendo una copia de los mismos con la extension .bak</li>
 <li>Crea archivo .reg para instalacion y otro para desinstalacion del mismo juego</li>
 <li>Crea archivo serial.txt que contiene el serial que usted ingreso o uno generado por el programa</li>
</ul>  

<h1><b>Descargas</b></h1>
  
<a href="https://github.com/moth1995/PES6-patch-stand-alone/releases/latest">Ultima version</a>

<h1><b>¿Como puedo confiar en este archivo?</b></h1>

Pueden leer el codigo en este repositorio :)

<h1><b>No te creo soy muy paranoico ¿Como lo compilo por cuenta para estar tranquilo?</b></h1>

Simple: 
<ul>
  <li> Instalan <a href="https://www.python.org/downloads/">Python 3.0</a> </li>
  <li> Corren el comando pip3 install pyinstaller</li>
  <li> Dentro de la carpeta donde tienen su archivo .py ejecutan pyinstaller --onefile "nombre del archivo.py"</li>
</ul>
