import tkinter as tk
from tkinter import scrolledtext
import logging 
import datetime
import scraper
import re

class Application(tk.Frame):
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry("1000x800")
        self.mainWindow.title("WebSCRAA")

        self.logger_init()

        tk.Frame.__init__(self, self.mainWindow)
        

    def logger_init(self):
        # LOGGER
        self.infoLogger = logging.Logger("Program logger")
        logFile = "log.txt"
        logFiler = logging.FileHandler(logFile)
        self.infoLogger.addHandler(logFiler)

        # output log
    def logMessage(self, message, output=True):
        actualTimeAndDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.infoLogger.info("{0}:{1}".format(actualTimeAndDate, message))
        if output: self.outputText.insert(tk.END, message + "\n")
        print(message)

    # theme color change
    def radThemecolor(self):
        selected = self.radChosen.get()
        if selected == 1: self.mainWindow.configure(background="Gray")
        elif selected == 2: self.mainWindow.configure(background="Black")
        self.logMessage("Theme changed")

    def addressButtonAction(self):
        self.multipleTextBox.delete('1.0', tk.END)
        if not re.match(r"^(http:\/\/)", self.addressInput.get()):
            self.addressInput.insert("0", "http://")
        self.multipleTextBox.insert(tk.INSERT, scraper.getSourceCode(self.addressInput.get(), "lxml"))
        self.logMessage("Website scrapped")
        self.parsedOutputBox.delete("1.0", tk.END)
        self.parsedOutputBox.insert(tk.INSERT, scraper.soup.find_all("li"))
        
    def createParseApp(self):
        # main areas
        self.upperArea = tk.Frame(self.mainWindow)
        self.upperArea.pack( side = tk.TOP)
        self.centerArea = tk.Frame(self.mainWindow)
        self.centerArea.pack( side = tk.TOP)
        self.lowerArea = tk.Frame(self.mainWindow)
        self.lowerArea.pack( side = tk.BOTTOM)

        # upperArea
        tk.Label(self.upperArea, text="Color theme:").pack(anchor=tk.W)
        self.radChosen = tk.IntVar()
        tk.Radiobutton(self.upperArea, text="Light", variable=self.radChosen, value=1, command=self.radThemecolor).pack(side=tk.LEFT)
        tk.Radiobutton(self.upperArea, text="Dark", variable=self.radChosen, value=2, command=self.radThemecolor).pack(side=tk.RIGHT)

        # centerArea
        # LEFT SIDE
        self.leftFrame = tk.Frame(self.centerArea, highlightcolor = "Blue")
        self.leftFrame.pack( side = tk.LEFT)

        self.addressInputLabel = tk.Label(self.leftFrame, text="Input address (URL):")
        self.addressInputLabel.pack(anchor = tk.NW)

        self.addressInput = tk.Entry(self.leftFrame)
        self.addressInput.pack(anchor = tk.NW)
        self.addressInput.focus()

        self.addressButton = tk.Button(self.leftFrame, text="Insert address", fg="green", command=self.addressButtonAction)
        #addressButton.bind('<Return>', addressButtonAction)
        self.addressButton.pack(anchor = tk.NW)

        self.outputArea = tk.Frame(self.leftFrame)
        self.outputArea.pack(anchor = tk.S)
        tk.Label(self.outputArea, text="Output:").pack(anchor = tk.NW)
        self.outputText = tk.Text(self.outputArea, width=30, height=5, exportselection=0)
        self.outputText.pack(anchor = tk.S)

        # CENTER SIDE
        self.centerFrame = tk.Frame(self.centerArea, highlightcolor = "yellow")
        self.centerFrame.pack( side = tk.LEFT)

        self.parsedOutputBox = tk.scrolledtext.ScrolledText(self.centerFrame, width=80, height=50, wrap = tk.WORD)
        self.parsedOutputBox.pack()

        # RIGHT SIDE
        self.rightFrame = tk.Frame(self.centerArea, highlightcolor = "yellow")
        self.rightFrame.pack( side = tk.RIGHT)

        self.multipleTextBox = tk.scrolledtext.ScrolledText(self.rightFrame, width=80, height=50, wrap = tk.WORD)
        self.multipleTextBox.pack()

        # lowerArea
        self.copyrightLabel = tk.Label(self.lowerArea, text="Website Code Read And Analyse - MrN")
        self.copyrightLabel.pack(anchor = tk.NW)

    def ParserApp(self):
        self.createParseApp()
        self.mainWindow.mainloop()


app = Application()
app.ParserApp()

        
