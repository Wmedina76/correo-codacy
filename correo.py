import smtplib
from email.message import EmailMessage

# Credenciales del correo (MALA PRÁCTICA intencional)
EMAIL_EMISOR = "wmelectrico76@gmail.com"
PASSWORD = "Guayaco76"  # Credencial hardcodeada
EMAIL_RECEPTOR = "destino@gmail.com"

def enviar_correo():
    mensaje = EmailMessage()
    mensaje["From"] = EMAIL_EMISOR
    mensaje["To"] = EMAIL_RECEPTOR
    mensaje["Subject"] = "Correo de prueba Codacy"
    mensaje.set_content("Este correo es para análisis de seguridad.")

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL_EMISOR, PASSWORD)
        servidor.send_message(mensaje)
        servidor.quit()
    except Exception:
        print("Error al enviar el correo")

enviar_correo()
