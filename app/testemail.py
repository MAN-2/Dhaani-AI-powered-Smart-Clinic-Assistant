import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Test body")
msg['Subject'] = "Test Subject"
msg['From'] = "your_email@gmail.com"
msg['To'] = "test_receiver@outlook.com"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password")
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
    print("✅ Test email sent")
except Exception as e:
    print("❌ Error:", e)
