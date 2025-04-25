import os
import random
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkFont

def overwrite_file(file_path, method="DoD"):
    size = os.path.getsize(file_path)
    with open(file_path, "r+b") as f:
        if method == "DoD":
            for _ in range(3):
                f.seek(0)
                f.write(os.urandom(size))
        elif method == "Gutmann":
            patterns = [b'\x55', b'\xAA', b'\x92', b'\x49', b'\x24'] * 5
            for p in patterns:
                f.seek(0)
                f.write(p * size)
            for _ in range(4):
                f.seek(0)
                f.write(os.urandom(size))
        elif method == "Schneier":
            for _ in range(7):
                f.seek(0)
                f.write(os.urandom(size))
        else:
            raise ValueError("Algoritmo sconosciuto")
    os.remove(file_path)

def secure_delete(path, method="DoD"):
    if os.path.isfile(path):
        overwrite_file(path, method)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                try:
                    overwrite_file(os.path.join(root, name), method)
                except:
                    pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except:
                    pass
        shutil.rmtree(path)

def browse_path(method):
    path = filedialog.askopenfilename()
    if not path:
        path = filedialog.askdirectory()
    if path:
        confirm = messagebox.askyesno("Conferma", f"Cancellare in modo sicuro:\n{path}?")
        if confirm:
            try:
                secure_delete(path, method)
                messagebox.showinfo("Completato", f"Cancellazione sicura completata con algoritmo {method}.")
            except Exception as e:
                messagebox.showerror("Errore", str(e))

# === INTERFACCIA MODERNA ===
app = tk.Tk()
app.title("DOGERASER")
app.geometry("500x400")
app.configure(bg="#0e0e0e")

# Font futuristico
try:
    ethno = tkFont.Font(family="Ethnocentric", size=48)
except:
    ethno = ("Helvetica", 48, "bold italic")

# Titolo principale
tk.Label(app, text="DOGERASER", font=ethno, fg="#00e0ff", bg="#0e0e0e").pack(pady=(30, 20))

# Pulsanti stile moderno
style_btn = {"width": 30, "height": 2, "font": ("Consolas", 11, "bold")}

tk.Button(app, text="🛡 Metodo DoD 5220.22-M", bg="#1f3b4d", fg="white",
          command=lambda: browse_path("DoD"), **style_btn).pack(pady=6)

tk.Button(app, text="🧠 Metodo Gutmann (35 passaggi)", bg="#512d3d", fg="white",
          command=lambda: browse_path("Gutmann"), **style_btn).pack(pady=6)

tk.Button(app, text="🔒 Metodo Schneier (7 passaggi)", bg="#2f4f4f", fg="white",
          command=lambda: browse_path("Schneier"), **style_btn).pack(pady=6)

# Firma finale in basso
tk.Label(app, text="Powered by Roy Merlo", font=("Arial", 8),
         fg="#444", bg="#0e0e0e").pack(side="bottom", pady=10)

app.mainloop()





