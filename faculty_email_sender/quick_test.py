#!/usr/bin/env python3
"""
Quick test script to verify Gmail credentials and email sending
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Gmail credentials
GMAIL_ADDRESS = "csankalp21@gmail.com"
APP_PASSWORD = "uczn jbue yreg jtlk"  # Your app password

# Test recipient (use your own email for testing)
TEST_RECIPIENT = "reachsankalp21@gmail.com"

# CV path
CV_PATH = "/home/sankalp/Downloads/resume_sankalp (2).pdf"

def test_email_send():
    """Test sending a single email"""

    if not GMAIL_ADDRESS or not TEST_RECIPIENT:
        print("ERROR: Please fill in GMAIL_ADDRESS and TEST_RECIPIENT in the script!")
        return

    print("=" * 60)
    print("GMAIL EMAIL SENDER - QUICK TEST")
    print("=" * 60)
    print(f"\nFrom: {GMAIL_ADDRESS}")
    print(f"To: {TEST_RECIPIENT}")
    print(f"CV Attachment: {CV_PATH if CV_PATH else 'None'}")
    print()

    confirm = input("Send test email? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Test cancelled.")
        return

    # Create message
    msg = MIMEMultipart()
    msg['From'] = GMAIL_ADDRESS
    msg['To'] = TEST_RECIPIENT
    msg['Subject'] = "TEST - Interested in joining your research group"

    # Email body
    body = """Dear Dr. Test,

My Name is Sankalp, i completed my Master's degree in Physics From the Indian Institute of Technology(IIT) Palakkad,where i specialized in condensed matter physics and computational physics.I am writing to inquire about the possibility of joining your research group as a graduate/project student.



During my master's, I have worked on a project related to Majorana zero modes(MZMs), which involved exploring the emergent phenomena in topological quantum systems. The focus of the project was on understanding how non-abelian quasiparticles, such as MZMs arise in condensed matter systems and their potential applications in quantum computing. Specifically, I investigated the role of topological superconductors in hosting majorana modes and worked on models to predict their behaviour in 1D and 2D systems.This work gave me significant experience in numerical simulations, quantum mechanical modelling and a solid understanding of topological phases.



Given my background I am confident that I could be a valuable addition to your group and keen to contribute to ongoing and future projects in your lab.



I would be grateful if you could consider me for any open graduate student positions in your group. I have attached my CV. If there is any additional information you would need from me, please feel free to ask.

Thank you for your time and consideration.


Best Regards,

Sankalp"""

    msg.attach(MIMEText(body, 'plain'))

    # Attach CV if path provided
    if CV_PATH and os.path.exists(CV_PATH):
        with open(CV_PATH, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        filename = os.path.basename(CV_PATH)
        part.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(part)
        print(f"✓ CV attached: {filename}")
    elif CV_PATH:
        print(f"⚠ Warning: CV file not found at {CV_PATH}")
    else:
        print("⚠ No CV path provided - sending without attachment")

    print("\nSending email...")

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Remove spaces from app password
        clean_password = APP_PASSWORD.replace(" ", "")

        print(f"Logging in to Gmail as {GMAIL_ADDRESS}...")
        server.login(GMAIL_ADDRESS, clean_password)

        print("Sending message...")
        text = msg.as_string()
        server.sendmail(GMAIL_ADDRESS, TEST_RECIPIENT, text)
        server.quit()

        print("\n" + "=" * 60)
        print("✓ TEST EMAIL SENT SUCCESSFULLY!")
        print("=" * 60)
        print(f"\nCheck your inbox at {TEST_RECIPIENT}")
        print("\nIf you received the email successfully:")
        print("1. Verify the email format looks correct")
        print("2. Check if CV is attached (if you provided CV_PATH)")
        print("3. You're ready to use the main script!")

    except smtplib.SMTPAuthenticationError:
        print("\n" + "=" * 60)
        print("✗ AUTHENTICATION FAILED")
        print("=" * 60)
        print("\nPossible issues:")
        print("1. Make sure you're using an App Password, not your regular Gmail password")
        print("2. Verify the app password is correct: " + APP_PASSWORD)
        print("3. Check that 2-Step Verification is enabled on your Google account")
        print("4. Visit: https://myaccount.google.com/apppasswords")

    except Exception as e:
        print("\n" + "=" * 60)
        print("✗ ERROR SENDING EMAIL")
        print("=" * 60)
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    test_email_send()
