from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=400)

weight_var = StringVar()
height_var = StringVar()

def bmi_calculator():
    try:
        weight = float(weight_var.get())
        height = float(height_var.get())

        if height == 0 or weight == 0:
            display.config(text="Please enter non-zero values.", justify="center")
            return

        bmi = round(weight / (height ** 2) * 10000, 2)

        if bmi < 18.5:
            msg = f"Your BMI: {bmi}\nYou are Underweight"
        elif bmi < 25:
            msg = f"Your BMI: {bmi}\nYou are NORMAL"
        elif bmi < 30:
            msg = f"Your BMI: {bmi}\nYou are Overweight"
        elif bmi < 35:
            msg = f"Your BMI: {bmi}\nYou are in Obese I"
        elif bmi < 40:
            msg = f"Your BMI: {bmi}\nYou are in Obese II"
        else:
            msg = f"Your BMI: {bmi}\nYou are in Obese III"

        display.config(text=msg, justify="center")

    except ValueError:
        display.config(text="Enter only numbers!\nExample: 80 (weight), 180 (height)", justify="center")

# Weight
Label(text='Enter your weight (kg)', font=('Helvetica', 10, 'normal')).place(x=50, y=30)
Entry(window, textvariable=weight_var, border=0.5, width=20).place(x=50, y=50)

# Height
Label(text='Enter your height (cm)', font=('Helvetica', 10, 'normal')).place(x=50, y=90)
Entry(window, textvariable=height_var, border=0.5, width=20).place(x=50, y=110)

# Button
Button(text='Calculate', width=17, command=bmi_calculator).place(x=50, y=150)

# Display
display = Message(width=250, justify="center")
display.place(relx=0.5, rely=0.6, anchor="center")

window.mainloop()
