import random
import time
import smtplib
from email.message import EmailMessage
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sends important letter about art to the galleries listed in '
                                                 'mailing_list.txt')
    parser.add_argument('s', metavar='Sender', help='sender email')
    args = parser.parse_args()
    textfile = 'mailing_list.txt'
    sender = args.s
    msg = EmailMessage()
    msg.set_content('Art is useless')
    with open(textfile) as fp:
        address = [x.strip().replace('\n','') for x in fp.readlines()]
    msg['Subject'] = f'Supporting message explains much'
    msg['From'] = sender
    msg['To'] = address
    s = smtplib.SMTP('localhost')
    sleep = 0
    while True:
        print(f'sleeping for {sleep} secs')
        time.sleep(sleep)
        try:
            s.send_message(msg)
            print("letter is sent")
        except:
            print("letter is not sent")
        sleep = random.randint(34, 99)
        # 34 are years passed from Joseph Beuys birth, 99 from his death
