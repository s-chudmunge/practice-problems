#!/usr/bin/env python3
"""
Script to send personalized emails to faculty members via Gmail
Author: Generated for Sankalp's PhD applications
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import json
import getpass
from datetime import datetime

# File to store faculty data
FACULTY_FILE = "faculty_emails.json"
TEST_FILE = "test_emails.json"
SENT_LOG_FILE = "emails_sent_log.json"

# Gmail credentials (hardcoded)
GMAIL_ADDRESS = "csankalp21@gmail.com"
APP_PASSWORD = "uczn jbue yreg jtlk"

# Email template
EMAIL_SUBJECT = "Interested in joining your research group"

def load_faculty_data(file_path):
    """Load faculty data from JSON file"""
    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} not found!")
        return []

    with open(file_path, 'r') as f:
        return json.load(f)

def save_faculty_data(faculty_list):
    """Save faculty data to JSON file"""
    with open(FACULTY_FILE, 'w') as f:
        json.dump(faculty_list, f, indent=2)
    print(f"Faculty data saved to {FACULTY_FILE}")

def create_email_body(prof_last_name):
    """Create email body with professor's last name"""
    return f"""Dear Dr. {prof_last_name},

My Name is Sankalp, i completed my Master's degree in Physics From the Indian Institute of Technology(IIT) Palakkad,where i specialized in condensed matter physics and computational physics.I am writing to inquire about the possibility of joining your research group as a graduate/project student.

During my master's, I have worked on a project related to Majorana zero modes(MZMs), which involved exploring the emergent phenomena in topological quantum systems. The focus of the project was on understanding how non-abelian quasiparticles, such as MZMs arise in condensed matter systems and their potential applications in quantum computing. Specifically, I investigated the role of topological superconductors in hosting majorana modes and worked on models to predict their behaviour in 1D and 2D systems.This work gave me significant experience in numerical simulations, quantum mechanical modelling and a solid understanding of topological phases.

Given my background I am confident that I could be a valuable addition to your group and keen to contribute to ongoing and future projects in your lab.

I would be grateful if you could consider me for any open graduate student positions in your group. I have attached my CV. If there is any additional information you would need from me, please feel free to ask.

Thank you for your time and consideration.

Best Regards,

Sankalp"""

def display_faculty_list(faculty_list):
    """Display all faculty with their information"""
    print("\n" + "=" * 80)
    print("FACULTY LIST")
    print("=" * 80)

    if not faculty_list:
        print("No faculty in the list.")
        return

    for idx, prof in enumerate(faculty_list, 1):
        email_status = prof['email'] if prof['email'] else "[NO EMAIL]"
        print(f"{idx:2d}. Dr. {prof['name']:20s} | {prof['university']:15s} | {email_status}")

    print("=" * 80)

def add_faculty(faculty_list):
    """Add a new faculty member"""
    print("\n--- Add New Faculty ---")
    name = input("Professor's last name: ").strip()
    email = input("Email address: ").strip()
    university = input("University (short name): ").strip()

    new_faculty = {
        "name": name,
        "email": email,
        "university": university
    }

    faculty_list.append(new_faculty)
    print(f"✓ Dr. {name} added successfully!")
    return faculty_list

def edit_faculty(faculty_list):
    """Edit an existing faculty member"""
    display_faculty_list(faculty_list)

    try:
        idx = int(input("\nEnter number of faculty to edit (0 to cancel): "))
        if idx == 0:
            return faculty_list

        if 1 <= idx <= len(faculty_list):
            prof = faculty_list[idx - 1]
            print(f"\nEditing Dr. {prof['name']}")
            print(f"Current email: {prof['email']}")
            print(f"Current university: {prof['university']}")
            print()

            name = input(f"New last name (Enter to keep '{prof['name']}'): ").strip()
            email = input(f"New email (Enter to keep '{prof['email']}'): ").strip()
            university = input(f"New university (Enter to keep '{prof['university']}'): ").strip()

            if name:
                prof['name'] = name
            if email:
                prof['email'] = email
            if university:
                prof['university'] = university

            print("✓ Faculty updated successfully!")
        else:
            print("Invalid number!")

    except ValueError:
        print("Invalid input!")

    return faculty_list

def delete_faculty(faculty_list):
    """Delete a faculty member"""
    display_faculty_list(faculty_list)

    try:
        idx = int(input("\nEnter number of faculty to delete (0 to cancel): "))
        if idx == 0:
            return faculty_list

        if 1 <= idx <= len(faculty_list):
            prof = faculty_list[idx - 1]
            confirm = input(f"Delete Dr. {prof['name']}? (yes/no): ").strip().lower()
            if confirm == 'yes':
                faculty_list.pop(idx - 1)
                print(f"✓ Dr. {prof['name']} deleted successfully!")
        else:
            print("Invalid number!")

    except ValueError:
        print("Invalid input!")

    return faculty_list

