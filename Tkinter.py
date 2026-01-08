from tkinter import *
windows = Tk()
windows.geometry("600x600")
windows.title("lihtsalt on")

#tekst
summa_label = Label(windows, text = "kulu/tulu", font=("Calibri", 10, "bold"))
kategooria_label = Label(windows, text = "Kategooria", font=("Calibri", 10, "bold"))
kirjeldus_label = Label(windows, text = "Kirjeldus", font=("Calibri", 10, "bold"))
tyyp_label = Label(windows, text="Tyyp", font=("Calibri", 10, "bold"))

#entry
summa_entry = Entry(windows, font=("Calibri", 10, "bold"))
kategooria_entry = Entry(windows, font=("Calibri", 10, "bold"))
kirjeldus_entry = Entry(windows, font=("Calibri", 10, "bold"))
tyyp_entry = Entry(windows, font=("Calibri", 10, "bold"))

#buttons
add_new_button = Button(windows, text="add new")
show_all_button = Button(windows, text="show all")
add_summa_button = Button(windows, text="add summa")


#positsioon
summa_label.grid(row=0, column=0)
kategooria_label.grid(row=1, column=0)
kirjeldus_label.grid(row=2, column=0)
tyyp_label.grid(row=3, column=0)

summa_entry.grid(row=0, column=1)
kategooria_entry.grid(row=1, column=1)
kirjeldus_entry.grid(row=2, column=1)
tyyp_entry.grid(row=3, column=1)

add_new_button.grid(row=1, column=5)
show_all_button.grid(row=2, column=5)
add_summa_button.grid(row=3, column=5)

windows.mainloop()