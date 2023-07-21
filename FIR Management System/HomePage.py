from tkinter import *
from PIL import ImageTk,Image
import os
import subprocess

#Function
def display_frame(frame) :
	frame.pack_forget()
	frame.pack()

def back() :
	global root
	global add_frame
	global frame,search_frame,delete_frame,modify_frame,add_victim_frame
	global add_case_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame

	for i in (frame,add_frame,search_frame,delete_frame,modify_frame,add_victim_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame):

		i.pack_forget()
	display_frame(frame)

from tkinter import *

from tkinter import *

from tkinter import *

from tkinter import *

from tkinter import *

from PIL import Image, ImageTk

from PIL import Image, ImageTk

from PIL import Image, ImageTk

from tkinter import *

from tkinter import *

def add():
    global frame, root, add_frame

    frame.pack_forget()

    add_frame = Frame(root, background="#6D7993")

    buttons = ['Add FIR Details', 'Go to Main Menu']
    functions = [add_victim, back]

    # Load the left image
    image_left = PhotoImage(file="D:\FIR Management System\signuplogo.png")
    new_width = int(image_left.width() * 1.5)  # Increase the width by 50% (change the factor as needed)
    new_height = int(image_left.height() * 1.5)  # Increase the height by 50% (change the factor as needed)
    image_left = image_left.zoom(2, 2)  # Increase the size of the image (change the factors as needed)
    image_label_left = Label(add_frame, image=image_left, background="#6D7993")
    image_label_left.image = image_left  # Keep a reference to the image object
    image_label_left.pack(side=LEFT, padx=10)

    for i in range(len(buttons)):
        button_frame = Frame(add_frame, background="#6D7993")
        button_frame.pack(side=TOP, pady=30)

        # Create the button and place it in the button_frame
        button = Button(button_frame, text=buttons[i], command=functions[i], height=3, width=30,
                        background="#675682", font=("Century Gothic", 16, "bold"), fg="black")
        button.pack(side=LEFT, padx=10)

    # Load the right image
    #image_right = PhotoImage(file="D:\FIR Management System\images.png")
    #image_label_right = Label(add_frame, image=image_right, background="#6D7993")
    #image_label_right.image = image_right  # Keep a reference to the image object
    #image_label_right.pack(side=RIGHT, padx=10)

    display_frame(add_frame)











from tkinter import *

from tkinter import *

from tkinter import *

from tkinter import *

from tkinter import *

from tkinter import *
from PIL import Image, ImageTk

def search():
    global frame, root, search_frame
    frame.pack_forget()

    search_frame = Frame(root, background="#6D7993")
    button = ['Search FIR Details', 'Go to Main Menu']
    function = [search_victim, back]

    # Load the image
    image = Image.open("D:/FIR Management System/signuplogo.png")  # Replace with the actual image path
    new_size = (image.width * 1, image.height * 1)  # Adjust the scaling factor as needed
    resized_image = image.resize(new_size)
    image_left = ImageTk.PhotoImage(resized_image)

    image_label_left = Label(search_frame, image=image_left, background="#6D7993")
    image_label_left.image = image_left  # Keep a reference to the image
    image_label_left.grid(row=0, column=0, padx=10, pady=10)

    for i in range(len(button)):
        Button(search_frame, text=button[i], command=function[i], height=3, width=30, background="#675682",
               font=("Century Gothic", 16, "bold"), fg="black").grid(row=i, column=1, padx=20, pady=30)

    display_frame(search_frame)








def delete():
    global frame, root, delete_frame
    frame.pack_forget()
    delete_frame = Frame(root, background="#6D7993")
    button = ['Delete FIR Details', 'Go to Main Menu']
    function = [delete_victim, back]

    # Load the left image
    image_left = PhotoImage(file="D:\FIR Management System\signuplogo.png")  # Replace with the actual path to the left image
    image_left = image_left.zoom(2, 2)  # Zoom the image by a factor of 1.5 (change the factors as needed)
    image_label_left = Label(delete_frame, image=image_left, background="#6D7993")
    image_label_left.image = image_left  # Keep a reference to the image
    image_label_left.pack(side=LEFT, padx=10)

    # Create a frame for the buttons
    button_frame = Frame(delete_frame, background="#6D7993")
    button_frame.pack(side=LEFT)

    for i in range(len(button)):
        Button(button_frame, text=button[i], command=function[i], height=5, width=30, background="#675682",
               font=("Century Gothic", 16, "bold"), fg="black").pack(side=TOP, padx=30, pady=10)

    display_frame(delete_frame)




def modify():
    global frame, root, modify_frame
    frame.pack_forget()
    modify_frame = Frame(root, background="#6D7993")
    button = ['DISPLAY BUCKETS']
    function = [modify_victim, back]

    # Load the left image
    image_left = PhotoImage(file="D:\FIR Management System\signuplogo.png")  # Replace with the actual path to the left image
    image_left = image_left.zoom(2, 2)  # Zoom the image by a factor of 1.5 (change the factors as needed)
    image_label_left = Label(modify_frame, image=image_left, background="#6D7993")
    image_label_left.image = image_left  # Keep a reference to the image
    image_label_left.pack(side=LEFT, padx=10)

    for i in range(len(button)):
        Button(modify_frame, text=button[i], command=function[i], height=1, width=20, background="#675682",
               font=("Century Gothic", 16, "bold"), fg="black").pack(side=TOP, padx=20, pady=30)

    display_frame(modify_frame)


