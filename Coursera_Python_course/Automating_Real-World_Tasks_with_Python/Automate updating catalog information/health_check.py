#!/usr/bin/env python3

import emails
import psutil
import shutil
import socket

def report_error(cpu_usage,free_hdd,memory,localhost):
  if cpu_usage >= 80:
    sender = "automation@example.com"
    receiver = "student-04-e7ec473da45a@example.com"
    subject = "Error - CPU usage is over 80%"
    body = "Please check your system and resolve the isssue an soon as possible"
    message = emails.generate_email(sender,receiver,subject,body,"")
    emails.send(message)
  if free_hdd <= 20:
    sender = "automation@example.com"
    receiver = "student-04-e7ec473da45a@example.com"
    subject = "Error - available disk space is lower than 20%"
    body = "Please check your system and resolve the isssue an soon as possible"
    message = emails.generate_email(sender,receiver,subject,body,"")
    emails.send(message)

  if memory <= 0.5:
    sender = "automation@example.com"
    receiver = "student-04-e7ec473da45a@example.com"
    subject = "Error - available memory is less than 500MB"
    body = "Please check your system and resolve the isssue an soon as possible"
    message = emails.generate_email(sender,receiver,subject,body,"")
    emails.send(message)

  if localhost != "127.0.0.1":
    sender = "automation@example.com"
    receiver = "student-04-e7ec473da45a@example.com"
    subject = "Error - the hostname 'localhost' cannot be resolved to 127.0.0.1"
    body = "Please check your system and resolve the isssue an soon as possible"
    message = emails.generate_email(sender,receiver,subject,body,"")
    emails.send(message)
def main():
  cpu_usage = psutil.cpu_percent(interval = 10)
  total, used, free = shutil.disk_usage('/')
  free_hdd = (free/total)*100
  available_memory = psutil.virtual_memory()._asdict()['available']/(2**30)
  localhost = socket.gethostbyname('localhost')
  print(cpu_usage,free_hdd,available_memory,localhost)
  report_error(cpu_usage,free_hdd,available_memory,localhost)
  
if __name__ == "__main__":
  main()