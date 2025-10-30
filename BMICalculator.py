from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=400)

weight_var = DoubleVar()
height_var = DoubleVar()

def bmi_calculator():
    try:
        weight = weight_var.get()
        height = height_var.get()

        if weight <= 0 or height <= 0:
            display.config(text="Please enter valid positive values!")
            bmi_value_label.config(text="")
            return

        bmi = round(weight / (height ** 2) * 10000, 2)

        # kategoriye göre renk ve mesaj
        if bmi < 18.5:
            color = "#A7C7E7"
            msg = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            color = "#A9D18E"
            msg = "Normal"
        elif 25 <= bmi <= 29.9:
            color = "#F4B183"
            msg = "Overweight"
        elif 30 <= bmi <= 34.9:
            color = "#E67E22"
            msg = "Obese I"
        elif 35 <= bmi <= 39.9:
            color = "#D35400"
            msg = "Obese II"
        else:
            color = "#B03A2E"
            msg = "Obese III"

        bmi_value_label.config(text=str(bmi), fg=color, font=("Helvetica", 20, "bold"))
        display.config(text=f"You are in {msg} category", fg=color)

    except TclError:
        display.config(text="Please enter numeric values!", fg="red")

# Weight
Label(text='Enter your weight (kg)', font=('Helvetica', 10)).place(x=50, y=30)
Entry(window, textvariable=weight_var, border=0.5, width=20).place(x=50, y=50)

# Height
Label(text='Enter your height (cm)', font=('Helvetica', 10)).place(x=50, y=90)
Entry(window, textvariable=height_var, border=0.5, width=20).place(x=50, y=110)

# Button
Button(text='Calculate', width=17, command=bmi_calculator).place(x=50, y=150)

# BMI display
bmi_value_label = Label(window, text="", font=("Helvetica", 20, "bold"))
bmi_value_label.place(x=120, y=190)

display = Label(window, text="", width=30, justify="center", wraplength=250)
display.place(x=25, y=250)

window.mainloop()
