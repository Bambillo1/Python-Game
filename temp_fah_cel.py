from tkinter import *

def convert_temperature():
	temp = float(entry.get())
	temp = 9/5 * temp+32
	output_label.configure(text = ' Converted to Fahrenheit: {:.1f} ' .format(temp))

main_window = Tk()
main_window.title("www.EasyCodeBook.com")
message_label = Label(text= ' Enter a temperature in Celsius ' ,
font=( ' Verdana ' , 12))
output_label = Label(font=( ' Verdana ' , 12))
entry = Entry(font=( ' Verdana ' , 12), width=4)
calc_button = Button(text= ' Convert C to F ' , font=( ' Verdana ' , 12),
command=convert_temperature)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)


mainloop()
