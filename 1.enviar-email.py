from email.message import EmailMessage
import ssl
import smtplib


# En la variable email_emisor se coloca el correo de la persona u organización quien entrega # y le dio permisos a python en su cuenta.


email_emisor = 'coloca_el_correo_quien_entrega'

# En la variable email_contrasena se debe colocar la contraseña de aplicación, la cual se #encuentra en la cuenta de Google. Y a la dirección: https://myaccount.google.com/#apppasswords 
#Y se crea una nueva aplicación para conectarla a Python.

email_contrasena = 'coloca_aquí_la_contraseña'

# En la variable email_receptor se coloca el correo de la persona u organización quien lo recibe.


email_receptor = 'coloca_el_correo_quien_recibe'

# A continuación se coloca el titulo y el cuerpo del correo electronico (Solo recibe texto)

asunto = 'Revisa el video en Youtube'
cuerpo = """
Se ha publicado un nuevo video en Youtube: https://www.youtube.com/watch?v=DDVpKvJXRz8&t=1s
"""

# Se crea un objeto el cual unira todos los componentes del correo electronico

em = EmailMessage()
em['From'] = email_emisor 
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

# Es este espacio se declaran el servidor y el puerto 465, como la tecnología de seguridad #ssl.


contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp: 
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
    
