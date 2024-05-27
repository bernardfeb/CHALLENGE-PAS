import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

names = ["ZONK🗑️🗑️🗑️", "IPHONE 15 PRO MAX📱📱📱", "HP SAMSUNG S24 ULTRA📱📱📱", "LAMBORGHINI🚗🚗🚗", "AIR PUTIH💧💧💧", "SENDAL MAMA🩴🩴🩴", "SAPU TERBANG🧹🧹🧹"]

def name(): 
    random_name = random.choice(names)
    name_var.set(random_name)
    slmt_var.set("Selamat!")

def show_main_page():
    registration_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

app = ttk.Window(themename="cyborg")
app.title("GACHA BERHADIAH")
app.geometry("700x450")

# Frame untuk halaman registrasi
registration_frame = ttk.Frame(app)
registration_frame.pack(fill='both', expand=True)

# Konten halaman registrasi
ttk.Label(registration_frame, text="Registrasi", font=("Helvetica", 16)).pack(pady=20)
ttk.Label(registration_frame, text="Nama:", font=("Helvetica", 14)).pack(pady=5)
name_entry = ttk.Entry(registration_frame, font=("Helvetica", 14))
name_entry.pack(pady=5)
ttk.Label(registration_frame, text="Email:", font=("Helvetica", 14)).pack(pady=5)
email_entry = ttk.Entry(registration_frame, font=("Helvetica", 14))
email_entry.pack(pady=5)

# Tombol untuk berpindah ke halaman utama
register_button = ttk.Button(registration_frame, text="Daftar", bootstyle="success", command=show_main_page)
register_button.pack(pady=20)

# Frame untuk halaman utama
main_frame = ttk.Frame(app)

# Variabel dan label untuk halaman utama
name_var = ttk.StringVar(value="")
slmt_var = ttk.StringVar(value="")

name_label = ttk.Label(main_frame, textvariable=name_var, font=('Helvetica', 16), bootstyle="primary")
name_label.pack(pady=20)

slmt_label = ttk.Label(main_frame, textvariable=slmt_var, font=('Helvetica', 16), bootstyle="success")
slmt_label.pack(pady=20)

random_name_button = ttk.Button(main_frame, text="KLIK DISINI!!!", bootstyle="info", command=name)
random_name_button.pack(pady=20)

info_label1 = ttk.Label(main_frame, text="CLAIM HADIAH MU DI = xxx.gachahadiah.com", font=("Helvetica", 16))
info_label1.pack(pady=20)

info_label2 = ttk.Label(main_frame, text="HUBUNGI NOMOR 0829118867 JIKA ADA KENDALA", font=("Helvetica", 16))
info_label2.pack(pady=20)

app.mainloop()