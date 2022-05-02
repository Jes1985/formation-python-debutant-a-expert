import tkinter as tk
from tkinter.font import Font

fenetre = tk.Tk()
fenetre.title("Calculatrice")

texte = tk.StringVar(value="")
label = tk.Label(textvariable=texte, width=29, pady=20,
                borderwidth=2, relief="groove",
                font=Font(family= "Comic Sans MS", size=16, weight="bold"))
label.pack()

nombres = []
operations = []
def handler_click(event):
    val = event.widget.cget("text").strip()
    if not val:
        return
    if val in "0123456789.":
        if val == '.' and val in texte.get():
            return
        texte.set(texte.get() + val)
    else:
        global nombres
        global operations
        if val == 'C':
            texte.set('')
            return

        nombre = int(texte.get()) if '.' not in texte.get() else float(texte.get())
        nombres.append(nombre)
        if val in '+-/x':
            operations.append(val)
            texte.set("")

        if val == "=":
            # print(nombres)
            # print(operations)
            formule = f"{nombres[0]}"
            for i, op in enumerate(operations):
                op = op.replace("x", "*")
                formule = formule + f"{op}{nombres[i+1]}"
            # print(formule)
            texte.set(eval(formule))
            operations = []
            nombres = []

btn_texte = ['  ', '  ', 'C', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '  ', '0', '.','=']

k = 0
btns = {}
frame = tk.Frame()
for i in range(5):
    for j in range(4):
        if k >= len(btn_texte):
            break
        val = btn_texte[k]
        btn = tk.Button(frame, text=val, padx=40, pady=20)
        btns[val] = btn
        btns[val].bind("<Button-1>", handler_click)
        btn.grid(row=i, column=j)
        k += 1

btns['C'].configure(padx=39)
btns['-'].configure(padx=41)
btns['.'].configure(padx=41)

frame.pack()
fenetre.mainloop()