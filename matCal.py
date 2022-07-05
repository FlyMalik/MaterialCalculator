from tkinter import *

screen = Tk()
screen.geometry('750x500')
screen.title('Cement-Sand-Granite Calculator')

intro_label1 = Label(text='This program is designed to calculate the'
                          ' amount of Cement, Sand, & Granite needed in a given Cubic Meter (m\u00B3).'
                     , font=('arial', 10, 'bold'))
intro_label2 = Label(text='This Program was written by Abdulmalik, I. O. (MNIOB)'
                     , font=('arial', 12, 'bold'))


# Button Functions
def clear():
    lgt_entry.delete(0, END)
    wdt_entry.delete(0, END)
    dpt_entry.delete(0, END)
    cmt_entry.delete(0, END)
    snd_entry.delete(0, END)
    grn_entry.delete(0, END)
    bag_entry.delete(0, END)
    dim_entry.delete(0, END)
    tnG_entry.delete(0, END)
    tnS_entry.delete(0, END)
    fdb_entry.delete(0, END)
    fdb_entry.insert(0, grt)


# gridding of intros
intro_label1.grid(row=0, column=0)
intro_label2.grid(row=1, column=0)

# screen definitions for labels
length_label = Label(screen, text='Enter Length of Concrete in meter:', font=('calibre', 10))
width_label = Label(text='Enter Width of Concrete in meter:', font=('calibre', 10))
depth_label = Label(text='Enter Depth of Concrete in meter:', font=('calibre', 10))
dimension_label = Label(text='The Dimension of your Concrete is:', font=('calibre', 10, 'bold'))
ratio_label = Label(text='Enter the Mix Ratio in their respective fields (i.e 1:2:4)',
                    font=('calibre', 10, 'italic', 'bold'))
cement_label = Label(text='Cement ratio:', font=('calibre', 10))
sand_label = Label(text='Sand ratio:', font=('calibre', 10))
granite_label = Label(text='Granite ratio:', font=('calibre', 10))
require_label = Label(text='You will require approximately:', font=('calibre', 10, 'bold'))
bags_label = Label(text='bag(s) of Cement', font=('calibre', 10))
tonS_label = Label(text='ton(s) of Sand', font=('calibre', 10))
tonG_label = Label(text='ton(s) of Granite', font=('calibre', 10))
feedback_label = Label(text="Program's Feedback", font=('calibre', 10, 'bold'))
si_label1 = Label(text='m')
si_label2 = Label(text='m')
si_label3 = Label(text='m')
si_label4 = Label(text='m\u00B3', font='bold')

# screen definition for entry & button
lgt_entry = Entry(textvariable='numbers only', width=15)
wdt_entry = Entry(width=15)
dpt_entry = Entry(width=15)
dim_entry = Entry(width=20, font='bold', cursor='none', border=0.5)
cmt_entry = Entry(width=10)
snd_entry = Entry(width=10)
grn_entry = Entry(width=10)
bag_entry = Entry(width=15, font='bold', cursor='none', border=0.5)
tnS_entry = Entry(width=15, font='bold', cursor='none', border=0.5)
tnG_entry = Entry(width=15, font='bold', cursor='none', border=0.5)
fdb_entry = Entry(width=70, font='bold', cursor='none', border=.5, fg= 'green')
# cal_button = Button(text='CALCULATE MATERIAL', font=('arial', 16, 'bold'), border=5)
rst_button = Button(text='RESET PROGRAM', font=('arial', 16, 'bold'), border=5, command=clear)

# Entry functions
lgt_entry.insert(0, 'Numbers Only')
lgt_entry.delete(0, END)

# Packing spots for labels
length_label.place(x=80, y=50)
width_label.place(x=80, y=70)
depth_label.place(x=80, y=90)
ratio_label.place(x=20, y=140)
cement_label.place(x=80, y=160)
sand_label.place(x=80, y=180)
granite_label.place(x=80, y=200)
dimension_label.place(x=20, y=285)
require_label.place(x=20, y=310)
bags_label.place(x=160, y=330)
tonS_label.place(x=160, y=350)
tonG_label.place(x=160, y=370)
feedback_label.place(x=20, y=410)
si_label1.place(x=395, y=50)
si_label2.place(x=395, y=70)
si_label3.place(x=395, y=90)
si_label4.place(x=435, y=285)

