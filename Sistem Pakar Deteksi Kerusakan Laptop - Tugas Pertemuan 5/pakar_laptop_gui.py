import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_laptop.pl")

gejala = []
index_gejala = 0
current_gejala = ""

def mulai_deteksi():
    global gejala, index_gejala
    prolog.retractall("gejala_pos(_)")

    start_btn.config(state=tk.DISABLED)
    yes_btn.config(state=tk.NORMAL)
    no_btn.config(state=tk.NORMAL)

    gejala.clear()
    index_gejala = 0

    for row in prolog.query("pertanyaan(X, _)"):
        gejala.append(row["X"])

    tampilkan_pertanyaan()

def tampilkan_pertanyaan():
    global current_gejala, index_gejala

    if index_gejala >= len(gejala):
        tampilkan_deteksi()
        return

    current_gejala = gejala[index_gejala]
    teks = list(prolog.query(f"pertanyaan({current_gejala}, T)"))[0]["T"].decode()

    kotak_pertanyaan.config(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, teks)
    kotak_pertanyaan.config(state=tk.DISABLED)

def jawab(ya):
    global index_gejala
    if ya:
        prolog.assertz(f"gejala_pos({current_gejala})")
    index_gejala += 1
    tampilkan_pertanyaan()

def tampilkan_deteksi():
    hasil = list(prolog.query("kerusakan(K)"))
    if hasil:
        kerusakan = hasil[0]["K"].decode()
        messagebox.showinfo("Hasil Deteksi", f"Kerusakan terdeteksi: {kerusakan}")
    else:
        messagebox.showinfo("Hasil Deteksi", "Kerusakan tidak teridentifikasi.")

    yes_btn.config(state=tk.DISABLED)
    no_btn.config(state=tk.DISABLED)
    start_btn.config(state=tk.NORMAL)

# GUI
root = tk.Tk()
root.title("Sistem Pakar Deteksi Kerusakan Laptop")

frame = ttk.Frame(root, padding="10")
frame.grid()

ttk.Label(frame, text="Deteksi Kerusakan Laptop", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)

kotak_pertanyaan = tk.Text(frame, width=60, height=4, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=1, columnspan=3, pady=10)

yes_btn = ttk.Button(frame, text="Ya", command=lambda: jawab(True), state=tk.DISABLED)
yes_btn.grid(column=1, row=2, padx=5)

no_btn = ttk.Button(frame, text="Tidak", command=lambda: jawab(False), state=tk.DISABLED)
no_btn.grid(column=2, row=2, padx=5)

start_btn = ttk.Button(frame, text="Mulai Deteksi", command=mulai_deteksi)
start_btn.grid(column=1, row=3, columnspan=2)

root.mainloop()
