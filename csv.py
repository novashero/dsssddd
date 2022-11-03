from imp import reload
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Codemy.com - Learn To Code!')

root.geometry("500x650")

# Read only r  
# Read and Write r+  (beginning of file)
# Write Only w   (over-written)
# Write and Read w+  (over written)
# Append Only a  (end of file)
# Append and Read a+  (end of file)



def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("Text Files", "*.csv"), ))
	name = text_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".csv", "")

	
	text_file = open(text_file, 'r')
	stuff = text_file.read()
	print(text_file)
	my_text.insert(END, stuff)
	text_file.close()
	root.title(f'{name} - Textpad')



def open_text():
	text_file = 'D:/Users/Sema/Desktop/Новая папка/facecontrol/Attendance.csv'
	name = text_file
	name = name.replace("C:/gui/", "")
	name = name.replace(".csv", "")
	
	
	text_file = open('D:/Users/Sema/Desktop/Новая папка/facecontrol/Attendance.csv', 'r')
	stuff = text_file.read()
	print(text_file)
	my_text.insert(END, stuff)
	text_file.close()

	root.title(f'{name} - Textpad')
	






my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=50, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

open_text()
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)




root.mainloop()