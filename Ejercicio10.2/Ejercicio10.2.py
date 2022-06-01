import tkinter
from tkinter import ttk


def main():

    def reset(event):
        print("reset")
        select.set('0')


    def destroy(event):
        print("Adios!")
        window.destroy()


    def imprimir(event):
        print(f"Opción {select.get()}")


    window = tkinter.Tk()

    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=3)

    frame = ttk.Frame(window)
    frame.grid(column=0, row=0, sticky=tkinter.W)

    label1 = ttk.Label(frame, text='Genero:', background='black', foreground='white')
    label1.grid(column=0, row=0, padx=5, pady=5, sticky='w')

    select = tkinter.StringVar()
    r11 = ttk.Radiobutton(frame, text='Masculino', value='1', variable=select)
    r22 = ttk.Radiobutton(frame, text='Femenino', value='2', variable=select)
    r33 = ttk.Radiobutton(frame, text='Otro', value='3', variable=select)

    r11.grid(column=0, row=1, padx=5, pady=5, sticky='w')
    r22.grid(column=0, row=2, padx=5, pady=5, sticky='w')
    r33.grid(column=0, row=3, padx=5, pady=5, sticky='w')

    botonEnter = ttk.Button(frame, text='Next')
    botonEnter.grid(column=0, row=4, padx=5, pady=5)
    botonEnter.bind('<Button-1>', imprimir)

    botonReset = ttk.Button(frame, text='Reset')
    botonReset.grid(column=0, row=5, padx=5, pady=5)
    botonReset.bind('<Button-1>', reset)

    botonExit = ttk.Button(frame, text='Exit')
    botonExit.grid(column=0, row=6, padx=5, pady=5)
    botonExit.bind('<Button-1>', destroy)

    window.mainloop()


if __name__ == '__main__':
    main()
