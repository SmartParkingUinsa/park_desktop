import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from database import *

def hitung_rekomendasi():
    hari_input = chosen_day.get()
    jam_input = float(chosen_hour.get())
    jenis_kendaraan_input = chosen_type.get()

    filtered_data = df[(df['hari'] == hari_input) & (df['jam'] == jam_input) & (df['jenis'] == jenis_kendaraan_input)]
    rata_rata = filtered_data.groupby(['area'])['jumlah'].mean()
    hasil_rata_rata = rata_rata.apply(tambahkan_label)

    hasil_label.config(text=f"Hasil pada hari {hari_input} jam {jam_input}:")
    hasil_text.config(state=tk.NORMAL)
    hasil_text.delete(1.0, tk.END)
    hasil_text.insert(tk.END, hasil_rata_rata.to_string())
    hasil_text.config(state=tk.DISABLED)

    parkiran_sepi = rekomendasi_parkiran_sepi(hasil_rata_rata)
    rekomendasi_label.config(text="Rekomendasi parkiran dengan label Sepi:")
    rekomendasi_text.config(state=tk.NORMAL)
    rekomendasi_text.delete(1.0, tk.END)
    rekomendasi_text.insert(tk.END, "\n".join(parkiran_sepi))
    rekomendasi_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Rekomendasi Parkiran")
root.geometry("400x550")

style = Style(theme="journal")

# comboBox
# hari
label_day = ttk.Label(root, text="Hari:")
label_day.pack(pady=(10, 0))
chosen_day = tk.StringVar()
hari = ttk.Combobox(root, width = 27, textvariable = chosen_day)
hari['values'] = ('Senin', 
                  'Selasa',
                  'Rabu',
                  'Kamis',
                  'Jumat')
hari.pack()
hari.current()

# jam
label_hour = ttk.Label(root, text="Jam:")
label_hour.pack(pady=(10, 0))
chosen_hour = tk.StringVar()
hour = ttk.Combobox(root, width = 27, textvariable = chosen_hour)
hour['values'] = ('06.00', 
                  '12.00',
                  '16.00')
hour.pack()
hour.current()

label_type = ttk.Label(root, text="Jenis Kendaraan:")
label_type.pack(pady=(10, 0))
chosen_type = tk.StringVar()
type = ttk.Combobox(root, width = 27, textvariable = chosen_type)
type['values'] = ('Motor', 
                  'Mobil',
                  'Sepeda')
type.pack()
type.current()

hitung_button = ttk.Button(root, text="Hitung Rekomendasi", command=hitung_rekomendasi)
hitung_button.pack(pady=(10, 20))

hasil_label = ttk.Label(root, text="")
hasil_label.pack()

hasil_text = tk.Text(root, height=6, width=50, state=tk.DISABLED)
hasil_text.pack()

rekomendasi_label = ttk.Label(root, text="")
rekomendasi_label.pack()

rekomendasi_text = tk.Text(root, height=6, width=50, state=tk.DISABLED)
rekomendasi_text.pack()

root.mainloop()
