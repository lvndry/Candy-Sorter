import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.greetings = tk.Label(self, text="Start using your candy sorter")
       self.greetings.pack()

       self.QUIT = tk.Button(self)
       self.QUIT["text"] = "QUIT"
       self.QUIT["fg"]   = "red"
       self.QUIT["command"] =  self.quit
       self.QUIT.pack({"side": "left"})

       self.startButton = tk.Button(self)
       self.startButton["text"] = "Start",
       self.startButton.pack({ "side": "left" })

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Configure your Candy Sorter")
       label.pack(side="top", fill="both", expand=True)
       initialValue = tk.StringVar(self)
       initialValue.set("one") # initial value
       cupsLabel = tk.Label(self, text="Number of cups")
       cupsEntry = tk.OptionMenu(self, initialValue, "one", "two", "three", "four", "five")
       cupsLabel.pack()
       cupsEntry.pack()
       yellowLabel = tk.Label(self, text="Yellow")
       yellowEntry = tk.Entry(self)
       yellowLabel.pack()
       yellowEntry.pack()
       greenLabel = tk.Label(self, text="Green")
       greenEntry = tk.Entry(self)
       yellowLabel.pack()
       yellowEntry.pack()
       blueLabel = tk.Label(self, text="Blue")
       blueEntry = tk.Entry(self)
       blueLabel.pack()
       blueEntry.pack()
       redLabel = tk.Label(self, text="Red")
       redEntry = tk.Entry(self)
       redLabel.pack()
       redEntry.pack()
       brownLabel = tk.Label(self, text="Brown")
       brownEntry = tk.Entry(self)
       brownLabel.pack()
       brownEntry.pack()

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Welcome", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Configure", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Candy Sorter")
    root.wm_geometry("400x400")
    root.mainloop()
