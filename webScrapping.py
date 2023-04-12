import requests  # for the http requests

from bs4 import BeautifulSoup  # for web scraping

import smtplib  # for email autentication and transfers

from email.mime.multipart import MIMEMultipart  # used for creating the email body
from email.mime.text import MIMEText  # for the email body text.
import datetime

currentTime = datetime.datetime.now()

content = ""


# extracting the News Stories


def extractNews(url):
    print("Extracting News Stories....")
    blockcnt = ""
    blockcnt += "<b>HN Top Stories:</b>\n" + "<br>" + "-" * 50 + "<br>"
    response = requests.get(url)
    blockContent = response.content
    soup = BeautifulSoup(blockContent, "html.parser")
    for i, tag in enumerate(
        soup.find_all("td", attrs={"class": "title", "valign": ""})
    ):
        blockcnt += (
            (
                str(i + 1)
                + " :: "
                + '<a href="'
                + tag.a.get("href")
                + '">'
                + tag.text
                + "</a>"
                + "\n"
                + "<br>"
            )
            if tag.text != "More"
            else ""
        )
    return blockcnt


cnt = extractNews("https://news.ycombinator.com/")
content += cnt
content += "<br>----Email Finished----<br>"

# Sending the email.
print("Composing Email..Hold on :)....")

# update your email details
# make sure to update the Google Low App Access settings before

SERVER = "smtp.gmail.com"  # "The email server-base". smtp server for gmail
PORT = 587  # port number for gmail
FROM = "**ericaddojr@gmail.com"  # "from email address" ENTER
TO = "ericaddojr@gmail.com"  #  to email address(es)  ENTER
FROMPASS = "******"  # Password of *From* address above. ENTER. If 2Fa is on your google account, you need to generate an app access password from myaccount.google.com/security by searching 'app password' in the search bar. :)

# Creating message body
msg = MIMEMultipart()

msg[
    "Subject"
] = (  # Email subject below. Concatenating with date and time to create a unique subject every time to escape gmail's torture :)
    "Top News Stories HN [Automated Email]"
    + " "
    + str(currentTime.day)
    + "-"
    + str(currentTime.month)
    + "-"
    + str(currentTime.year)
)
msg["From"] = FROM
msg["To"] = TO

msg.attach(MIMEText(content, "html"))

print("Initiating Server...")

server = smtplib.SMTP(SERVER, PORT)  # SERVER and PORT above
server.set_debuglevel(1)  # want to see error messages
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, FROMPASS)  # login into the FROM email.
server.sendmail(FROM, TO, msg.as_string())  # Send the email.

print("Email Sent...")

server.quit()  # Quit from the server afterwards.


# ++EAJ++
