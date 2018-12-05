import tkinter as tk

class applicationWithGridManagement (tk.Frame):
    def __init__(self):
        print("Application start")
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("App with window management")
        self.root.config(background="gray")

        self.createApp()

    def createApp(self):
        self.header = tk.LabelFrame(self.root, text="Header")
        self.header.pack(fill=tk.BOTH, expand=tk.YES)
        self.mainArea = tk.LabelFrame(self.root, text="Main area")
        self.mainArea.pack(fill=tk.BOTH, expand=tk.YES)
        self.footnote = tk.LabelFrame(self.root, text="Footnote")
        self.footnote.pack(fill=tk.BOTH, expand=tk.YES)

        # HEADER AREA
        tk.Label(self.header, text="Application with grid management").pack(fill=tk.BOTH, expand=tk.YES)
        
        # CONTENT AREA
        self.frame1 = tk.LabelFrame(self.mainArea, background="yellow", text="Entries area")
        self.frame1.grid(column=0, row=1, sticky=tk.W)
        self.frame2 = tk.LabelFrame(self.mainArea, background="red", text="Content")
        self.frame2.grid(column=1, row=1)
        self.frame3 = tk.LabelFrame(self.mainArea, background="lime", text="Info area")
        self.frame3.grid(column=2, row=1, sticky=tk.E)

        tk.Label(self.frame2, text="Once there was a label..").grid(column=0, row=1, padx=10, pady=10)
        tk.Label(self.frame2, text="...and it wasn't alone.").grid(column=2, row=3, sticky=tk.E, padx=10, pady=10)
        tk.Label(self.frame2, text="And the Label no3 came out!").grid(column=1, row=2, padx=10, pady=10)
        tk.Label(self.frame1, text="Label in frame1").grid(column=0, row=0)
        tk.Label(self.frame3, text="Label in frame3").grid(column=0, row=0)

        # FOOTNOTE AREA
        tk.Label(self.footnote, text="Created by Mrn, part of Kira Dev, 2018").pack()

        print("App gridsize: ", self.root.grid_size())

    def getWindowSizeInColumns(self):
        return self.root.size()[0]    

    def startApp(self):
        self.root.mainloop()

app = applicationWithGridManagement()
app.startApp()