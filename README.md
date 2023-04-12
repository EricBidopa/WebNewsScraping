# WebNewsScraping
This script scraps latest news on ycombinator's hacker news website and sends them to your email

# Definitions

Python script that scrapes top news stories from the Hacker News website and sends an email 
containing the scraped content to a specified email address.

## The code makes extensive use of the following libraries:

requests:
for making HTTP requests to the website
BeautifulSoup:
for parsing the HTML content of the website and extracting the news stories
smtplib:
for sending the email
email.mime:
for creating the email message body

The code defines a function extractNews which takes a URL as input, sends a 
GET request to the URL, and then uses BeautifulSoup to extract the top
 news stories from the HTML content of the website. The extracted news stories are returned as a string.

 The code then calls the extractNews function to scrape the top news stories 
 from Hacker News and adds the scraped content to a string variable content.

 Next, the code creates an email message body by attaching the content 
 string to an instance of MIMEMultipart. The code also sets the email subject, 
 from address, and to address.

 The code then sets up an SMTP server to send the email using smtplib, 
 logs in to the from email address using the provided password, sends the email message, 
 and finally quits the server.

Note that some variables in the code (such as the from email address, password, and to email address)
should be updated to match your email credentials. 


# Getting Started
1. Install all library listed above. most of them comes with python installation by default.
2. clone this repository 'git clone ......'. replace '..........' with the SSH link.
3. navigate the code to locate the input section of your email credentials (email address and your server's SMTP port, etc.)
4. input into the password section(FROMPASS) the password of the email account that you specified.If that email account has 
2Fa enables, you will have to disable it in your google account or generate 'app password' from google by searching 'app password'
in your search tab in your google account security page :)
 


# Cheers!










