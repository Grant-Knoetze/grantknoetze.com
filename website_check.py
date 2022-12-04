#!/usr/bin/env python3
from email.message import EmailMessage

import http.client
import smtplib


def main():
    """Main function"""


def get_website():
    """Use the GET method on a given domain
    and return 200 OK response if site is up"""
    conn = http.client.HTTPConnection('www.grantknoetze.com')
    conn.request("GET", "/")
    resp1 = conn.getresponse()
    print(resp1.status, resp1.reason)
    data1 = resp1.read()
    print(data1)
    if data1:
        return data1


def send_email():
    # Open the plain text file whose name is in textfile for reading.
    with open("C:\\Users\\grant\\OneDrive\\Documents\\grantknoetze.com\\message.txt") as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = "Website is up"
        msg['From'] = "grant@sendemail.com"
        msg['To'] = "grant2@sendemail.com"

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()


if __name__ == "__main__":
    get_website()
    send_email()
