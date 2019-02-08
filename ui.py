import tkinter as tk
import json

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
        label.grid(row=0, column=1)
        self.numberOfCups = self.getTkInt()
        self.numberOfCups.trace('w', self.onNumberOfCupsChange)
        self.yellowCup = self.getTkInt()
        self.greenCup = self.getTkInt()
        self.blueCup = self.getTkInt()
        self.brownCup = self.getTkInt()
        self.redCup = self.getTkInt()
        self.cupsArray = self.cupOptions(self.numberOfCups.get())
        self.cupsLabel = tk.Label(self, text="Number of cups")
        self.cupsEntry = tk.OptionMenu(self, self.numberOfCups, 1, 2, 3, 4, 5)
        self.cupsLabel.grid(row=1, column=0)
        self.cupsEntry.grid(row=1, column=1)
        self.yellowLabel = tk.Label(self, text="Yellow")
        self.yellowEntry = tk.OptionMenu(self, self.yellowCup, *self.cupsArray)
        self.yellowLabel.grid(row=2, column=0)
        self.yellowEntry.grid(row=2, column=1)
        self.greenLabel = tk.Label(self, text="Green")
        self.greenEntry = tk.OptionMenu(self, self.greenCup, *self.cupsArray)
        self.yellowLabel.grid(row=3, column=0)
        self.yellowEntry.grid(row=3, column=1)
        self.blueLabel = tk.Label(self, text="Blue")
        self.blueEntry = tk.OptionMenu(self, self.blueCup, *self.cupsArray)
        self.blueLabel.grid(row=4, column=0)
        self.blueEntry.grid(row=4, column=1)
        self.redLabel = tk.Label(self, text="Red")
        self.redEntry = tk.OptionMenu(self, self.redCup, *self.cupsArray)
        self.redLabel.grid(row=5, column=0)
        self.redEntry.grid(row=5, column=1)
        self.brownLabel = tk.Label(self, text="Brown")
        self.brownEntry = tk.OptionMenu(self, self.brownCup, *self.cupsArray)
        self.brownLabel.grid(row=6, column=0)
        self.brownEntry.grid(row=6, column=1)
        self.button = tk.Button(self, text="Valid", command=self.logger)
        self.button.grid(row=7, column=1)

    def logger(self):
        config = {
            "numberOfCups": self.numberOfCups.get(),
            "yellow": self.yellowCup.get(),
            "blue": self.blueCup.get(),
            "green": self.greenCup.get(),
            "brown": self.brownCup.get()
        }
        print(config)
        print("Number of cups: " + str(self.numberOfCups.get()))
        print("Yellow goes in cup: " + str(self.yellowCup.get()))
        print("Blue goes in cup: " + str(self.blueCup.get()))
        print("Green goes in cup: " + str(self.greenCup.get()))
        print("Red goes in cup: " + str(self.redCup.get()))
        print("Brown goes in cup: " + str(self.brownCup.get()))

    def updateMenu(self, entry, cups):
        menu = entry["menu"]
        menu.delete(0, "end")
        for val in range(1, self.numberOfCups.get() + 1):
            menu.add_command(label=val, command=lambda value=val: cups.set(value))

    def getTkInt(self):
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
        self.updateMenu(self.yellowEntry, self.yellowCup)
        self.updateMenu(self.blueEntry, self.blueCup)
        self.updateMenu(self.greenEntry, self.greenCup)
        self.updateMenu(self.redEntry, self.redCup)
        self.updateMenu(self.brownEntry, self.brownCup)
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
