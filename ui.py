import tkinter as tk

class Factory():
    def buildLabel(self, text, side="left"):
        label = tk.Label(self, text)
        label.pack(side, fill="both", expand=True)

    def buldOptionMenu(self, initalValue, *args):
        init = initalValue
        optionMenu = tk.OptionMenu(self, init, *args)
        optionMenu.pack()

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
        self.numberOfCups = self.tkVar()
        self.yellowCup = self.tkVar()
        self.greenCup = self.tkVar()
        self.blueCup = self.tkVar()
        self.brownCup = self.tkVar()
        self.redCup = self.tkVar()
        cupsLabel = tk.Label(self, text="Number of cups")
        cupsEntry = tk.OptionMenu(self, self.numberOfCups, 1, 2, 3, 4, 5)
        cupsLabel.pack()
        cupsEntry.pack()
        yellowLabel = tk.Label(self, text="Yellow")
        yellowEntry = tk.OptionMenu(self, self.yellowCup, 1, 2, 3, 4, 5)
        yellowLabel.pack()
        yellowEntry.pack()
        greenLabel = tk.Label(self, text="Green")
        greenEntry = tk.OptionMenu(self, self.greenCup, 1, 2, 3, 4, 5)
        yellowLabel.pack()
        yellowEntry.pack()
        blueLabel = tk.Label(self, text="Blue")
        blueEntry = tk.OptionMenu(self, self.blueCup, 1, 2, 3, 4, 5)
        blueLabel.pack()
        blueEntry.pack()
        redLabel = tk.Label(self, text="Red")
        redEntry = tk.OptionMenu(self, self.redCup, 1, 2, 3, 4, 5)
        redLabel.pack()
        redEntry.pack()
        brownLabel = tk.Label(self, text="Brown")
        brownEntry = tk.OptionMenu(self, self.brownCup, 1, 2, 3, 4, 5)
        brownLabel.pack()
        brownEntry.pack()
        button = tk.Button(self, text="Valid", command=self.logger)
        button.pack()

    def logger(self):
        print("Number of cups: " + str(self.numberOfCups.get()))
        print("Yellow goes in cup: " + str(self.yellowCup.get()))
        print("Blue goes in cup: " + str(self.blueCup.get()))
        print("Green goes in cup: " + str(self.greenCup.get()))
        print("Red goes in cup: " + str(self.greenCup.get()))
        print("Brown goes in cup: " + str(self.brownCup.get()))

    def tkVar(self):
        value = tk.IntVar(self)
        value.set(1)
        return value

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