# packing for entry & button
lgt_entry.place(x=300, y=50)
wdt_entry.place(x=300, y=70)
dpt_entry.place(x=300, y=90)
cmt_entry.place(x=180, y=160)
snd_entry.place(x=180, y=180)
grn_entry.place(x=180, y=200)
dim_entry.place(x=250, y=285)
bag_entry.place(x=20, y=330)
tnS_entry.place(x=20, y=350)
tnG_entry.place(x=20, y=370)
fdb_entry.place(x=20, y=430)
# cal_button.place(x=20, y=237)
rst_button.place(x=320, y=230)

grt = 'Hello user, enter only numbers in the spaces provided'
fdb_entry.insert(0, grt)


# Maths variables
def calculate():
    try:
        # Error definitions
        mess = 'Thank you for using this Program'
        mess2 = '  Reset Program and enter only numbers'
        err1 = 'Negative number entered,kindly check and enter positive numbers only. Thank You'
        err2 = 'You entered a Zero (0), kindly check and enter positive numbers only. Thank You'
        err3 = 'All parameters were not entered, kindly check and enter positive numbers only. Thank You'
        err4 = 'The quantity entered is too small. Cement is less than Half bag.  Thank You'
        err5 = 'You entered an invalid entry'

        # concrete volume section
        length = float(lgt_entry.get())
        width = float(wdt_entry.get())
        depth = float(dpt_entry.get())
        cubic = length * width * depth
        dimension = round(cubic, 2)
        dim_entry.delete(0, END)
        dim_entry.insert(0, dimension)

        # material section
        cement_factor = 1440
        sand_factor = 1450
        granite_factor = 1550
        k2 = 50
        k3 = 1000
        cement_ratio = int(cmt_entry.get())
        sand_ratio = int(snd_entry.get())
        granite_ratio = int(grn_entry.get())
        total_ratio = cement_ratio + sand_ratio + granite_ratio
        cement_co = cement_ratio / total_ratio
        sand_co = sand_ratio / total_ratio
        granite_co = granite_ratio / total_ratio
        # Cement
        cement1 = cement_co * dimension
        cement2 = cement1 * cement_factor
        cement3 = cement2 / k2
        cement_final = round(cement3, 2)
        # Sand
        sand1 = sand_co * dimension
        sand2 = sand1 * sand_factor
        sand3 = sand2 / k3
        sand_final = round(sand3, 2)
        # Granite
        granite1 = granite_co * dimension
        granite2 = granite1 * granite_factor
        granite3 = granite2 / k3
        granite_final = round(granite3, 2)

        # On Screen
        bag_entry.delete(0, END)
        bag_entry.insert(0, cement_final)
        tnS_entry.delete(0, END)
        tnS_entry.insert(0, sand_final)
        tnG_entry.delete(0, END)
        tnG_entry.insert(0, granite_final)

        # For feedback section
        fdb_entry.delete(0, END)
        if dimension > 0:
            fdb_entry.delete(0, END)
            fdb_entry.insert(0, mess)

    except ValueError as err5:
        fdb_entry.delete(0, END)
        fdb_entry.insert(0, mess2)
        fdb_entry.insert(0, err5)

    except ZeroDivisionError as err6:
        fdb_entry.delete(0, END)
        fdb_entry.insert(0, mess2)
        fdb_entry.insert(0, err6)
    except TypeError as err7:
        fdb_entry.delete(0, END)
        fdb_entry.insert(0, mess2)
        fdb_entry.insert(0, err7)



cal_button = Button(text='CALCULATE MATERIAL', font=('arial', 16, 'bold'), border=5, command=calculate)
cal_button.place(x=20, y=230)
screen.mainloop()

