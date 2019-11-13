import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Test Email From Cody"
Name = "Landen"
Month = "November"
body = """\
<html>
  <body>
    <p style='font-family:"Comic Sans MS", cursive, sans-serif; font-size: 16px;'>Hi """ + Name + """,<br><br> I have attached the invoice for mowing in the month of """ + Month + """. Please let me know if you have any questions or need anything else done. Thank you so much and I hope you have a good rest of your week.
  <br><br>Landon Wiswall<br>
  Well-Groomed Lawn Care, LLC<br>
    </p>
  </body>
</html>
"""
sender_email = "testEmailWellGroomed@gmail.com"
receiver_email = "cj.polton@gmail.com" 
password = "Groomed1!"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "html"))

filename = "Invoices/test-output.docx"  # In same directory as script
logo = "Images/logo.png"

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    "attachment; filename={}".format(filename),
)

# Add attachment to message and convert message to string


with open(logo, "rb") as attachment:
  # Add file as application/octet-stream
  # Email client can usually download this automatically as attachment
  part2 = MIMEBase("application", "octet-stream")
  part2.set_payload(attachment.read())

encoders.encode_base64(part2)

part2.add_header('Content-Disposition', "attachment; filename={}".format(logo),)
part2.add_header('X-Attachment-Id', '0')
part2.add_header('Content-ID', '<0>')

message.attach(part2)
message.attach(part)

text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, text)
server.quit()