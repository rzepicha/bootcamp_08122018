import tkinter
from tkinter import messagebox

def koszt_przejazdu():
    print("nacisnieto przycik")
    try:
        dyst=float(dyst_entry.get())
        spalanie=float(spalanie_entry.get())
        cena = float(cena_entry.get())
        wynik = dyst*spalanie*cena/100
        wynik_label.configure(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Dane powinny byc liczbami")


root=tkinter.Tk()
root.columnconfigure(1, weight=1)
dyst_label=tkinter.Label(master=root, text='dystans')
dyst_label.grid(row=0, column=0)
dyst_entry=tkinter.Entry(master=root)
dyst_entry.grid(row=0, column=1)

spalanie_label=tkinter.Label(master=root, text='spalanie')
spalanie_label.grid(row=1, column=0)
spalanie_entry=tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

cena_label=tkinter.Label(master=root, text='cena paliwa')
cena_label.grid(row=2, column=0)
cena_entry=tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1)

button=tkinter.Button(master=root, text='Koszt przejazdu', command=koszt_przejazdu)
button.grid(row=3, column=1)

wynik_label=tkinter.Label(master=root, text='-')
wynik_label.grid(row=4, column=2)

root.mainloop()