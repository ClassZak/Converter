import tkinter as tk
import tkinter.messagebox
from mediamemorymanager import MediaMemoryManager

root = tk.Tk() 

def finish():
	global root
	root.destroy()
	print('Converter closed')

def exit_command():
	response = tkinter.messagebox.askyesno('Exit', 'Are you sure to exit?')
	if response:
		finish()

def create_main_menu(root):
	menu_main = tk.Menu(tearoff = 0)
	menu_edit = tk.Menu(tearoff = 0)
	
	menu_edit.add_command(label = 'Edit')
	menu_edit.add_command(label = 'Exit', command=exit_command)
	
	menu_main.add_cascade(label = 'File', menu = menu_edit)
	
	root.config(menu = menu_main)
	
def main():
	global root
	root.title('Python converter')
	root.protocol('WM_DELETE_WINDOW', finish)
	
	button_convert	= tk.Button(text='Convert')
	button_about	= tk.Button(text='About')
	button_convert.pack()
	button_about.pack()
	
	create_main_menu(root)
	
	root.mainloop()



if __name__ == '__main__':
	main()
	
