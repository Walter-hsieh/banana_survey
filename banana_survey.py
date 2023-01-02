import tkinter as tk

root = tk.Tk()

# set the title
root.title('Banana interest survey')

# set the root window size 
root.geometry('640x480+300+100') # +300+100 set the position of the window on the screen
root.resizable(False, False)

""" window is ready, let's add some widgets"""
title = tk.Label(
	root,
	text = 'please take the survey',
	font = ('Arial 16 bold'),
	bg = 'blue',
	fg = '#FF0'
	)
title.grid()
title.grid(columnspan=2)


# text-input box
name_label = tk.Label(root, text='What is your name?')
name_label.grid(row=1,column=0)

name_inp = tk.Entry(root)
name_inp.grid(row=1, column=1)

# checkbutton
eater_inp = tk.Checkbutton(
	root,
	text='Check this box if you eat bananas'
	)
eater_inp.grid(row=2, columnspan=2, sticky='we') 

# spinbox for entering numbers
num_label = tk.Label(
	root,
	text='How many bananas do you eat per day?'
	)
num_label.grid(row=3, sticky=tk.W)


num_inp = tk.Spinbox(root,
	from_=0,
	to=1000,
	increment=1
	)
num_inp.grid(row=3, column=1, sticky=(tk.W+ tk.E))

# list box
color_label = tk.Label(
	root,
	text='What is the best color for a banana?'
	)
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)

color_inp = tk.Listbox(
	root,
	height=6
	)

color_choices = (
	'Any', 'Green', 'Green-Yellow',
	'Yellow', 'Brown Spotted', 'Black'
	)

for choice in color_choices:
	color_inp.insert(tk.END, choice)
color_inp.grid(row=5, columnspan=2, sticky=tk.W, padx=25, ipady=2, ipadx=2)


# Radiobutton
plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)

plantain_frame = tk.Frame(root) # Frame object is a blank panel with nothing on it
plantain_frame.grid(row=7, columnspan=2, stick=tk.W)

plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes')
plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)

plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewww, No!')
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)



# text widget for multi-line strings input
banana_haiku_label = tk.Label(
	root,
	text='Write a haiku about bananas')
banana_haiku_label.grid(row=8, sticky=tk.W)

banana_haiku_inp = tk.Text(
	root,
	height=3)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')



# submit 
submit_btn = tk.Button(
	root,
	text='Submit Survey')
submit_btn.grid(row=99, column=0, columnspan=1)

output_line = tk.Label(root, text='', anchor='w', justify='left')
output_line.grid(row=100, columnspan=2, sticky='NSEW')


# clean 
clean_btn =tk.Button(
	root,
	text='Clean Output'
	)
clean_btn.grid(row=99, column=1)



def on_submit():
	"""To be run when user submits the form"""
	name = name_inp.get()
	number = num_inp.get()
	selected_idx = color_inp.curselection() # to get the index of the selected color
	if  selected_idx:
		color = color_inp.get(selected_idx)
	else:
		color = '' # if there is no selection, curselection() will return a empty tuple. In this case, we will just set color to an empty string.
	haiku = banana_haiku_inp.get('1.0', tk.END)

	message = (
		f'Thanks for taking the survey, {name}.\n'
		f'Enjoy your {number} {color} bananas!'
		)
	output_line.configure(text=message)
	print(haiku)


submit_btn.configure(command=on_submit)

"""Can't rest the the whole textbox, when new submission the interpreter print the old input."""
def on_clean():
	banana_haiku_inp = tk.Text(
	root,
	height=3)
	banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')
	haiku = banana_haiku_inp.get('1.0', tk.END)
	output_line.configure(text='textbox is clean')

clean_btn.configure(command=on_clean)



root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)



root.mainloop()






 
