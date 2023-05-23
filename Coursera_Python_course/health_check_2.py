#!/usr/bin/env python3
import psutil
import shutil
import socket
import emails
import os

def alert(cpu_usage, free_hdd, memory, localhost):
    
    if cpu_usage >= 80:
        # TODO: send the PDF report as an email attachment
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - CPU usage is over 80%"
        body = "Please check your system and resolve the isssue an soon as possible"
        message = emails.generate(sender,receiver,subject,body,"")
        emails.send(message)

    if free_hdd <= 20:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - available disk space is lower than 20%"
        body = "Please check your system and resolve the isssue an soon as possible"
        message = emails.generate(sender,receiver,subject,body,"")
        emails.send(message)

    if memory <= 0.5:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - available memory is less than 500MB"
        body = "Please check your system and resolve the isssue an soon as possible"
        message = emails.generate(sender,receiver,subject,body,"")
        emails.send(message)
    
    if localhost != "127.0.0.1":
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - the hostname 'localhost' cannot be resolved to 127.0.0.1"
        body = "Please check your system and resolve the isssue an soon as possible"
        message = emails.generate(sender,receiver,subject,body,"")
        emails.send(message)


cpu_usage = psutil.cpu_percent(interval=3)
total, used, free = shutil.disk_usage('/')
free_hdd = free/total*100
memory = psutil.virtual_memory()._asdict()['available']//2**30
localhost = socket.gethostbyname('localhost')
print("Current CPU(%) = " + str(cpu_usage))
print("Current Disk_Space(%) = {:.2f} (%) ".format(free_hdd))
print("Current Memory(GB) = " + str(memory))
print("Current local_host : {}".format(localhost))
alert(cpu_usage, free_hdd, memory, localhost)