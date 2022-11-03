import mysql.connector
import tkinter  as tk 
from tkinter import * 
import time
my_w = tk.Tk()
my_w.geometry("1200x250") 
my_connect = mysql.connector.connect(
  host="sql7.freemysqlhosting.net",
  user="sql7533907", 
  passwd="j5X7P5nQcX",
  database="sql7533907"
)

my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM userss limit 0,10")
i=0 

for student in my_conn: 
    for j in range(len(student)):
        e = Entry(my_w, width=50, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
        print("Успех")       
    i=i+1
my_w.mainloop()   



  
    