#Add Menu
def add_victim() :
	global add_frame,root,add_victim_frame
	global v1,v2,v3,v4,v5,v6,v7,v8
	global lbl1
	add_frame.pack_forget()
	add_victim_frame = Frame(root,background="#6D7993")
	
	image = Image.open("D:\FIR Management System\signuplogo.png")
	resize_image = image.resize((700, 700))
	img = ImageTk.PhotoImage(resize_image)
	label_img = Label(add_victim_frame, image=img, background="#6D7993")
	label_img.image = img
	label_img.pack(side=LEFT, padx=20, pady=20)

	lbl1 = Label(add_victim_frame, text='',background="#675682",font=("Courier New", 16,"bold"),fg="white")
	lbl1.pack(side=BOTTOM, expand=YES ,padx=20, pady=15)

	label1=Label(add_victim_frame,text="Enter the FIR NO.",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label1.pack()
	#label1.place(x=0,y=100)
	v1=Entry(add_victim_frame,font=("Courier New", 18))
	v1.pack()
	#v1.place(x=0,y=120)

	label2=Label(add_victim_frame,text="Enter the VICTIM name",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label2.pack()
	v2=Entry(add_victim_frame,font=("Courier New", 18))
	#label2.place(x=100,y=200)
	v2.pack()
	#v2.place(x=100,y=250)

	label3=Label(add_victim_frame,text="Enter ACCUSED name",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label3.pack()
	#label3.place(x=100,y=300)
	v3=Entry(add_victim_frame,font=("Courier New", 18))
	v3.pack()
	#v3.place(x=100,y=350)

	label4=Label(add_victim_frame,text="Enter the CASE PLACE",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label4.pack()
	#label4.place(x=100,y=400)
	v4=Entry(add_victim_frame,font=("Courier New", 18))
	v4.pack()
	#v4.place(x=100,y=450)

	label5=Label(add_victim_frame,text="Enter the CASE TIME",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label5.pack()
	#label5.place(x=100,y=500)
	v5=Entry(add_victim_frame,font=("Courier New", 18))
	v5.pack()
	#v5.place(x=100,y=550)

	label6=Label(add_victim_frame,text="Enter the CASE DESCRIPTION",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label6.pack()
	#label6.place(x=100,y=600)
	v7=Entry(add_victim_frame,font=("Courier New", 18))
	v7.pack()
	#v7.place(x=100,y=650)

	label7=Label(add_victim_frame,text="Enter the CASE STATUS",background="#675682",font=("Courier New", 18,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label7.pack()
	#label7.place(x=100,y=350)
	v6=Entry(add_victim_frame,font=("Courier New", 18))
	v6.pack()
	#v6.place(x=100,y=230)

	


	#label_img.place(relx=0.5, y=80, anchor=N)
	b1=Button(add_victim_frame,text="Enter",command=gett,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side = LEFT)

	b2=Button(add_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=RIGHT, expand=YES ,padx=20, pady=15)
	#b2.pack(side = RIGHT)
	#label8=Label(add_victim_frame,text="Bucket overflow",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label7.pack()
	#label7.place(x=100,y=350)
	
	#v6.place(x=100,y=230)

	#lbl1 = Label(add_victim_frame, text='',background="#675682",font=("Courier New", 16,"bold"),fg="white")
	#lbl1.pack(side=BOTTOM, expand=YES ,padx=20, pady=15)
	display_frame(add_victim_frame)
	
def gett():
    command = 'python Insert.py ' + v1.get() + " " + v2.get() + " " + v3.get() + " " + v4.get() + " " + v5.get() + " " + v6.get() + " " + v7.get()
    output = os.popen(command).read().strip()
    if "Bucket overflow" in output:
        lbl1.config(text="Bucket overflow")
    else:
        lbl1.config(text="")
    print(command)

#Search
def search_victim() :
	global search_frame,root,search_victim_frame
	global vs1,vs2,vs3,vs4
	global lbl
	search_frame.pack_forget()
	search_victim_frame = Frame(root,background="#6D7993")
	global vs1,vs2,vs3
	
	image_path = "D:\FIR Management System\signuplogo.png"  # Replace with the actual path to the image file
	image = Image.open(image_path)
	resize_image = image.resize((700, 700))  # Adjust the image size as needed
	img = ImageTk.PhotoImage(resize_image)
	label_img = Label(search_victim_frame, image=img, background="#6D7993")
	label_img.image = img
	label_img.pack(side=LEFT, padx=20, pady=20)

	lbl = Label(search_victim_frame, text='',background="#675682",font=("Courier New", 16,"bold"),fg="black")
	lbl.pack(side=TOP, expand=YES ,padx=20, pady=15)


	key=Label(search_victim_frame,text="Enter FIR NO.",background="#675682",font=("Courier New", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key.pack()
	vs3=Entry(search_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	vs3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(search_victim_frame,text="Enter",command=get1,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side=LEFT)

	b2=Button(search_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=RIGHT, expand=YES ,padx=20, pady=15)
	#b2.pack(side = RIGHT)

	
	display_frame(search_victim_frame)


def get1():

	command='python Search.py '+" "+vs3.get()



	output = subprocess.check_output(command, shell=True)

	lbl['text'] = output.strip()


	os.system(command)
	print(command)




#Delete
def delete_victim() :
	#global add_frame
	global delete_frame,root,delete_victim_frame
	global vd1,vd2,vd3
	global lbl1
	delete_frame.pack_forget()
	delete_victim_frame = Frame(root,background="#6D7993")
#	global vs1,vs2,vs3
	global lbl

	image_path = "D:\FIR Management System\signuplogo.png"  # Replace with the actual path to the image file
	image = Image.open(image_path)
	resize_image = image.resize((700, 700))  # Adjust the image size as needed
	img = ImageTk.PhotoImage(resize_image)
	label_img = Label(delete_victim_frame, image=img, background="#6D7993")
	label_img.image = img
	label_img.pack(side=LEFT, padx=20, pady=20)

	lbl1 = Label(delete_victim_frame, text='',background="#675682",font=("Courier New", 16,"bold"),fg="white")
	lbl1.pack(side=TOP, expand=YES ,padx=20, pady=15)



	key=Label(delete_victim_frame,text="Enter FIR NO.",background="#675682",font=("Courier New", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key.pack()
	vd3=Entry(delete_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	vd3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(delete_victim_frame,text="Enter",command=delete1,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side=LEFT)

	b2=Button(delete_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#2.pack(side = RIGHT)
	display_frame(delete_victim_frame)

def delete1():
	command='python Delete.py '+" "+vd3.get()



	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(delete_victim_frame)


def get_modify():
	command='python Modify.py '


	print("modified")
	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(modify_victim_frame)

#Modify
#Modify
def modify_victim():
	global modify_frame,root,modify_victim_frame
	global v1,v2,v3,v4,v5,vs4
	global lbl1

	


	modify_frame.pack_forget()
	modify_victim_frame = Frame(root,background="#6D7993")

	image_path = "D:\FIR Management System\signuplogo.png"  # Replace with the actual path to the image file
	image = Image.open(image_path)
	resize_image = image.resize((290, 290))  # Adjust the image size as needed
	img = ImageTk.PhotoImage(resize_image)
	label_img = Label(modify_victim_frame, image=img, background="#6D7993")
	label_img.image = img
	label_img.pack(side=LEFT, padx=20, pady=20)

	lbl1 = Label(modify_victim_frame, text='',background="#6D7993",font=("Courier New", 18,"bold"),fg="#000080")
	lbl1.pack(side=TOP, expand=YES ,padx=20, pady=5)




	#label3=Label(modify_victim_frame,text="Enter FIR NO.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label3.pack()
	#v3=Entry(modify_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	#v3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	#key1=Label(modify_victim_frame,text="Enter new Status.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key1.pack()
	#vs4=Entry(modify_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	#vs4.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(modify_victim_frame,text="Enter",command=get_modify,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=45)
	#b1.pack(side = LEFT)

	b2=Button(modify_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=45)
	#b2.pack(side = RIGHT)
	display_frame(modify_victim_frame)








#Main Program


root = Tk(className="GUI")

frame = add_frame = search_frame = delete_frame = modify_frame = Frame(root, background="#6D7993")
root.minsize(200, 200)
root.geometry("500x900")
root.title("Crime Files")
root.configure(background='#6D7993')

add_victim_frame = add_case_frame = Frame(root)
search_victim_frame = Frame(root)
delete_victim_frame = Frame(root)
modify_victim_frame = Frame(root)

label_head = Label(frame, text="FIR Portal", width=15, font=("Tahoma", 40, "bold"), fg="black", background='#675682',
                   justify="center")
label_head.pack(side=TOP, expand=YES, padx=20, pady=30)

# Inserting image to the left
left_image = PhotoImage(file="D:\FIR Management System\signuplogo.png")
left_label = Label(frame, image=left_image, background='#6D7993')
left_label.pack(side=LEFT, padx=10, pady=10)

# Inserting image to the right
right_image = PhotoImage(file="D:\FIR Management System\signuplogo.png")
right_label = Label(frame, image=right_image, background='#6D7993')
right_label.pack(side=RIGHT, padx=10, pady=10)

# Creating Main_Menu Frame
button = ['Register FIR', 'Search FIR', 'Delete FIR', 'Display FIR']
function = [add, search, delete, modify]
for i in range(len(button)):
    Button(frame, text=button[i], command=function[i], height=2, width=20, background="#675682",
           font=("Century Gothic", 16, "bold")).pack(side=TOP, expand=YES, padx=20, pady=30)

# Display
display_frame(frame)
root.mainloop()
