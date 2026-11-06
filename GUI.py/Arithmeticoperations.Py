# GUI_Addition:

# 1. Creating Library for GUI Development
from tkinter import *

# 9. Creating logic to make adding of two numbers
def addNumbers():
    sum = int(textBox1.get()) + int(textBox2.get()) # sum = 10 + 20 , sum = 30 (int)
    my_text.set(sum)


def divNumbers():
    div = int(textBox1.get()) / int(textBox2.get()) # div = 10 / 20 , div = 0.5 (float)
    my_text.set(div)

def subNumbers():
    sub = int(textBox1.get()) - int(textBox2.get()) # sub = 10 - 20 , sub = -10 (int)
    my_text.set(sub)

def mulNumbers():
    mul = int(textBox1.get()) * int(textBox2.get()) # mul = 10 * 20 , mul = 200 (int)
    my_text.set(mul)

def expNumbers():
    exp = int(textBox1.get()) ** int(textBox2.get()) # exp = 10 ** 20 , exp = 100000000000000000000 (int)
    my_text.set(exp)

def modNumbers():
    mod = int(textBox1.get()) % int(textBox2.get()) # mod = 10 % 20 , mod = 10 (int)
    my_text.set(mod)

def floorDivNumbers():
    floorDiv = int(textBox1.get()) // int(textBox2.get()) # floorDiv = 10 // 20 , floorDiv = 0 (int)
    my_text.set(floorDiv)


# Performing other arithmetic operations
    # div = int(textBox1.get()) / int(textBox2.get()) # div = 10 / 20 , div = 0.5 (float)
    # sub = int(textBox1.get()) - int(textBox2.get()) # sub = 10 - 20 , sub = -10 (int)
    # mul = int(textBox1.get()) * int(textBox2.get()) # mul = 10 * 20 , mul = 200 (int)
    # exp = int(textBox1.get()) ** int(textBox2.get()) # exp = 10 ** 20 , exp = 100000000000000000000 (int)
    # mod = int(textBox1.get()) % int(textBox2.get()) # mod = 10 % 20 , mod = 10 (int)
    # floorDiv = int(textBox1.get()) // int(textBox2.get()) # floorDiv = 10 // 20 , floorDiv = 0 (int)


    # a = int(textBox1.get())
    # b = int(textBox2.get()) 


    # Perform other arithmetic operations
         

    # # Update the text variable with the results
    # my_text.set(sum) # my_text
    # my_text.set(div)
    # my_text.set(sub)
    # my_text.set(mul)
    # my_text.set(exp)
    # my_text.set(mod)
    # my_text.set(floorDiv)

# 2. To Creating Window
root = Tk()
my_text = StringVar()

# 4. Creating window Title and window size

# TITLE ANTE EKKADA MANAKI HEADING RAVATANIKI USE ITUNDHI ARITHEMETIC ANTE ALL +-/* OPERATIONS KOSAM USE ITUNDHI

root.title("Arithmetic Operations")   # Window Title
root.geometry("500x200") # Window Size H x W

# 5. Creating Label(Text/Font) in the window by using 3 postiions(Grid, Place, pack)


Label(root, text="Enter Your First Number:").grid(row=0, column=0)
Label(root, text="Enter Your Second Number:").grid(row=1, column=0)
Label(root, text="Result of Arithmetic Operations is:").grid(row=2, column=0)


# Label(root, text="Addition of Two Numbers is:").grid(row=2, column=0)
# Label(root, text="Subtraction of Two Numbers is:").grid(row=3, column=0)
# Label(root, text="Multiplication of Two Numbers is:").grid(row=4, column=0)
# Label(root, text="Division of Two Numbers is:").grid(row=5, column=0)
# Label(root, text="Modulus of Two Numbers is:").grid(row=6, column=0)
# Label(root, text="Exponent of Two Numbers is:").grid(row=7, column=0)
# Label(root, text="Floor Division of Two Numbers is:").grid(row=8, column=0)

# 6. Creating Text Boxes, for entering values
textBox1 = Entry(root)
textBox1.grid(row=0, column=1)

textBox2 = Entry(root)
textBox2.grid(row=1, column=1)

textBox3 = Entry(root)
textBox3.grid(row=2, column=1)

# 7. Displaying result from the addition of two number
result = Label(root, text="", textvariable=my_text).grid(row=2, column=2)

# 8. Creating a Button to generate the values
Button(root, text="Add", command=addNumbers).grid(row=4, column=0)
Button(root, text="Divide", command=divNumbers).grid(row=4,column=1)
Button(root, text="Multiply", command=mulNumbers).grid(row=4,column=2)
Button(root, text="Modulus", command=modNumbers).grid(row=4,column=3)
Button(root, text="Exponent", command=expNumbers).grid(row=5,column=0)
Button(root, text="Floor Division", command=floorDivNumbers).grid(row=5,column=1)
Button(root, text="Subtract", command=subNumbers).grid(row=5,column=2)

#3. To Stop the window, and need to view the window
mainloop()