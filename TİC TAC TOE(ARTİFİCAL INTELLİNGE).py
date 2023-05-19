import tkinter as tk
import random
import time
from tkinter import *
from tkinter import messagebox

a = random.choice(["red","blue","lime"])
b = random.choice(["orange","white","pink","black","purple"])
c = random.choice(["red","blue","lime"])
d = random.choice(["orange","white","pink","black","purple"])

random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]

RANDOM_LİST_REAL = random.choice(random_list)

BOOL = True

tic_tac_toe = tk.Tk()

def Aİ():
    global BOOL
    global random_list
    global RANDOM_LİST_REAL
    if BOOL == False:
        if RANDOM_LİST_REAL == "a1":
            if a1_1["text"] == "":
                a1.place(width = 100,height = 100,x = 0,y = 1000)
                a1_1["text"] = "O"
                random_list.remove("a1")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a1_1["text"] != "":
                if RANDOM_LİST_REAL == "a1":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL
            
        if RANDOM_LİST_REAL == "a2":
            if a2_1["text"] == "":
                a2.place(width = 100,height = 100,x = 0,y = 1000)
                a2_1["text"] = "O"
                random_list.remove("a2")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a2_1["text"] != "":
                if RANDOM_LİST_REAL == "a2":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL
            
        if RANDOM_LİST_REAL == "a3":
            if a3_1["text"] == "":
                a3.place(width = 100,height = 100,x = 0,y = 1000)
                a3_1["text"] = "O"
                random_list.remove("a3")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a3_1["text"] != "":
                if RANDOM_LİST_REAL == "a3":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL
            
        if RANDOM_LİST_REAL == "a4":
            if a4_1["text"] == "":
                a4.place(width = 100,height = 100,x = 0,y = 1000)
                a4_1["text"] = "O"
                random_list.remove("a4")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a4_1["text"] != "":
                if RANDOM_LİST_REAL == "a4":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL
            
        if RANDOM_LİST_REAL == "a5":
            if a5_1["text"] == "":
                a5.place(width = 100,height = 100,x = 0,y = 1000)
                a5_1["text"] = "O"
                random_list.remove("a5")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a5_1["text"] != "":
                if RANDOM_LİST_REAL == "a5":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL

        if RANDOM_LİST_REAL == "a6":
            if a6_1["text"] == "":
                a6.place(width = 100,height = 100,x = 0,y = 1000)
                a6_1["text"] = "O"
                random_list.remove("a6")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a6_1["text"] != "":
                if RANDOM_LİST_REAL == "a6":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL

        if RANDOM_LİST_REAL == "a7":
            if a7_1["text"] == "":
                a7.place(width = 100,height = 100,x = 0,y = 1000)
                a7_1["text"] = "O"
                random_list.remove("a7")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a7_1["text"] != "":
                if RANDOM_LİST_REAL == "a7":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL

        if RANDOM_LİST_REAL == "a8":
            if a8_1["text"] == "":
                a8.place(width = 100,height = 100,x = 0,y = 1000)
                a8_1["text"] = "O"
                random_list.remove("a8")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0

            if a8_1["text"] != "":
                if RANDOM_LİST_REAL == "a8":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL

        if RANDOM_LİST_REAL == "a9":
            if a9_1["text"] == "":
                a9.place(width = 100,height = 100,x = 0,y = 1000)
                a9_1["text"] = "O"
                random_list.remove("a9")
                RANDOM_LİST_REAL = random.choice(random_list)
                BOOL = True
                return 0
            
            if a9_1["text"] != "":
                if RANDOM_LİST_REAL == "a9":
                    BOOL = False
                    RANDOM_LİST_REAL = random.choice(random_list)
                    return Aİ()
                    return RANDOM_LİST_REAL
 
def a1():
    global BOOL
    global random_list
    if BOOL == True:
        a1.place(width = 100,height = 100,x = 0,y = 1000)
        a1_1["text"] = "X"
        random_list.remove("a1")
        BOOL = False
        Aİ()

