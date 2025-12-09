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
	
	root.mainloop()



if __name__ == '__main__':
	main()
	
