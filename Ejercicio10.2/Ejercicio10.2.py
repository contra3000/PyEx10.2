import tkinter
from tkinter import ttk


def main():

    def reset(event):
        print("reset")
        label2.config(text='')


    def destroy(event):
        print("Adios!")
        window.destroy()


    def imprimir(event):
        print(listbox.get(listbox.curselection()))
        label2.config(text=listbox.get(listbox.curselection()))


    window = tkinter.Tk()
    window.title("Ejercicio 10.2")
    window.geometry('200x350+0+0')

    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=3)

    frame = ttk.Frame(window)
    frame.grid(column=0, row=0, sticky=tkinter.W, padx=25)

    label1 = ttk.Label(frame, text='País:')
    label1.grid(column=0, row=0, padx=5, pady=5, sticky='w')

    select = tkinter.StringVar()
    lista = ['Argentina', 'Brasil', 'Paraguay', 'Uruguay', 'Chile', 'Bolivia']
    lista = sorted(lista)
    listbox = tkinter.Listbox(frame)
    for item in lista:
        listbox.insert('end', item)
    listbox.grid(column=0, row=1, padx=5, pady=5, sticky='w')

    botonEnter = ttk.Button(frame, text='Enter')
    botonEnter.grid(column=0, row=4, padx=5, pady=5)
    botonEnter.bind('<Button-1>', imprimir)

    botonReset = ttk.Button(frame, text='Reset')
    botonReset.grid(column=0, row=5, padx=5, pady=5)
    botonReset.bind('<Button-1>', reset)

    botonExit = ttk.Button(frame, text='Exit')
    botonExit.grid(column=0, row=6, padx=5, pady=5)
    botonExit.bind('<Button-1>', destroy)

    label2 = ttk.Label(frame, text='', foreground='grey')
    label2.grid(column=0, row=7, padx=5, pady=5)

    window.mainloop()


if __name__ == '__main__':
    main()
