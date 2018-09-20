import tkinter as tk
import pymysql

LARGE_FONT= ("Verdana", 12)

class  School(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		frame = registration(container, self)

		self.frames[registration] = frame

		frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(registration)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

        
class registration(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Boresha High School System", font=LARGE_FONT). grid (padx=10, pady= 10)
		button1 = tk.Button(self, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),text="exit",bg="powder blue", command=lambda: btnclick(7)).grid(row=1, column=0)


		


app = School()
app.title("Boresha")

app.mainloop()


        