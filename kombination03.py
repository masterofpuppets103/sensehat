#!/usr/bin/python
import sys
import time
import random
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

##visualization of four different ways with functions und picks randomly next one

##neue Farbe kreieren
def newcolor():
    colorone =random.randint(0,255)
    colortwo =random.randint(0,255)
    colorthree =random.randint(0,255)
    color= [colorone, colortwo, colorthree]
    return(color)

def begin(setcolor):
    x =4
    for y in range(1, 8):
        sense.set_pixel(x, y, setcolor)

def second(setcolor):
    for y in range(1, 8):
        x = 8-y
        sense.set_pixel(x, y, setcolor)
def third(setcolor):
    y = 4
    for x in range(1, 8):
        sense.set_pixel(x, y, setcolor)
def fourth(setcolor):
    for x in range(1, 8):
        sense.set_pixel(x, x, setcolor)
def kreis():
    color = newcolor();
    begin(color)
    time.sleep(0.1)
    second(color)
    time.sleep(0.1)
    third(color)    
    time.sleep(0.1)
    fourth(color)
    time.sleep(0.2)

def loop(min, max,setcolor):
    for y in range(min, max):
        sense.set_pixel(y,min, setcolor)#oben
        sense.set_pixel(y,max-1, setcolor)#unten
        sense.set_pixel(min,y, setcolor)#linke seite
        sense.set_pixel(max-1,y, setcolor)#rechte Seite

def quadrat():
    color = newcolor();
    counter = 1
    sense.set_pixel(4, 4, color)
    for k in range(6,9):
        i = 4-counter
        counter = counter +1
        loop(i,k,color)
        time.sleep(0.25)
        #sense.clear()

def linksrechts():
    color = newcolor();
    for y in range(1,8):
        for x in range(1, 8): ##mache alles von oben nach unten blau
            sense.set_pixel(x, y, color)
        time.sleep(0.25)
    time.sleep(0.25)

def obenunten():
    color = newcolor();
    for x in range(1,8):
        for y in range(1, 8): ##mache alles von links nach rechts farbig
             sense.set_pixel(x, y, color)
        time.sleep(0.25)
    time.sleep(0.25)

def letter():
    color = newcolor();
    letters = ["0","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i =random.randint(0,36)
    sense.show_letter(letters[i], color)
    time.sleep(0.5)

while True:
    nextone =random.randint(0,4)
    #print (nextone)
    if nextone == 0:
        linksrechts()
    elif nextone == 1:
        obenunten()
    elif nextone == 2:
        for z in range(0,2):
            kreis()
    elif nextone == 3:
        quadrat()
    elif nextone == 4:
        letter()
