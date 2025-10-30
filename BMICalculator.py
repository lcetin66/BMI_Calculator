from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=400)

weight_var = IntVar()
height_var = IntVar()

def bmi_calculator():
    global bmi
    try:
        weight = weight_var.get()
        if weight == 0 or "":
            display.config(text="Please enter a value. Example: 80.50",justify="center")
    except TclError:
        display.config(text="Enter your weight as a number only! Example: 80.50",justify="center")
    except ZeroDivisionError, UnboundLocalError:
        display.config(text="Please enter a value. Example: 80.50",justify="center")
    try:
        height = height_var.get()
        if height == 0:
            display.config(text="\nPlease enter a value. Example: 180",justify="center")
    except TclError:
        display.config(text="Enter your height as a number only! Example: 180",justify="center")
    except ZeroDivisionError, UnboundLocalError:
        display.config(text="Please enter a value. Example: 180",justify="center")

    bmi = round((weight / (height ** 2)*10000),2)

    if bmi < 18.5:
        display.config(text="Your BMI: " + str(bmi)+".\nYou are in Underweight Category",justify="center")
    elif 25 < bmi < 29.9:
        display.config(text="Your BMI: " + str(bmi) + ".\nYou are in Overweight Category",justify="center")
    elif 30 < bmi < 34.9:
        display.config(text="Your BMI: " + str(bmi) + ".\nYou are in Obese I Category",justify="center")
    elif 35 < bmi < 39.9:
        display.config(text="Your BMI: " + str(bmi) + ".\nYou are in Obese II Category",justify="center")
    elif 40 < bmi:
        display.config(text="Your BMI: " + str(bmi) + ".\nYou are in Obese III Category",justify="center")
    else:
        display.config(text="Your BMI: " + str(bmi) + ".\nYou are in NORMAL Category",justify="center")


#Weight
weight_label = Label(text='Enter your weight (kg)',font=('Helvetica', 10,'normal'),)
weight_label.place(x=50,y=30)
weight = Entry(window, textvariable=weight_var, border=0.5, width=20)
weight.place(x=50,y=50)

#Height
height_label = Label(text='Enter your height (m)',font=('Helvetica',10,'normal'))
height_label.place(x=50,y=90)
height = Entry(window, textvariable=height_var, border=0.5,width=20)
height.place(x=50,y=110)

#Button
calculate = Button(text='Calculate', width=17, command=bmi_calculator)
calculate.place(x=50,y=150)

#Display
display = Message(width=250)
display.place(x=25,y=200)

window.mainloop()