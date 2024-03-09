# Importing the SMTP library to handle sending emails
import smtplib

# Importing MIMEText for handling plain text in the email
from email.mime.multipart import MIMEMultipart

# Importing MIMEMultipart for creating a multipart message (subject, body, etc.)
from email.mime.text import MIMEText

# Email details
sender_email = "sender_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "App password from Google Account"
subject = "Subject you like"
body = "Hello, this is a test email sent using Python!"

# Setup the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
server.starttls()

# Log in to the email account
server.login(sender_email, password)
text = message.as_string()

# Send the email
server.sendmail(sender_email, receiver_email, text)
server.quit()

# Print a confirmation message
print("Email sent successfully!")