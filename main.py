import tkinter as tk
from tkinter import scrolledtext
import logging 
import datetime
import scraper
import re

# LOGGER
infoLogger = logging.Logger("Program logger")
logFile = "log.txt"
logFiler = logging.FileHandler(logFile)
infoLogger.addHandler(logFiler)

# output log
def logMessage(message, output=True):
    actualTimeAndDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    infoLogger.info("{0}:{1}".format(actualTimeAndDate, message))
    if output: outputText.insert(tk.END, message + "\n")
    print(message)

# theme color change
def radThemecolor():
    selected = radChosen.get()
    if selected == 1: mainWindow.configure(background="Gray")
    elif selected == 2: mainWindow.configure(background="Black")
    logMessage("Theme changed")

def addressButtonAction():
    multipleTextBox.delete('1.0', tk.END)
    if not re.match(r"^(http:\/\/)", addressInput.get()):
        addressInput.insert("0", "http://")
    multipleTextBox.insert(tk.INSERT, scraper.getSourceCode(addressInput.get()))
    logMessage("Website scrapped")
    parsedOutputBox.delete("1.0", tk.END)
    parsedOutputBox.insert(tk.INSERT, scraper.soup.find_all("li"))
    
    
# WINDOW BUILDING
mainWindow = tk.Tk()
mainWindow.title("WebCRAA")
##mainWindow.resizable(False, False) 
# main areas
upperArea = tk.Frame(mainWindow)
upperArea.pack( side = tk.TOP)
centerArea = tk.Frame(mainWindow)
centerArea.pack( side = tk.TOP)
lowerArea = tk.Frame(mainWindow)
lowerArea.pack( side = tk.BOTTOM)
# upperArea
tk.Label(upperArea, text="Color theme:").pack(anchor=tk.W)
    
radChosen = tk.IntVar()
tk.Radiobutton(upperArea, text="Light", variable=radChosen, value=1, command=radThemecolor).pack(side=tk.LEFT)
tk.Radiobutton(upperArea, text="Dark", variable=radChosen, value=2, command=radThemecolor).pack(side=tk.RIGHT)

# centerArea
# LEFT SIDE
leftFrame = tk.Frame(centerArea, highlightcolor = "Blue")
leftFrame.pack( side = tk.LEFT)

addressInputLabel = tk.Label(leftFrame, text="Input address (URL):")
addressInputLabel.pack(anchor = tk.NW)

addressInput = tk.Entry(leftFrame)
addressInput.pack(anchor = tk.NW)
addressInput.focus()

addressButton = tk.Button(leftFrame, text="Insert address", fg="green", command=addressButtonAction)
#addressButton.bind('<Return>', addressButtonAction)
addressButton.pack(anchor = tk.NW)

outputArea = tk.Frame(leftFrame)
outputArea.pack(anchor = tk.S)
tk.Label(outputArea, text="Output:").pack(anchor = tk.NW)
outputText = tk.Text(outputArea, width=30, height=5, exportselection=0)
outputText.pack(anchor = tk.S)

# CENTER SIDE
centerFrame = tk.Frame(centerArea, highlightcolor = "yellow")
centerFrame.pack( side = tk.LEFT)

parsedOutputBox = tk.scrolledtext.ScrolledText(centerFrame, width=80, height=50, wrap = tk.WORD)
parsedOutputBox.pack()

# RIGHT SIDE
rightFrame = tk.Frame(centerArea, highlightcolor = "yellow")
rightFrame.pack( side = tk.RIGHT)

multipleTextBox = tk.scrolledtext.ScrolledText(rightFrame, width=80, height=50, wrap = tk.WORD)
multipleTextBox.pack()

# lowerArea
copyrightLabel = tk.Label(lowerArea, text="Website Code Read And Analyse - MrN")
copyrightLabel.pack(anchor = tk.NW)

################### 
#  Start of program
logMessage("[START] PROGRAM START", False)
logMessage("Program Started")

multipleTextBox.insert(tk.INSERT, "Insert website address and click the button to get source code here..")

parsedOutputBox.insert(tk.INSERT, scraper.parsed)


###################

mainWindow.mainloop()