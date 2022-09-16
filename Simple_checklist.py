import tkinter
from tkinter  import RIGHT,END,DISABLED,NORMAL,ANCHOR
from tkinter import StringVar,ttk

#Define root window
root =tkinter.Tk()
root.title('My To-do List')
root.iconbitmap('Simple Checklist\pad.ico')
root.geometry('400x400')
root.resizable(0,0)


my_font=('Times New Roman',12)
root_colour='lightblue'
button_colour="#e2cff4"






def add_item():
    word='ALLAH'
    if list_entry.get()== word :
        my_listbox.insert(0,"ALLAH IS THE GREATEST!")
    else:
        my_listbox.insert(0,list_entry.get())
    list_entry.delete(0,END)


def remove_item():
    my_listbox.delete(ANCHOR)


def clear_list():
    my_listbox.delete(0,END)


def save_item():
    with open('Simple_checklist.txt','w') as f:
      list_tuple=my_listbox.get(0,END)
      print(list_tuple)
      for item in list_tuple:
          if item.endswith('\n'):
              f.write(item)
          else:
            f.write(item +'\n')


def open_list():
    try:
        with open('Simple_checklist.txt','r') as f:
            for line in f:
                my_listbox.insert(END,line)
    except:
        return

input_frame=tkinter.Frame(root,bg=root_colour)
output_frame=tkinter.Frame(root,bg=root_colour)
button_frame=tkinter.Frame(root,bg=root_colour)

input_frame.pack()
output_frame.pack()
button_frame.pack()

list_entry=tkinter.Entry(input_frame,font=my_font,width=35,borderwidth=3)
list_add_button=tkinter.Button(input_frame,font=my_font,text='Add Item',borderwidth=2,bg=button_colour,command=add_item)

list_entry.grid(row=0 ,column=0,padx=5,pady=5)
list_add_button.grid(row=0 ,column=1,padx=5,pady=5,ipadx=5)

my_scrollbar=tkinter.Scrollbar(output_frame)
my_listbox=tkinter.Listbox(output_frame,font=my_font,height=15,borderwidth=3,width=45,yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1,sticky='NS')

list_remove_button=tkinter.Button(button_frame,text='Remove Item',font=my_font,bg=button_colour,command=remove_item)
list_clear_button=tkinter.Button(button_frame,text='Clear List',font=my_font,bg=button_colour,command=clear_list)
save_button=tkinter.Button(button_frame,text='Save Item',font=my_font,bg=button_colour,command=save_item)
quit_button=tkinter.Button(button_frame,text='Quit',font=my_font,bg=button_colour,command=root.destroy)


list_remove_button.grid(row=0,column=0,padx=2,pady=10)
list_clear_button.grid(row=0,column=1,padx=2,pady=10,ipadx=10)
save_button.grid(row=0,column=2,padx=2,pady=10,ipadx=10)
quit_button.grid(row=0,column=3,padx=2,pady=10,ipadx=15)


open_list()

root.mainloop()