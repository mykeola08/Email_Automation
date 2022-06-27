import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Program is working
# Send personalised email to multiple contacts
data = [
    # (NAME, EMAIL, SUBJECT_LINE, YOUTUBE_VIDEO_LINK)
    ("salami12", "salami12michael789@gmail.com", "", "https://youtube.com"),
    ("salami123", "salami123michael6789@gmail.com", "", "https://youtube.com"),
    ("myke08", "mykeola08@gmail.com", "", "https://youtube.com"),

]
my_email = 'salamimichael789@gmail.com'
my_pass = input(f"Enter password for {my_email}: ")
subject = 'Testing mail with youtube tutorial'

for email in data:
    name = email[0]
    address = email[1]
    sbj = email[2]
    video_link = email[3]
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.login(my_email, my_pass)

            msg = MIMEMultipart("alternatives")
            msg['From'] = my_email
            msg['To'] = f"{address}"
            msg['Subject'] = subject

            content = f"""/
            <html>
                <head>
                </head>
                <body style="max-width:800px; font-size:20px;">
                    <p style="margin:3%;">Hi {name},<br>
                    <br>
                    I know your busy but this would only take 60 seconds to read.<br>
                    <br>
                    Here is the link to know more about your <a href="{video_link}">website</a>.</p>
                    <br>
                    <hr style="height:1px; width:80%; margin:auto;">
                    <p style="margin:3%; text-align:center; padding-bottom:3%;">Michael Oladimeji<br>
                    Digital Strategist</p>
                </body>
            </html>"""

            # textPart = MIMEText(content, 'plain')
            htmlPart = MIMEMultipart(content, 'html')
            msg.attach(htmlPart)
            # msg.attach(textPart, htmlPart)
            message = msg.as_string()
            
            smtp.sendmail("salamimichael789@gmail.com", address, message)
            time.sleep(5)
            print(f"Email sent to {address}")
            smtp.quit()
    except Exception as e:
        print(e)
