import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from pathlib import Path

class Sortify:
    def __init__(self, root):
        self.root = root
        self.root.title("Sortify - Smart File Organizer")
        self.root.geometry("550x450")
        self.root.configure(bg="#F8FAFC")
        self.root.resizable(False, False)

        # --- State ---
        self.target_dir = tk.StringVar(value="No folder selected")
        self.organize_type = tk.IntVar(value=0)

        # Map folders to extensions (can be loaded from files as per your logic)
        self.extension_map = {
            "images_": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
            "videos_": [".mp4", ".mkv", ".mov", ".avi"],
            "documents_": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "audios_": [".mp3", ".wav", ".flac", ".m4a"],
            "apps_": [".exe", ".msi", ".apk", ".bat"]
        }

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#F8FAFC")
        header.pack(fill="x", pady=(30, 20))
        tk.Label(header, text="Sortify", font=("Helvetica", 24, "bold"), bg="#F8FAFC", fg="#1E293B").pack()
        tk.Label(header, text="Organize your workspace instantly", font=("Helvetica", 11), bg="#F8FAFC", fg="#64748B").pack()

        # Card
        card = tk.Frame(self.root, bg="#FFFFFF", bd=1, relief="solid", padx=20, pady=20)
        card.pack(fill="x", padx=40)

        # Path Selection
        path_frame = tk.Frame(card, bg="#FFFFFF")
        path_frame.pack(fill="x", pady=(0, 10))
        self.path_lbl = tk.Label(path_frame, textvariable=self.target_dir, font=("Helvetica", 10), bg="#FFFFFF", fg="#64748B", wraplength=280)
        self.path_lbl.pack(side="left")
        
        tk.Button(card, text="Select Folder", font=("Helvetica", 10, "bold"), bg="#F1F5F9", relief="flat", command=self.open_folder).pack(fill="x")

        # Options
        opts_frame = tk.Frame(self.root, bg="#F8FAFC", pady=20)
        opts_frame.pack(fill="x", padx=40)
        style = ttk.Style()
        style.configure("TRadiobutton", background="#F8FAFC", font=("Helvetica", 13))
        ttk.Radiobutton(opts_frame, text="Organize by File Type", variable=self.organize_type, value=1).pack(anchor="w")
        ttk.Radiobutton(opts_frame, text="Organize by Keyword", variable=self.organize_type, value=2).pack(anchor="w")

        # Execute
        tk.Button(self.root, text="Start Organizing", font=("Helvetica", 12, "bold"), bg="#3B82F6", fg="white", relief="flat", height=2, command=self.run_logic).pack(fill="x", padx=40, pady=10)

    def open_folder(self):
        selected = filedialog.askdirectory()
        if selected:
            self.target_dir.set(selected)
            self.path_lbl.config(fg="#10B981")

    def run_logic(self):
        loc = self.target_dir.get()
        if loc == "No folder selected":
            messagebox.showerror("Error", "Please select a directory!")
            return

        mode = self.organize_type.get()
        if mode == 1:
            self.sort_by_type(loc)
        elif mode == 2:
            self.open_keyword_modal(loc)
        else:
            messagebox.showwarning("Selection", "Choose an organization method.")

    # --- Backend Logic Integrated ---

    def sort_by_type(self, loc):
        """Logic for sort1: Grouping by extension."""
        try:
            files = [f for f in os.listdir(loc) if os.path.isfile(os.path.join(loc, f))]
            moved_count = 0

            for f in files:
                ext = Path(f).suffix.lower()
                dest_folder = "extras_"
                
                for folder, extensions in self.extension_map.items():
                    if ext in extensions:
                        dest_folder = folder
                        break
                
                # Create folder and move
                target_path = Path(loc) / dest_folder
                target_path.mkdir(exist_ok=True)
                shutil.move(Path(loc) / f, target_path / f)
                moved_count += 1

            messagebox.showinfo("Success", f"Organized {moved_count} files into categories!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not organize: {e}")

    def open_keyword_modal(self, loc):
        """Logic for sort2: Keyword pattern."""
        win = tk.Toplevel(self.root)
        win.title("Keyword Settings")
        win.geometry("300x300")
        win.grab_set()

        tk.Label(win, text="Keyword Pattern", font=("Helvetica", 12, "bold")).pack(pady=10)
        word_var = tk.StringVar()
        tk.Entry(win, textvariable=word_var, font=("Helvetica", 12)).pack(pady=5, padx=20)

        logic_var = tk.IntVar(value=3)
        tk.Radiobutton(win, text="Starts with", variable=logic_var, value=1).pack(anchor="w", padx=50)
        tk.Radiobutton(win, text="Ends with", variable=logic_var, value=2).pack(anchor="w", padx=50)
        tk.Radiobutton(win, text="Contains", variable=logic_var, value=3).pack(anchor="w", padx=50)

        def execute():
            keyword = word_var.get().strip()
            if not keyword: return
            
            all_files = [f for f in os.listdir(loc) if os.path.isfile(os.path.join(loc, f))]
            
            if logic_var.get() == 1:
                matches = [f for f in all_files if f.lower().startswith(keyword.lower())]
            elif logic_var.get() == 2:
                matches = [f for f in all_files if Path(f).stem.lower().endswith(keyword.lower())]
            else:
                matches = [f for f in all_files if keyword.lower() in f.lower()]

            if matches:
                dest = Path(loc) / keyword
                dest.mkdir(exist_ok=True)
                for f in matches:
                    shutil.move(Path(loc) / f, dest / f)
                messagebox.showinfo("Done", f"Moved {len(matches)} files to folder '{keyword}'")
            else:
                messagebox.showwarning("No Match", "No files matched that keyword.")
            win.destroy()

        tk.Button(win, text="Run", bg="#10B981", fg="white", command=execute).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = Sortify(root)
    root.mainloop()