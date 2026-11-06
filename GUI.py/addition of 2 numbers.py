# GUI_Addition:

# 1. Creating Library for GUI Development
from tkinter import *

# 9. Creating logic to make adding of two numbers
def addNumbers():
    sum = int(textBox1.get()) + int(textBox2.get()) # sum = 10 + 20 , sum = 30 (int)
    my_text.set(sum) # my_text

# 2. To Creating Window
root = Tk()

my_text = StringVar()

# 4. Creating window Title and window size
root.title("Addition of Two Numbers")   # Window Title
root.geometry("500x200") # Window Size H x W

# 5. Creating Label(Text/Font) in the window by using 3 postiions(Grid, Place, pack)
Label(root, text="Enter Your First Number:").grid(row=0, column=0)
Label(root, text="Enter Your Second Number:").grid(row=1, column=0)
Label(root, text="Addition of Two Numbers is:").grid(row=2, column=0)

# 6. Creating Text Boxes, for entering values
textBox1 = Entry(root)
textBox1.grid(row=0, column=1)

textBox2 = Entry(root)
textBox2.grid(row=1, column=1)

# 7. Displaying result from the addition of two number
result = Label(root, text="", textvariable=my_text).grid(row=2, column=1)

# 8. Creating a Button to generate the values
Button(root, text="Submit", command=addNumbers).grid(row=2, column=2)

#3. To Stop the window, and need to view the window
mainloop()