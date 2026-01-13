def add_new():
    global order
    
    andmed[order] ={
        "summa": int(summa_entry.get()),
        "kategooria": kategooria_entry.get(),
        "kirjeldus": kirjeldus_entry.get(),
        "tyyp": kulu_tulu_var.get()
    }
    
    order += 1
    
    summa_entry.delete(0, END)
    kategooria_entry.delete(0, END)
    kirjeldus_entry.delete(0, END)
    
def show_all():
    output_text.delete("1.0", END)
    for k, v in andmed.items():
        output_text.insert(END, f"list {k}\n")
        output_text.insert(END, f"  summa: {v['summa']}\n")
        output_text.insert(END, f"  Kategooria: {v['kategooria']}\n")
        output_text.insert(END, f"  Kirjeldus: {v['kirjeldus']}\n")
        output_text.insert(END, f"  Tüüp: {v['tyyp']}\n\n")
