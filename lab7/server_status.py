#!/usr/bin/env python3
import subprocess
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

sender = 'your@gmail.com'
password = 'your_app_pass'
receiver = 'owner@example.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

cpu = subprocess.getoutput("top -bn1 | grep 'Cpu(s)' | awk '{print $2}' | cut -d'%' -f1")
disk = subprocess.getoutput("df -h / | awk 'NR==2 {print $5}'")
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

body = f"""
Server Status Report ({timestamp})
CPU Usage: {cpu}%
Disk Usage (/): {disk}

Generated automatically.
"""

msg = MIMEText(body)
msg['Subject'] = 'Server Status Update'
msg['From'] = sender
msg['To'] = receiver

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
