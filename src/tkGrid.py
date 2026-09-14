import tkinter as tk

class MinesweeperGrid:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")

        self.buttons = {}
        self.grid_size = 10

        self.create_grid()

    def create_grid(self):
        # Generate the 10x10 coordinate layout
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Button styling 
                btn = tk.Button(
                    self.root,
                    font=("Arial", 12, "bold"),
                    bg="#d9d9d9",
                    fg="black",
                    relief="raised",
                )

                # Grid positioning
                btn.grid(row=row, column=col, padx=1, pady=1)

                # Bind mouse clicks
                btn.bind(
                    "<Button-1>",
                    lambda event, r=row, c=col: self.on_left_click(r, c),
                )
                btn.bind(
                    "<Button-2>" if self.root.tk.call("tk", "windowingsystem") == "aqua" else "<Button-3>",
                    lambda event, r=row, c=col: self.on_right_click(r, c),
                )

                # (Debug) Bind Esc key to exit the application for quick testing
                # REMOVE THIS CODE BEFORE SUBMITTING 
                self.root.bind("<Escape>", lambda event: self.root.destroy())

                self.buttons[(row, col)] = btn

        # Configure scaling for resizing the window
        for i in range(self.grid_size):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_left_click(self, row, col):
        # (Debug) Print coordinates of the clicked cell
        # print(f"Left-clicked cell: ({row}, {col})")
        btn = self.buttons[(row, col)]

        # display (row, col) coordinates on the button
        btn.config(text=f"({row}, {col})")

        # Reveal the cell
        btn.config(state="disabled", relief="sunken", bg="#b3b3b3")
        

    def on_right_click(self, row, col):
        # (Debug) Print coordinates of the clicked cell
        # print(f"Right-clicked cell: ({row}, {col})")
        btn = self.buttons[(row, col)]

        # Right click to flag or unflag the cell
        if btn.cget("text") == "Flag":
            btn.config(text="")
        else:
            btn.config(text="Flag", fg="red")

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x500")
    app = MinesweeperGrid(window)
    window.mainloop()
