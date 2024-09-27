---

# Daily Email Report Automation Script

This Python script automates the process of sending daily email reports via Gmail's SMTP server. It generates a custom report and sends it to a specified recipient every day. The script uses Python's `smtplib` and `email` libraries to create the email and securely connect to Gmail's SMTP server.

## Features

- **Automated Email Reports:** Sends a daily email report with dynamic content based on the current date and time.
- **Customizable Content:** Easily modify the report content to include any data or information needed.
- **Secure SMTP Connection:** Utilizes TLS encryption for secure email delivery via Gmail.
- **Error Handling:** Provides error messages for SMTP connection or authentication issues.

## Prerequisites

- Python 3.x installed on your system
- A Gmail account
- If using Two-Factor Authentication (2FA), generate an **App Password** from your Google Account

## How It Works

1. **Configuration:**
   - The script is configured with your Gmail account's credentials (username and password or app password).
   - The recipient's email and the subject of the report can be modified.

2. **Report Generation:**
   - A simple function generates a daily report with the current date and time.
   - The report content can be customized according to your needs.

3. **Email Sending:**
   - The script establishes a secure connection to Gmail's SMTP server using TLS.
   - It logs in to your Gmail account and sends the report to the recipient.

4. **Error Handling:**
   - If any issues occur during login or sending the email (e.g., incorrect credentials or network issues), a detailed error message is printed.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/daily-email-report.git
   ```

2. Navigate to the project directory:

   ```bash
   cd daily_email_report
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open `email_report.py` and configure the following:

   - `EMAIL_USERNAME`: Your Gmail email address.
   - `EMAIL_PASSWORD`: Your Gmail password or app password (if using 2FA).
   - `EMAIL_TO`: The recipient's email address.
   - `EMAIL_SUBJECT`: Customize the subject line of the email.

5. Run the script:

   ```bash
   python daily_email_report.py
   ```

6. To schedule the email to send daily, you can use cron (Linux/macOS) or Task Scheduler (Windows).

## Example

```bash
python daily_email_report.py
```

Output:

```
Email sent successfully.
```

## Troubleshooting

- Ensure "Less Secure Apps" is enabled in your Gmail account if you're not using 2FA.
- If you're using 2FA, make sure to generate and use an App Password.
- Check the error messages for more information if the email fails to send.

---