def send_email(sender_email, sender_password, recipient_email, prof_name, cv_path):
    """Send email to a single professor"""

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = EMAIL_SUBJECT

    # Add body
    body = create_email_body(prof_name)
    msg.attach(MIMEText(body, 'plain'))

    # Attach CV
    if os.path.exists(cv_path):
        with open(cv_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        filename = os.path.basename(cv_path)
        part.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(part)
    else:
        print(f"WARNING: CV file not found at {cv_path}")
        return False

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Remove any spaces from password
        clean_password = sender_password.replace(" ", "")
        server.login(sender_email, clean_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"✓ Email sent successfully to Dr. {prof_name} ({recipient_email})")
        return True
    except Exception as e:
        print(f"✗ Failed to send email to Dr. {prof_name}: {str(e)}")
        return False

def load_sent_log():
    """Load the log of sent emails"""
    if os.path.exists(SENT_LOG_FILE):
        with open(SENT_LOG_FILE, 'r') as f:
            return json.load(f)
    return []

def save_sent_log(log_entries):
    """Save the log of sent emails"""
    with open(SENT_LOG_FILE, 'w') as f:
        json.dump(log_entries, f, indent=2)

def send_emails_batch(faculty_list, data_file, start_idx, end_idx):
    """Send emails to faculty in batch mode without individual confirmation"""
    print("\n" + "=" * 80)
    print("BATCH SEND EMAILS")
    print("=" * 80)

    # Get CV path
    default_cv = "/home/sankalp/Downloads/resume_sankalp (2).pdf"
    cv_input = input(f"\nEnter CV path (Enter for default: {default_cv}): ").strip()
    cv_path = cv_input if cv_input else default_cv

    if not os.path.exists(cv_path):
        print(f"\nERROR: CV file not found at {cv_path}")
        return

    # Filter faculty with valid emails
    valid_faculty = [f for f in faculty_list if f['email'] and '@' in f['email']]

    if not valid_faculty:
        print("ERROR: No valid email addresses found!")
        return

    # Validate range
    if start_idx < 1 or start_idx > len(valid_faculty):
        print(f"ERROR: Start index {start_idx} is out of range (1-{len(valid_faculty)})")
        return
    if end_idx < start_idx or end_idx > len(valid_faculty):
        print(f"ERROR: End index {end_idx} is invalid (must be between {start_idx} and {len(valid_faculty)})")
        return

    # Load sent log
    sent_log = load_sent_log()
    sent_emails = {entry['email'] for entry in sent_log if entry.get('status') == 'success'}

    # Show what will be sent
    print(f"\nTotal professors in database: {len(valid_faculty)}")
    print(f"Batch range: #{start_idx} to #{end_idx} ({end_idx - start_idx + 1} emails)")
    print(f"Using CV: {cv_path}")
    print(f"Using Gmail: {GMAIL_ADDRESS}")

    # Show sample of professors that will receive emails
    print("\n" + "=" * 80)
    print(f"PROFESSORS TO EMAIL (showing first 10 and last 5 of selected range)")
    print("=" * 80)

    batch_faculty = valid_faculty[start_idx - 1:end_idx]
    display_limit = min(10, len(batch_faculty))
    for i in range(display_limit):
        prof = batch_faculty[i]
        actual_num = start_idx + i
        status = "[ALREADY SENT]" if prof['email'] in sent_emails else ""
        print(f"{actual_num:3d}. Dr. {prof['name']:25s} | {prof['university']:20s} {status}")

    if len(batch_faculty) > 15:
        print(f"\n     ... {len(batch_faculty) - 15} professors in the middle ...")

    if len(batch_faculty) > 10:
        print()
        for i in range(max(10, len(batch_faculty) - 5), len(batch_faculty)):
            prof = batch_faculty[i]
            actual_num = start_idx + i
            status = "[ALREADY SENT]" if prof['email'] in sent_emails else ""
            print(f"{actual_num:3d}. Dr. {prof['name']:25s} | {prof['university']:20s} {status}")

    print("=" * 80)

    # Final confirmation
    confirm = input(f"\nProceed to send {len(batch_faculty)} emails in batch mode? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Batch send cancelled.")
        return

    print("\n" + "=" * 80)
    print("SENDING EMAILS IN BATCH MODE...")
    print("=" * 80)

    success_count = 0
    fail_count = 0
    already_sent_count = 0

    # Send emails in batch
    for idx in range(start_idx - 1, end_idx):
        prof = valid_faculty[idx]

        # Skip if already sent
        if prof['email'] in sent_emails:
            print(f"[{idx + 1}/{end_idx}] ⊘ Skipping Dr. {prof['name']} - already sent")
            already_sent_count += 1
            continue

        print(f"[{idx + 1}/{end_idx}] Sending to Dr. {prof['name']} ({prof['email']})...")

        if send_email(GMAIL_ADDRESS, APP_PASSWORD, prof['email'], prof['name'], cv_path):
            success_count += 1
            # Log successful send
            log_entry = {
                "name": prof['name'],
                "email": prof['email'],
                "university": prof['university'],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "success"
            }
            sent_log.append(log_entry)
            save_sent_log(sent_log)
            sent_emails.add(prof['email'])  # Update the set
        else:
            fail_count += 1

    print("\n" + "=" * 80)
    print("BATCH SEND SUMMARY")
    print("=" * 80)
    print(f"✓ Sent successfully:  {success_count}")
    print(f"✗ Failed:             {fail_count}")
    print(f"⊘ Already sent:       {already_sent_count}")
    print(f"\nLog saved to: {SENT_LOG_FILE}")
    print("=" * 80)

def send_emails_to_faculty(faculty_list, data_file):
    """Send emails to faculty one by one with confirmation"""
    print("\n" + "=" * 80)
    print("SEND EMAILS")
    print("=" * 80)

    # Get CV path
    default_cv = "/home/sankalp/Downloads/resume_sankalp (2).pdf"
    cv_input = input(f"\nEnter CV path (Enter for default: {default_cv}): ").strip()
    cv_path = cv_input if cv_input else default_cv

    if not os.path.exists(cv_path):
        print(f"\nERROR: CV file not found at {cv_path}")
        return

    # Filter faculty with valid emails
    valid_faculty = [f for f in faculty_list if f['email'] and '@' in f['email']]
    missing_emails = [f for f in faculty_list if not f['email'] or '@' not in f['email']]

    print("\n" + "-" * 80)

    if missing_emails:
        print(f"⚠ WARNING: {len(missing_emails)} professors don't have email addresses:")
        for prof in missing_emails[:5]:  # Show first 5
            print(f"  - Dr. {prof['name']} ({prof['university']})")
        if len(missing_emails) > 5:
            print(f"  ... and {len(missing_emails) - 5} more")
        print()

    if not valid_faculty:
        print("ERROR: No valid email addresses found!")
        return

    print(f"Found {len(valid_faculty)} professors with valid email addresses.")
    print(f"Using Gmail: {GMAIL_ADDRESS}")
    print("-" * 80)

    # Load sent log
    sent_log = load_sent_log()

    # Create a set of emails that have already been sent
    sent_emails = {entry['email'] for entry in sent_log if entry.get('status') == 'success'}

    # Show faculty list with sent status
    print("\n" + "=" * 80)
    print("FACULTY LIST (showing first 20 and last 5)")
    print("=" * 80)

    # Show first 20
    display_limit = min(20, len(valid_faculty))
    for idx in range(display_limit):
        prof = valid_faculty[idx]
        status = "[SENT]" if prof['email'] in sent_emails else ""
        print(f"{idx + 1:3d}. Dr. {prof['name']:25s} | {prof['university']:20s} {status}")

    if len(valid_faculty) > 25:
        print(f"\n     ... {len(valid_faculty) - 25} professors in the middle ...")

    # Show last 5
    if len(valid_faculty) > 20:
        print()
        for idx in range(max(20, len(valid_faculty) - 5), len(valid_faculty)):
            prof = valid_faculty[idx]
            status = "[SENT]" if prof['email'] in sent_emails else ""
            print(f"{idx + 1:3d}. Dr. {prof['name']:25s} | {prof['university']:20s} {status}")

    print("=" * 80)

    # Ask where to start
    start_from_input = input(f"\nStart from which number? (1-{len(valid_faculty)}, or press Enter for 1): ").strip()

    if start_from_input:
        try:
            start_from = int(start_from_input)
            if start_from < 1 or start_from > len(valid_faculty):
                print(f"Invalid number. Starting from 1.")
                start_from = 1
        except ValueError:
            print(f"Invalid input. Starting from 1.")
            start_from = 1
    else:
        start_from = 1

    print(f"\n✓ Starting from professor #{start_from}")
    print("-" * 80)

    success_count = 0
    fail_count = 0
    skipped_count = 0

    # Send emails one by one, starting from the specified index
    for idx in range(start_from - 1, len(valid_faculty)):
        prof = valid_faculty[idx]
        while True:  # Loop to allow editing
            print("\n" + "=" * 80)
            print(f"EMAIL {idx + 1} of {len(valid_faculty)}")
            print("=" * 80)
            print(f"Name:       Dr. {prof['name']}")
            print(f"University: {prof['university']}")
            print(f"Email:      {prof['email']}")
            if prof['email'] in sent_emails:
                print(f"Status:     ⚠ ALREADY SENT (check log)")
            print("=" * 80)

            choice = input("\nSend this email? (yes/no/edit/quit): ").strip().lower()

            if choice == 'quit':
                print("\nStopping email sending.")
                break
            elif choice == 'edit':
                print(f"\nCurrent email: {prof['email']}")
                new_email = input("Enter new email address: ").strip()
                if new_email and '@' in new_email:
                    prof['email'] = new_email
                    print(f"✓ Email updated to: {new_email}")
                    # Save the updated faculty list to file
                    with open(data_file, 'w') as f:
                        json.dump(faculty_list, f, indent=2)
                    print(f"✓ Changes saved to {data_file}")
                    continue  # Show details again with updated email
                else:
                    print("Invalid email. Keeping original.")
                    continue
            elif choice == 'no':
                print("Skipped.")
                skipped_count += 1
                break
            elif choice == 'yes':
                # Send the email
                if send_email(GMAIL_ADDRESS, APP_PASSWORD, prof['email'], prof['name'], cv_path):
                    success_count += 1
                    # Log successful send
                    log_entry = {
                        "name": prof['name'],
                        "email": prof['email'],
                        "university": prof['university'],
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "success"
                    }
                    sent_log.append(log_entry)
                    save_sent_log(sent_log)
                else:
                    fail_count += 1
                break
            else:
                print("Invalid choice. Please enter yes/no/edit/quit")
                continue

        # Break outer loop if quit was chosen
        if choice == 'quit':
            break

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Sent successfully: {success_count}")
    print(f"✗ Failed:           {fail_count}")
    print(f"⊘ Skipped:          {skipped_count}")
    print(f"\nLog saved to: {SENT_LOG_FILE}")
    print("=" * 80)

def main_menu():
    """Display main menu and handle user choice"""
    print("\n" + "=" * 80)
    print(" " * 20 + "FACULTY EMAIL SENDER")
    print("=" * 80)
    print("\n1. View faculty list")
    print("2. Add new faculty")
    print("3. Edit faculty")
    print("4. Delete faculty")
    print("5. Send emails to all faculty (interactive)")
    print("6. Batch send emails (specify range)")
    print("7. Save and exit")
    print()

    choice = input("Enter your choice (1-7): ").strip()
    return choice

def main():
    """Main program loop"""
    print("\n" + "=" * 80)
    print(" " * 15 + "FACULTY EMAIL SENDER FOR PhD APPLICATIONS")
    print("=" * 80)

    # Ask user which file to use
    print("\nSelect data file:")
    print("1. faculty_emails.json (344 professors - REAL)")
    print("2. test_emails.json (Test emails)")

    file_choice = input("\nEnter choice (1 or 2): ").strip()

    if file_choice == '2':
        data_file = TEST_FILE
        print(f"\n✓ Using TEST file: {TEST_FILE}")
    else:
        data_file = FACULTY_FILE
        print(f"\n✓ Using FACULTY file: {FACULTY_FILE}")

    faculty_list = load_faculty_data(data_file)

    if not faculty_list:
        print("\nNo faculty data loaded. Starting with empty list.")
        faculty_list = []

    while True:
        choice = main_menu()

        if choice == '1':
            display_faculty_list(faculty_list)
        elif choice == '2':
            faculty_list = add_faculty(faculty_list)
            save_faculty_data(faculty_list)
        elif choice == '3':
            faculty_list = edit_faculty(faculty_list)
            save_faculty_data(faculty_list)
        elif choice == '4':
            faculty_list = delete_faculty(faculty_list)
            save_faculty_data(faculty_list)
        elif choice == '5':
            send_emails_to_faculty(faculty_list, data_file)
        elif choice == '6':
            # Batch send
            valid_faculty = [f for f in faculty_list if f['email'] and '@' in f['email']]
            if not valid_faculty:
                print("\nERROR: No faculty with valid email addresses!")
            else:
                print(f"\nTotal professors with valid emails: {len(valid_faculty)}")
                try:
                    start_str = input("Enter start professor number: ").strip()
                    end_str = input("Enter end professor number: ").strip()
                    start_idx = int(start_str)
                    end_idx = int(end_str)
                    send_emails_batch(faculty_list, data_file, start_idx, end_idx)
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
        elif choice == '7':
            save_faculty_data(faculty_list)
            print("\n✓ Data saved. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-7.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
