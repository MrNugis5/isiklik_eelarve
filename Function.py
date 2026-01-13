andmed = {}
order = 1
def add_new():
    global order
    
    andmed[order] ={
        "kulu/tulu": summa_entry.get(),
        "kategooria": kategooria_entry.get(),
        "kirjeldus": kirjeldus_entry.get(),
        "tyyp": tyyp_entry.get()
    }
    
    order += 1
    
    summa_entry.delete(0, END)
    kategooria_entry.delete(0, END)
    kirjeldus_entry.delete(0, END)
    tyyp_entry.delete(0, END)
    
def show_all():
    output_text.delete("1.0", END)  # clear previous text
    for k, v in andmed.items():
         output_text.insert(END, f"{key}: {value}\n")
        