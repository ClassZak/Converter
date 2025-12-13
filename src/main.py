import tkinter as tk

root = None

def finish():
	global root
	root.destroy()
	print('Converter closed')

def create_main_menu(root):
	menu_main = tk.Menu(tearoff = 0)
	menu_edit = tk.Menu(tearoff = 0)
	
	menu_edit.add_command(label = 'Edit')
	
	menu_main.add_cascade(label = 'File', menu = menu_edit)
	
	root.config(menu = menu_main)
	
def main():
	global root
	root = tk.Tk()
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
	
