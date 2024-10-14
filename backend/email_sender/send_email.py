import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import MAIL_USERNAME, APP_PASSWORD

def generate_email(to_email, subject, body, query):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = MAIL_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Combine body and query into a single message
    full_body = f"<h3>Your search: {query}</h3><br>{body}"  # Concatenate body and query in HTML format
    
    # Attach the combined body to the email
    msg.attach(MIMEText(full_body, 'html'))  # 'html' for HTML format

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            print("Connecting to server...")
            server.set_debuglevel(1)  # Add debugging information
            print("Starting TLS...")
            server.starttls()
            print("Logging in...")
            server.login(MAIL_USERNAME, APP_PASSWORD)
            print("Sending email...")
            server.sendmail(MAIL_USERNAME, to_email, msg.as_string())
        return "Email sent successfully!"
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed. Error: {e}")
        print("Please check your email and password, and make sure you've allowed less secure apps or are using an app-specific password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

