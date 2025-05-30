import tkinter as tk
from tkinter import messagebox

class Suma:
    def __init__(self): 
        self.ventana = tk.Tk()
        self.ventana.title("Suma de dos números")

        tk.Label(self.ventana, text="Escribe el primer numero:").grid(row=0, column=0, padx=10, pady=5)
        self.entrada1 = tk.Entry(self.ventana)
        self.entrada1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Escribe el segundo numero:").grid(row=1, column=0, padx=10, pady=5)
        self.entrada2 = tk.Entry(self.ventana)
        self.entrada2.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(
            self.ventana,
            text="Sumar",
            command=lambda: messagebox.showinfo(
                "Resultado",
                f"La suma es: {int(self.entrada1.get()) + int(self.entrada2.get())}"
            ) if self.entrada1.get().isdigit() and self.entrada2.get().isdigit()
            else messagebox.showerror("Error", "Solo se permiten numeros.")
        ).grid(row=2, column=0, columnspan=2, pady=10)

        self.ventana.mainloop()

def main():
    Suma()

main()
