# GUI_Addition:

# 1. Creating Library for GUI Development
from tkinter import *

# 9. Creating logic to make adding of two numbers
def calculateInterest():
    principal = float(textBox1.get())
    rate = float(textBox2.get())
    time = float(textBox3.get())
    interest = (principal * rate * time) / 100
    my_text.set(interest)


# 2. To Creating Window
root = Tk()

my_text = StringVar()

# 4. Creating window Title and window size
root.title("Simple Interest")   # Window Title
root.geometry("500x200") # Window Size H x W

# 5. Creating Label(Text/Font) in the window by using 3 postiions(Grid, Place, pack)
Label(root, text="Enter The Principal ammount:").grid(row=0, column=0)
Label(root, text="Enter The Intrest rate:").grid(row=1, column=0)
Label(root, text="Enter The Time Period:").grid(row=2, column=0)

# 6. Creating Text Boxes, for entering values
textBox1 = Entry(root)
textBox1.grid(row=0, column=1)

textBox2 = Entry(root)
textBox2.grid(row=1, column=1)

textBox3 = Entry(root)
textBox3.grid(row=2, column=1)

# 7. Displaying result from the addition of two number
# result = Label(root, text="My Interest Amount(Every Month) is: ", textvariable=my_text).grid(row=2, column=1)



Label(root, text="My Interest Amount(Every Month) is:").grid(row=8, column=0)
Label(root, textvariable=my_text, fg="black").grid(row=8, column=1)



# 8. Creating a Button to generate the values
Button(root, text="Submit", command=calculateInterest).grid(row=2, column=2)

#3. To Stop the window, and need to view the window
mainloop()