def a2():
    global BOOL
    if BOOL == True:
        a2.place(width = 100,height = 100,x = 0,y = 1000)
        a2_1["text"] = "X"
        random_list.remove("a2")
        BOOL = False
        Aİ()

def a3():
    global BOOL
    if BOOL == True:
        a3.place(width = 100,height = 100,x = 0,y = 1000)
        a3_1["text"] = "X"
        random_list.remove("a3")
        BOOL = False
        Aİ()
        
def a4():
    global BOOL
    if BOOL == True:
        a4.place(width = 100,height = 100,x = 0,y = 1000)
        a4_1["text"] = "X"
        random_list.remove("a4")
        BOOL = False
        Aİ()

def a5():
    global BOOL
    if BOOL == True:
        a5.place(width = 100,height = 100,x = 0,y = 1000)
        a5_1["text"] = "X"
        random_list.remove("a5")
        BOOL = False
        Aİ()
        
def a6():
    global BOOL
    if BOOL == True:
        a6.place(width = 100,height = 100,x = 0,y = 1000)
        a6_1["text"] = "X"
        random_list.remove("a6")
        BOOL = False
        Aİ()
        
def a7():
    global BOOL
    if BOOL == True:
        a7.place(width = 100,height = 100,x = 0,y = 1000)
        a7_1["text"] = "X"
        random_list.remove("a7")
        BOOL = False
        Aİ()
       
def a8():
    global BOOL
    if BOOL == True:
        a8.place(width = 100,height = 100,x = 0,y = 1000)
        a8_1["text"] = "X"
        random_list.remove("a8")
        BOOL = False
        Aİ()

def a9():
    global BOOL
    if BOOL == True:
        a9.place(width = 100,height = 100,x = 0,y = 1000)
        a9_1["text"] = "X"
        random_list.remove("a9")
        BOOL = False
        Aİ()

def tic_tac_toe_control():
    global BOOL
    global random_list
    acxz1 = player_x.get()
    if a1_1["text"] == "X" and a2_1["text"] == "X" and a3_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a4_1["text"] == "X" and a5_1["text"] == "X" and a6_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a7_1["text"] == "X" and a8_1["text"] == "X" and a9_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a1_1["text"] == "X" and a4_1["text"] == "X" and a7_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a2_1["text"] == "X" and a5_1["text"] == "X" and a8_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a3_1["text"] == "X" and a6_1["text"] == "X" and a9_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a1_1["text"] == "X" and a5_1["text"] == "X" and a9_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a3_1["text"] == "X" and a5_1["text"] == "X" and a7_1["text"] == "X":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)",str(acxz1)+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a1_1["text"] == "O" and a2_1["text"] == "O" and a3_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a4_1["text"] == "O" and a5_1["text"] == "O" and a6_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a7_1["text"] == "O" and a8_1["text"] == "O" and a9_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a1_1["text"] == "O" and a4_1["text"] == "O" and a7_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a2_1["text"] == "O" and a5_1["text"] == "O" and a8_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a3_1["text"] == "O" and a6_1["text"] == "O" and a9_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a1_1["text"] == "O" and a5_1["text"] == "O" and a9_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    elif a3_1["text"] == "O" and a5_1["text"] == "O" and a7_1["text"] == "O":
        well_done = Tk()
        well_done.withdraw()
        messagebox.showinfo("WELL DONE :)","DRUNK MASTER"+" WON THİS GAME :)")
        BOOL = True
        a1_1["text"] = ""
        a2_1["text"] = ""
        a3_1["text"] = ""
        a4_1["text"] = ""
        a5_1["text"] = ""
        a6_1["text"] = ""
        a7_1["text"] = ""
        a8_1["text"] = ""
        a9_1["text"] = ""
        a1.place(width = 100,height = 100,x = 0,y = 100)
        a2.place(width = 100,height = 100,x = 100,y = 100)
        a3.place(width = 100,height = 100,x = 200,y = 100)
        a4.place(width = 100,height = 100,x = 0,y = 200)
        a5.place(width = 100,height = 100,x = 100,y = 200)
        a6.place(width = 100,height = 100,x = 200,y = 200)
        a7.place(width = 100,height = 100,x = 0,y = 300)
        a8.place(width = 100,height = 100,x = 100,y = 300)
        a9.place(width = 100,height = 100,x = 200,y = 300)
        random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
        return tic_tac_toe_control()
    
    tic_tac_toe.after(10,tic_tac_toe_control)

