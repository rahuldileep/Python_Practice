#!/usr/bin/env python3

import reports
import emails
import os
from datetime import date

def main():
  dir = os.path.dirname(os.path.abspath(__file__))
  desc_dir = dir + "/supplier-data/descriptions"
  summary = []
  for infile in os.listdir(desc_dir):
    file_path = os.path.join(desc_dir,infile)
    with open(file_path) as fp:
      reader = fp.read().splitlines()
      summary.append("")
      summary.append('name: '+ reader[0].strip())
      summary.append('weight: '+ reader[1].strip())
  today = date.today()
  current_date = today.strftime("%B %d, %Y")
  reports.generate_report('/tmp/processed.pdf', "Process Update on " + current_date, "<br/>".join(summary),"")
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)

if __name__ == "__main__":
  main()