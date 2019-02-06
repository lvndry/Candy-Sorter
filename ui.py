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
        self.numberOfCups = self.tkVar()
        self.numberOfCups.trace('w', self.onNumberOfCupsChange)
        self.yellowCup = self.tkVar()
        self.greenCup = self.tkVar()
        self.blueCup = self.tkVar()
        self.brownCup = self.tkVar()
        self.redCup = self.tkVar()
        self.cupsArray = self.cupOptions(self.numberOfCups.get())
        self.cupsLabel = tk.Label(self, text="Number of cups")
        self.cupsEntry = tk.OptionMenu(self, self.numberOfCups, 1, 2, 3, 4, 5)
        self.cupsLabel.pack()
        self.cupsEntry.pack()
        self.yellowLabel = tk.Label(self, text="Yellow")
        self.yellowEntry = tk.OptionMenu(self, self.yellowCup, *self.cupsArray)
        self.yellowLabel.pack()
        self.yellowEntry.pack()
        self.greenLabel = tk.Label(self, text="Green")
        self.greenEntry = tk.OptionMenu(self, self.greenCup, *self.cupsArray)
        self.yellowLabel.pack()
        self.yellowEntry.pack()
        self.blueLabel = tk.Label(self, text="Blue")
        self.blueEntry = tk.OptionMenu(self, self.blueCup, *self.cupsArray)
        self.blueLabel.pack()
        self.blueEntry.pack()
        self.redLabel = tk.Label(self, text="Red")
        self.redEntry = tk.OptionMenu(self, self.redCup, *self.cupsArray)
        self.redLabel.pack()
        self.redEntry.pack()
        self.brownLabel = tk.Label(self, text="Brown")
        self.brownEntry = tk.OptionMenu(self, self.brownCup, *self.cupsArray)
        self.brownLabel.pack()
        self.brownEntry.pack()
        self.button = tk.Button(self, text="Valid", command=self.logger)
        self.button.pack()

    def logger(self):
        print("Number of cups: " + str(self.numberOfCups.get()))
        print("Yellow goes in cup: " + str(self.yellowCup.get()))
        print("Blue goes in cup: " + str(self.blueCup.get()))
        print("Green goes in cup: " + str(self.greenCup.get()))
        print("Red goes in cup: " + str(self.redCup.get()))
        print("Brown goes in cup: " + str(self.brownCup.get()))

    def updateMenu(self, entry):
        menu = entry["menu"]
        menu.delete(0, "end")
        for val in self.cupsArray:
            menu.add_command(label=val, command=lambda value=val: self.numberOfCups.set(value))

    def tkVar(self):
        value = tk.IntVar(self)
        value.set(1)
        return value

    def cupOptions(self, numberMax):
        arr = []
        for i in range(0, numberMax):
            arr.append(i+1)
        print(arr)
        return arr

    def onNumberOfCupsChange(self, name='', index='', mode=''):
        self.cupsArray = self.cupOptions(self.numberOfCups.get())
        self.updateMenu(self.yellowEntry)
        self.updateMenu(self.blueEntry)
        self.updateMenu(self.greenEntry)
        self.updateMenu(self.redEntry)
        self.updateMenu(self.brownEntry)
        return self.cupsArray

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
