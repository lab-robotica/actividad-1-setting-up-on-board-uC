# Actividad-1-setting-up-on-board-uC

## Requerimientos
- Monitor
- Teclado
- Mouse (opcional)
- Cable micro hdmi
- Router 
- Raspberry Pi
- Foco led 
- Protoboard

## Procedimiento:

- Conectar y Encender la Raspberry Pi
- Conectar un monitor con un cable microHDMI
- Conectar un teclado 
- Conectar un mouse (opcional)
- Acceder a la cuenta 
- Verificar que esté conectado a internet, si no conectarla
- Abrir la terminal 
- Escribir “ifconfig”
- Aparecerá la IP de la Raspberry Pi
- Cambiar la IP dinámica a una IP estática para usar esa siempre que se quiera acceder a la Rpi
- En la computadora personal entrar a la Terminal
- Asegurarse de que este la computadora conectada a la misma red que la Rpi
- Ingresar el siguiente comando en la terminal “ssh user@192.168.1.4(ip)”
- Ingresar contraseña de usuario
- Correr programa de `python3 ./hello-world/hello.py`
- Correr programa de `python3 ./led-display/main.py`
