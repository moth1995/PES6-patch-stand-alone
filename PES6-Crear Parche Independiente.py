pes6='PES6.exe'
pes6_settings='Settings.exe'
chunk_size = 4096
chunk_size2 = 4096
i = 0
while i != 22:
  valornuevo22 = input("Ingrese el nombre de su parche debe tener SI O SI 22 caracteres: ")
  if len(valornuevo22) == 22:
    break
  i = len(valornuevo22)

i = 0
while i != 4:
  valornuevo4 = input("Ingrese un nombre corto para su parche debe tener SI O SI 4 caracteres: ")
  if len(valornuevo4) == 4:
    break
  i = len(valornuevo4)
  
code =input("Ingrese el serial del juego SIN ESPACIOS (si no lo sabe presione enter y se generara uno automaticamente): ")
if len(code)==0:
    code="A6V9D5HXPT62H4PFWA45"
else:
     i = len(code)
     while i!=20:
         code = input("Ingrese el serial del juego SIN ESPACIOS: ")
         if len(code) == 20:
             break
         i = len(code)

#si no llega hasta aca es porque el usuario no ingreso un dato correcto por ende nunca sale del loop
#una vez mal ingresado el codigo tendra que ingresar un codigo por su cuenta

print("Su serial es: "+code)
 

 
#primero creamos un backup de los dos archivos

with open(pes6,'rb') as rf_exe:
    with open('PES6.bak','wb') as wf_exe:
        rf_exe_chunk = rf_exe.read(chunk_size)
        while len(rf_exe_chunk) >0:
            wf_exe.write(rf_exe_chunk)
            rf_exe_chunk = rf_exe.read(chunk_size)


with open(pes6_settings,'rb') as rf_settings:
      with open('settings.bak','wb') as wf_settings:
           rf_settings_chunk = rf_settings.read(chunk_size2)
           while len(rf_settings_chunk) >0:
              wf_settings.write(rf_settings_chunk)
              rf_settings_chunk = rf_settings.read(chunk_size2)

#abrimos el exe del pes6 en modo lectoescritura

wf_exe=open(pes6,'r+b')
wf_exe.seek(0x77E0A4,0)
wf_exe.write(valornuevo4.encode('utf8'))
wf_exe.seek(0x77DCD0,0)
wf_exe.write(valornuevo22.encode('utf8'))
wf_exe.close()

wf_settings=open(pes6_settings,'r+b')
wf_settings.seek(0x3987C,0)
wf_settings.write(valornuevo4.encode('utf8'))
wf_settings.seek(0x39894,0)
wf_settings.write(valornuevo22.encode('utf8'))
wf_settings.close()

#codigo a modo de ejemplo, de esta manera se lee una direccion de memoria

#rf_exe=open(pes6,'rb')
#rf_exe.seek(0x6CE4B8,0)
#cuando usamos la funcion .read() lo que va entre parentesis es la cantidad de caracteres que queremos agarrar, 
#puede ir en formato hexadecimal o decimal, yo prefiero usar hexadecimal
#print(rf_exe.read(0x16))
#rf_exe.close()


with open("Instalador ejecutar como Administrador.bat", "w+") as myfile:
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_e /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_p /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_s /T REG_DWORD /F /D \"1\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\KONAMIPES6\\"+ valornuevo4 + "\\1.0\" /F\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_e /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_p /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\" /V lang_s /T REG_DWORD /F /D \"1\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\\1.0\" /F\n")

with open("Desinstalador ejecutar como Administrador.bat", "w+") as myfile:
    myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES6\\"+ valornuevo4 + "\" /F\n")
    myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES6\\"+ valornuevo4 + "\"/F\n")

with open("serial.txt", "w+") as myfile:
    myfile.write(code)