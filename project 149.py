from tkinter import *
import random

root=Tk()

root.title("Random word generator")
root.geometry("500x500")

label = Label(root)

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(list1)

def random_number():
    random_no1 = random.randint(0, 25)
    random_no2 = random.randint(0, 25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_no5 = random.randint(0, 25)
    
    random_alpha1 = list1[random_no1]
    random_alpha2 = list1[random_no2]
    random_alpha3 = list1[random_no3]
    random_alpha4 = list1[random_no4]
    random_alpha5 = list1[random_no5]
    
    label["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5

btn1 = Button(root)
btn1 = Button(root, text="Generate random words", command = random_number)
btn1.place(relx= 0.5,rely= 0.5,anchor = CENTER)

label.place(relx= 0.5,rely= 0.6,anchor = CENTER)

root.mainloop()