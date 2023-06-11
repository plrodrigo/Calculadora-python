import tkinter as tk

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x700")
        self.config(bg="black", padx=5, pady=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_principal= tk.Frame(self, bg="#161616", padx=10, pady=10)
        self.frame_principal.grid(row=0, column=0, sticky="news")
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(2, weight=1)
        
        self.texto_pantalla1 = tk.StringVar(value=0)
        self.pantalla1 = tk.Label(self.frame_principal, bg="#1f1f1f", font=("default", 30), textvariable=self.texto_pantalla1, anchor="e", fg="white", padx=10)
        self.pantalla1.grid(row=0, column=0, sticky="we")

        self.texto_pantalla2 = tk.StringVar(value=0)
        self.pantalla2 = tk.Label(self.frame_principal, bg="#1f1f1f", font=("default", 60), textvariable=self.texto_pantalla2, anchor="e", fg="white", padx=10)
        self.pantalla2.grid(row=1, column=0, sticky="we")

        self.frame_botones = tk.Frame(self.frame_principal, bg="black")
        self.frame_botones.grid(row=2, column=0, sticky="nsew")

        lista_botones=[["C", "⌫", " / ", " * "], ["7", "8", " 9 ", "-"], ["4", "5", " 6 ", "+"], ["1", "2", " 3 ", "="], ["HI", "0", " . "]]
        
        self.botones_creados = []

        for i in range(len(lista_botones)):
            for j in range(len(lista_botones[i])):
                self.boton = tk.Button(self.frame_botones, text=lista_botones[i][j], 
                                       font=("default", 20),  bg="#181818", fg="white", 
                                       borderwidth=0, activebackground="#2f2f2f", command=lambda id=lista_botones[i][j].strip() : Calculadora.funcion_principal(id))
                
                self.boton.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                self.frame_botones.grid_columnconfigure(j, weight=1)
                self.frame_botones.grid_rowconfigure(i, weight=1)

                self.key=lista_botones[i][j]
                if self.key == "⌫":
                    self.key = "BackSpace"
                if self.key == "HI":
                    self.key="h"
                if self.key == "C":
                    self.key = "Delete"
                if self.key == "=":
                    self.key = "Return"
                    self.boton.grid(row=i, column=j, sticky="nsew", rowspan=2)

                self.bind("<Key-" + self.key +">", lambda event, b=self.boton: b.invoke()) 

                self.botones_creados.append(self.boton)

        def on_enter(e):
            e.widget.config(bg="#101010")
        def on_leave(e):
            e.widget.config(bg="#181818")

        for i in self.botones_creados:
            i.bind("<Enter>", on_enter)
            i.bind("<Leave>", on_leave)

class Calculadora(): 
    def __init__(self, interfaz):
        pass
        
    def funcion_principal(id): 
        id = id
        if interfaz.texto_pantalla1.get() == "0":
            interfaz.texto_pantalla1.set("")
        if interfaz.texto_pantalla2.get() == "0":
            interfaz.texto_pantalla2.set("")

        if id.isnumeric() or id == ".":
            interfaz.texto_pantalla2.set(interfaz.texto_pantalla2.get() + id)

        if id in ["/", "*", "-", "+"]:
            interfaz.texto_pantalla1.set(interfaz.texto_pantalla1.get() + interfaz.texto_pantalla2.get() + id)
            interfaz.texto_pantalla2.set("")
        
        if id == "C":
            interfaz.texto_pantalla1.set("0")
            interfaz.texto_pantalla2.set("0")
            
        if id == "⌫":
            if interfaz.texto_pantalla2.get() != "":
                interfaz.texto_pantalla2.set(interfaz.texto_pantalla2.get()[:-1])
            else:
                interfaz.texto_pantalla1.set(interfaz.texto_pantalla1.get()[:-1])

            if interfaz.texto_pantalla2.get() == "" and interfaz.texto_pantalla1.get() == "":
                interfaz.texto_pantalla2.set("0")
                interfaz.texto_pantalla1.set("0")

        if id == "=":
            if interfaz.texto_pantalla1.get() == "" and interfaz.texto_pantalla2.get() == "":
                interfaz.texto_pantalla2.set("0")
                interfaz.texto_pantalla1.set("0")
            else:
                try:
                    interfaz.texto_pantalla2.set(round(eval(interfaz.texto_pantalla1.get() + interfaz.texto_pantalla2.get()), 4))
                    interfaz.texto_pantalla1.set("0")

                except: 
                    interfaz.texto_pantalla2.set("Error")
                    interfaz.update()
                    interfaz.after(800)
                    interfaz.texto_pantalla1.set("0")
                    interfaz.texto_pantalla2.set("0")
           
        
if __name__=="__main__":
    interfaz = Interfaz()
    calculadora = Calculadora(interfaz)
    interfaz.mainloop()
