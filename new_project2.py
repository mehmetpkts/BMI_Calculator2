import tkinter

window = tkinter.Tk()
window.title("BMI CALCUALTOR")
window.config(padx=30,pady=30)

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are "
    if bmi < 18.5:
        result_string += "weak"
    elif bmi >= 18.5 and bmi < 24.9 :
        result_string += "ideal weight"
    elif bmi >=24.9 and bmi < 29.9:
        result_string += "overweight"
    else:
        result_string += "obesity"
    return result_string



def calculate_BMI():
    weight = weight_input.get()
    height = height_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    elif float(weight) < 0 or float(height) < 0:
        result_label.config(text="Please enter positive value")
    else:
        try:
            BMI = float(weight) / (float(height)/100) ** 2 
            result_string = write_result(BMI)
            result_label.config(text=result_string )
        except:
            result_label.config(text="Enter a valid number")
    
    
#user interface

weight_input_label = tkinter.Label(text="please enter weight")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="please enter height")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate",command=calculate_BMI)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

window.mainloop()

