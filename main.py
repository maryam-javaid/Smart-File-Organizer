import os
import shutil
import tkinter as tk
from tkinter import filedialog

# ---------------- FUNCTIONS ---------------- #

def select_folder():

    folder = filedialog.askdirectory()

    if folder:
        folder_path.set(folder)

        status_label.config(
            text="Folder Selected Successfully",
            fg="#00ff99"
        )


def organize_files():

    folder = folder_path.get()

    if folder == "":

        status_label.config(
            text="Please Select a Folder First",
            fg="red"
        )

        return

    categories = {
        "Images": [".png", ".jpg", ".jpeg"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Code": [".py", ".cpp", ".java"]
    }

    moved_files = 0

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for category, extensions in categories.items():

            if extension in extensions:

                category_folder = os.path.join(folder, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                moved = True
                moved_files += 1
                break

        # Others folder
        if not moved:

            other_folder = os.path.join(folder, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            moved_files += 1

    status_label.config(
        text=f"{moved_files} Files Organized Successfully!\nCheck your selected folder — it has been updated automatically.",
        fg="#00ff99"
    )


# ---------------- GUI ---------------- #

window = tk.Tk()

window.title("Smart File Organizer")

window.geometry("700x450")

window.config(bg="#121212")

window.resizable(False, False)

folder_path = tk.StringVar()

# ---------------- TITLE ---------------- #

title = tk.Label(
    window,
    text="Smart File Organizer",
    font=("Helvetica", 24, "bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=25)

# ---------------- SUBTITLE ---------------- #

subtitle = tk.Label(
    window,
    text="Automatically organize your messy folders",
    font=("Helvetica", 12),
    bg="#121212",
    fg="#bbbbbb"
)

subtitle.pack()

# ---------------- PATH LABEL ---------------- #

path_label = tk.Label(
    window,
    text="Selected Folder",
    font=("Helvetica", 12, "bold"),
    bg="#121212",
    fg="white"
)

path_label.pack(pady=(30, 5))

# ---------------- PATH BOX ---------------- #

path_box = tk.Entry(
    window,
    textvariable=folder_path,
    width=65,
    font=("Helvetica", 11),
    bd=0,
    bg="#1f1f1f",
    fg="white",
    insertbackground="white"
)

path_box.pack(ipady=10)

# ---------------- BUTTON FRAME ---------------- #

button_frame = tk.Frame(
    window,
    bg="#121212"
)

button_frame.pack(pady=30)

# ---------------- SELECT BUTTON ---------------- #

select_button = tk.Button(
    button_frame,
    text="Browse Folder",
    font=("Helvetica", 12, "bold"),
    bg="#00b894",
    fg="white",
    padx=20,
    pady=12,
    bd=0,
    cursor="hand2",
    command=select_folder
)

select_button.grid(row=0, column=0, padx=15)

# ---------------- ORGANIZE BUTTON ---------------- #

organize_button = tk.Button(
    button_frame,
    text="Organize Files",
    font=("Helvetica", 12, "bold"),
    bg="#0984e3",
    fg="white",
    padx=20,
    pady=12,
    bd=0,
    cursor="hand2",
    command=organize_files
)

organize_button.grid(row=0, column=1, padx=15)

# ---------------- STATUS BOX ---------------- #

status_label = tk.Label(
    window,
    text="No Folder Selected",
    font=("Helvetica", 12),
    bg="#1f1f1f",
    fg="yellow",
    width=60,
    height=4,
    wraplength=500,
    justify="center"
)

status_label.pack(pady=20)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    window,
    text="Built with Python & Tkinter",
    font=("Helvetica", 10),
    bg="#121212",
    fg="#777777"
)

footer.pack(side="bottom", pady=15)

window.mainloop()