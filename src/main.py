import tkinter as tk

root = None

def finish():
	global root
	root.destroy()
	print('Converter closed')
	
def main():
	global root
	root = tk.Tk()
	root.title('Python converter')
	root.protocol('WM_DELETE_WINDOW', finish)
	
	button_convert	= tk.Button(text='Convert')
	button_about	= tk.Button(text='About')
	button_convert.pack()
	button_about.pack()
	
	root.mainloop()



if __name__ == '__main__':
	main()
	
