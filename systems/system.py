'''
** ** ** ** **
Code Filename: main.py
Course: PSP0201 Mini IT Project 
Trimester: 2030
Lecture Section: TC1V
Tutorial Section: TT2V

Student Name as per MMU 1: Chua Hui Yi
Student ID 1: 1201100840
Email 1: 1201100840@student.mmu.edu.my
Phone 1: 010-7843168

Student Name as per MMU 2: Edwin Lim Cheng Yin
Student ID 2: 1201100287
Email 2: 1201100287@student.mmu.edu.my
Phone 2: 016-2152148

Student Name as per MMU 3: Lim Yuen Khai
Student ID 3: 1201100842
Email 3: 1201100842@student.mmu.edu.my
Phone 3: 011-60977732

Student Name as per MMU 4: Muhammad Haikal bin Lokman
Student ID 4: 1201100844 
Email 4: 1201100844@student.mmu.edu.my
Phone 4: 019-2580817
** ** ** ** **
'''


###########################
# TKINTER SYSTEM SETTINGS #
###########################

### IMPORT MODULES
from tkinter import *
from tkinter import ttk

### Tkinter Root Settings
root = Tk()
root.title("Bus Ticketing System")
root.iconbitmap("./imgs/bus_icon.ico")
root.resizable(False, False)

## Treeview Style
style = ttk.Style()
style.map('Treeview')
style.theme_use("default")

## Geometry
WIDTH = '740'
HEIGHT = '550'
root.geometry(WIDTH + 'x' + HEIGHT)