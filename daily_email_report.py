import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465  # Try port 465 if 587 does not work
EMAIL_USERNAME = '#Add your username'
EMAIL_PASSWORD = os.getenv('#Add your Password')  # Use environment variable for password
EMAIL_FROM = '#Add your mail'
EMAIL_TO = '#Add receipient mail'
EMAIL_SUBJECT = 'Daily Report'

# Generate the report
def generate_report():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = f"Daily Report for {current_time}\n\n"
    report_content += "This is your daily report content. Modify this as needed."
    return report_content

# Send the email
def send_email(report_content):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = EMAIL_SUBJECT
    msg.attach(MIMEText(report_content, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)  # Enable debug output if needed
        server.starttls()  # Secure the connection
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except smtplib.SMTPConnectError as e:
        print(f"SMTP Connection Error: {e}")
    except Exception as e:
        print(f"Failed to send email: {type(e).__name__}, {str(e)}")

# Main function
if __name__ == "__main__":
    report_content = generate_report()
    send_email(report_content)
