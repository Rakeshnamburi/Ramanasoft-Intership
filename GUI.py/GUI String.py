# GUI_Addition:

# 1. Creating Library for GUI Development
from tkinter import *

# 9. Creating logic to make adding of two numbers
def displayFullName():
    fullName = textBox1.get() + " " + textBox2.get() # fullName = "Alice" + "Bob" , fullName = "Alice Bob" (str)
    name_text.set(fullName) # name_text

# 2. To Creating Window
root = Tk()

name_text = StringVar()

# ekkada name_text endhuku sue chesam ante akkada only manam echina text a print avutundhi  and also manam andhuke add name ani echam starting lo 

# 4. Creating window Title and window size
root.title("GUI String")   # Window Title
root.geometry("500x200") # Window Size H x W

# 5. Creating Label(Text/Font) in the window by using 3 postiions(Grid, Place, pack)
Label(root, text="Enter Your First Name:").grid(row=0, column=0)
Label(root, text="Enter Your Second Name:").grid(row=1, column=0)

# 6. Creating Text Boxes, for entering values
textBox1 = Entry(root)
textBox1.grid(row=0, column=1)

textBox2 = Entry(root)
textBox2.grid(row=1, column=1)

# 7. Displaying result from the addition of two number
# result = Label(root, text="", textvariable=my_text).grid(row=2, column=1)




Label(root, text="My Full Name :").grid(row=8, column=0)
Label(root, textvariable=name_text, fg="red").grid(row=8, column=1)


# 8. Creating a Button to generate the values
Button(root, text="Submit", command=displayFullName).grid(row=2, column=2)

#3. To Stop the window, and need to view the window
mainloop()