def REF():
    global BOOL
    global random_list
    a1_1["text"] = ""
    a2_1["text"] = ""
    a3_1["text"] = ""
    a4_1["text"] = ""
    a5_1["text"] = ""
    a6_1["text"] = ""
    a7_1["text"] = ""
    a8_1["text"] = ""
    a9_1["text"] = ""
    a1.place(width = 100,height = 100,x = 0,y = 100)
    a2.place(width = 100,height = 100,x = 100,y = 100)
    a3.place(width = 100,height = 100,x = 200,y = 100)
    a4.place(width = 100,height = 100,x = 0,y = 200)
    a5.place(width = 100,height = 100,x = 100,y = 200)
    a6.place(width = 100,height = 100,x = 200,y = 200)
    a7.place(width = 100,height = 100,x = 0,y = 300)
    a8.place(width = 100,height = 100,x = 100,y = 300)
    a9.place(width = 100,height = 100,x = 200,y = 300)
    random_list = ["a1","a2","a3","a4","a5","a6","a7","a8","a9"]
    BOOL = True

tic_tac_toe.title("TİC TAC TOE")
tic_tac_toe.geometry("300x450+500+130")
tic_tac_toe.minsize(300,450)
tic_tac_toe.maxsize(300,450)

player_x_info = tk.Label(tic_tac_toe,text = "PLAYER 1\n(X):",fg = c,bg = d,font = "verdana 15")
player_x_info.place(width = 100,height = 50,x = 0,y = 0)
player_x = tk.Entry(tic_tac_toe,fg = c,bg = d,font = "verdana 20")
player_x.place(width = 200,height = 50,x = 100,y = 0)

player_y_info = tk.Label(tic_tac_toe,text = "PLAYER (Y): DRUNK MASTER",fg = c,bg = d,font = "verdana 15")
player_y_info.place(width = 300,height = 50,x = 0,y = 50)

a1_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a1_1.place(width = 100,height = 100,x = 0,y = 100)
a2_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a2_1.place(width = 100,height = 100,x = 100,y = 100)
a3_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a3_1.place(width = 100,height = 100,x = 200,y = 100)

a4_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a4_1.place(width = 100,height = 100,x = 0,y = 200)
a5_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a5_1.place(width = 100,height = 100,x = 100,y = 200)
a6_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a6_1.place(width = 100,height = 100,x = 200,y = 200)

a7_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a7_1.place(width = 100,height = 100,x = 0,y = 300)
a8_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a8_1.place(width = 100,height = 100,x = 100,y = 300)
a9_1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 85")
a9_1.place(width = 100,height = 100,x = 200,y = 300)

a1 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a1)
a1.place(width = 100,height = 100,x = 0,y = 100)
a2 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a2)
a2.place(width = 100,height = 100,x = 100,y = 100)
a3 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a3)
a3.place(width = 100,height = 100,x = 200,y = 100)

a4 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a4)
a4.place(width = 100,height = 100,x = 0,y = 200)
a5 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a5)
a5.place(width = 100,height = 100,x = 100,y = 200)
a6 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a6)
a6.place(width = 100,height = 100,x = 200,y = 200)

a7 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a7)
a7.place(width = 100,height = 100,x = 0,y = 300)
a8 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a8)
a8.place(width = 100,height = 100,x = 100,y = 300)
a9 = tk.Button(tic_tac_toe,text = "",fg = a,bg = b,font = "verdana 10",command = a9)
a9.place(width = 100,height = 100,x = 200,y = 300)

refresh_button = tk.Button(tic_tac_toe,text = "REFRESH",fg = b,bg = a,font = "verdana 20",command = REF)
refresh_button.place(width = 300,height = 50,x = 0,y = 400)

tic_tac_toe_control()

tic_tac_toe.mainloop()
