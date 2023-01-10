import tkinter as tk
import csv

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.search_button = tk.Button(self)
        self.search_button["text"] = "Search data"
        self.search_button["command"] = self.search_data
        self.search_button.grid(row=0, column=0)

        self.add_button = tk.Button(self)
        self.add_button["text"] = "Add data"
        self.add_button["command"] = self.add_data
        self.add_button.grid(row=0, column=1)

        self.modify_button = tk.Button(self)
        self.modify_button["text"] = "Modify data"
        self.modify_button["command"] = self.modify_data
        self.modify_button.grid(row=0, column=2)

        self.delete_button = tk.Button(self)
        self.delete_button["text"] = "Delete data"
        self.delete_button["command"] = self.delete_data
        self.delete_button.grid(row=0, column=3)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=3)

    def search_data(self):
        # kod do odczytu danych
        print("search")
        pass

    def add_data(self):
        # kod do dodawania danych
        print("add")
        pass

    def modify_data(self):
        # kod do modyfikowania danych
        print("modify")
        pass

    def delete_data(self):
        # kod do usuwania danych
        print("delete")
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
