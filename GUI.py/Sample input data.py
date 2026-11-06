# GUI_Addition:

# 1. Creating Library for GUI Development
from tkinter import *

# 9. Creating logic to make adding of two numbers
def displayData():
    name_text.set(textBox1.get())
    age_text.set(textBox2.get())
    email_text.set(textBox3.get())
    phone_text.set(textBox4.get())
    salary_text.set(textBox5.get())



#  + ", Age: " + textBox2.get() + ", Email: " + textBox3.get() + ", Phone: " + textBox4.get() + ", Salary: " + textBox5.get())


    # sum = int(textBox1.get()) + int(textBox2.get()) # sum = 10 + 20 , sum = 30 (int)
    # my_text.set(sum) # my_text

# 2. To Creating Window
root = Tk()

my_text = StringVar()

# 3. Creating Variables for each Text Box
name_text = StringVar()
age_text = StringVar()
email_text = StringVar()
phone_text = StringVar()
salary_text = StringVar()

# 4. Creating window Title and window size
root.title("Sample Input Data")   # Window Title
root.geometry("600x400") # Window Size H x W

# 5. Creating Label(Text/Font) in the window by using 3 postiions(Grid, Place, pack)
Label(root, text="Enter Your Name:").grid(row=0, column=0)

Label(root, text="Enter Your Age:").grid(row=1, column=0)

Label(root, text="Enter your Email:").grid(row=2, column=0)

Label(root, text="Enter Your Phone Number:").grid(row=3, column=0)

Label(root, text="Enter Your Salary:").grid(row=4, column=0)

# 6. Creating Text Boxes, for entering values
textBox1 = Entry(root)
textBox1.grid(row=0, column=1)

textBox2 = Entry(root)
textBox2.grid(row=1, column=1)

textBox3 = Entry(root)
textBox3.grid(row=2, column=1)

textBox4 = Entry(root)
textBox4.grid(row=3, column=1)

textBox5 = Entry(root)
textBox5.grid(row=4, column=1)

# 7. Displaying result from the addition of two number
# result = Label(root, text="Employee Name :").grid((row=6, column=2)
# textvariable=my_text).grid(row=8, column=5)

Label(root, text="Employee Name :").grid(row=8, column=0)
Label(root, textvariable=name_text, fg="red").grid(row=8, column=1)

Label(root, text="Employee Age :").grid(row=9, column=0)
Label(root, textvariable=age_text, fg="red").grid(row=9, column=1)

Label(root, text="Employee Email :").grid(row=10, column=0)
Label(root, textvariable=email_text, fg="red").grid(row=10, column= 1)

Label(root, text="Employee Phone :").grid(row=11, column=0)
Label(root, textvariable=phone_text, fg="red").grid(row=11, column=1)

Label(root, text="Employee Salary :").grid(row=12, column=0)
Label(root, textvariable=salary_text, fg="red").grid(row=12, column=1)



# 8. Creating a Button to generate the values
Button(root, text="Submit", command=displayData).grid(row=6, column=2)


#3. To Stop the window, and need to view the window
mainloop()