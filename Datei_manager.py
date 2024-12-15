import os
import tkinter as tk
from tkinter import messagebox, filedialog

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Dateimanager")
        self.root.geometry("600x400")

        # Verzeichnis-Anzeige
        self.dir_label = tk.Label(self.root, text="Aktuelles Verzeichnis: ", width=80, anchor='w')
        self.dir_label.pack(padx=10, pady=10)

        # Listbox für Dateien und Ordner
        self.file_listbox = tk.Listbox(self.root, width=80, height=15)
        self.file_listbox.pack(padx=10, pady=10)
        self.file_listbox.bind('<Double-1>', self.on_file_select)

        # Buttons
        self.create_folder_button = tk.Button(self.root, text="Ordner erstellen", command=self.create_folder)
        self.create_folder_button.pack(side="left", padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Löschen", command=self.delete_item)
        self.delete_button.pack(side="left", padx=10, pady=10)

        self.refresh_button = tk.Button(self.root, text="Aktualisieren", command=self.refresh_directory)
        self.refresh_button.pack(side="left", padx=10, pady=10)

        # Standard-Verzeichnis anzeigen
        self.current_directory = os.getcwd()
        self.update_directory()

    def update_directory(self):
        self.dir_label.config(text=f"Aktuelles Verzeichnis: {self.current_directory}")
        self.refresh_directory()

    def refresh_directory(self):
        self.file_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(self.current_directory):
                self.file_listbox.insert(tk.END, item)
        except PermissionError:
            messagebox.showerror("Fehler", "Sie haben keine Berechtigung, dieses Verzeichnis anzuzeigen.")

    def on_file_select(self, event):
        selected_item = self.file_listbox.get(self.file_listbox.curselection())
        item_path = os.path.join(self.current_directory, selected_item)
        if os.path.isdir(item_path):
            self.current_directory = item_path
            self.update_directory()
        elif os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                content = file.read()
                self.show_file_content(content)

    def show_file_content(self, content):
        content_window = tk.Toplevel(self.root)
        content_window.title("Dateiinhalt")
        text_widget = tk.Text(content_window, width=80, height=20)
        text_widget.pack(padx=10, pady=10)
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)

    def create_folder(self):
        folder_name = filedialog.askstring("Ordner erstellen", "Ordnername eingeben:")
        if folder_name:
            new_folder_path = os.path.join(self.current_directory, folder_name)
            try:
                os.makedirs(new_folder_path)
                self.refresh_directory()
            except FileExistsError:
                messagebox.showerror("Fehler", "Ordner existiert bereits.")
            except Exception as e:
                messagebox.showerror("Fehler", str(e))

    def delete_item(self):
        selected_item = self.file_listbox.get(self.file_listbox.curselection())
        item_path = os.path.join(self.current_directory, selected_item)
        if messagebox.askyesno("Löschen", f"Sind Sie sicher, dass Sie {selected_item} löschen möchten?"):
            try:
                if os.path.isdir(item_path):
                    os.rmdir(item_path)
                else:
                    os.remove(item_path)
                self.refresh_directory()
            except Exception as e:
                messagebox.showerror("Fehler", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    file_manager = FileManager(root)
    root.mainloop()

