import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
import sys

class LetterEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Letter Editor")
        self.geometry("800x500")

        self.bind("<Control-s>",   self.save_button_func)

        self.top_bar = ctk.CTkFrame(self)

        self.theme_chooser = ctk.CTkSegmentedButton(self.top_bar, values=["Dark", "Light"], command=lambda value: ctk.set_appearance_mode(value))
        self.theme_chooser.set(ctk.get_appearance_mode())
        self.theme_chooser.pack(side="left", padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.top_bar, text="Save", command=self.save_button_func)
        self.save_button.pack(side="right", padx=5, pady=5)

        self.close_button = ctk.CTkButton(self.top_bar, text="Close", command=self.close_button_func)
        self.close_button.pack(side="right", padx=5, pady=5)

        self.open_button = ctk.CTkButton(self.top_bar, text="Open", command=self.open_button_func)
        self.open_button.pack(side="right", padx=5, pady=5)

        self.file_label = ctk.CTkLabel(self.top_bar)
        self.file_label.pack(padx=5, pady=5)

        self.top_bar.pack(fill="x",padx=10, pady=(10, 0))

        self.textbox = ctk.CTkTextbox(self)
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)

        if len(sys.argv) > 1:
            self.path = Path(sys.argv[1])
            if self.path and self.path.exists():
                self.textbox.insert("0.0", self.path.read_text())
                self.file_label.configure(text=self.path.name)
            else:
                self.path = None
                self.file_label.configure(text="")
        else:
            self.path = None
            self.file_label.configure(text="")

    def open_button_func(self):
        path = filedialog.askopenfilename(filetypes=[("Letter File", "*.txt"), ("All Files", "*.*")])
        if path:
            self.path = Path(path)
            self.textbox.delete("0.0", "end")
            self.textbox.insert("0.0", self.path.read_text())
            self.file_label.configure(text=self.path.name)

    def save_button_func(self, event=None):
        if self.path:
            self.path.write_text(self.textbox.get("0.0", "end"))
        else:
            name = ctk.CTkInputDialog(title="save", text="Enter file name").get_input()
            if name:
                file = filedialog.asksaveasfile(mode="w", initialfile=name, defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
                if file:
                    file.write(self.textbox.get("0.0", "end"))
                    file.close()

    def close_button_func(self):
        self.textbox.delete("0.0", "end")
        self.path = None
        self.file_label.configure(text="")

if __name__ == "__main__":
    editor = LetterEditor()
    editor.mainloop()