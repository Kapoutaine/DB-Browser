import tkinter as tk



class Window:
    def __init__(self, height=720, weight=480):
        self.root = tk.Tk()
        self.root.title("Data Base Browser")

        self.root.geometry(f"{str(height)}x{str(weight)}")

        self.create_frame()

        self.root.mainloop()

    def create_frame(self):
        # Creating the 4 main frames
        self.frame_top = tk.Frame(self.root)
        self.frame_left = tk.Frame(self.root)
        self.frame_right = tk.Frame(self.root)
        self.frame_bottom = tk.Frame(self.root)

        # Placing frames
        self.frame_top.pack(expand=1)
        self.frame_left.pack(expand=1, side="left")
        self.frame_right.pack(expand=1, side="right")
        self.frame_bottom.pack(expand=1)

    def create_label(self):
        # Creating labels
        self.title = tk.Label(self.frame_top, text="Data Base Browser")
        self.title.pack()





if __name__ == "__main__":
    my_window = Window()