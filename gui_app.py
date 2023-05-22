import tkinter as tk
from tkinter import ttk

 
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height =300)
 
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='INICIO', menu = menu_inicio)
 
    menu_inicio.add_command(label='Crear Registro en Base de datos')
    menu_inicio.add_command(label='Eliminar Registro en Base de datos')
    menu_inicio.add_command(label='Salir', command = root.destroy)
 

# Primera parte

class Frame(tk.Frame):
     def __init__(self, root =  None): 
         super().__init__(root, width = 480, height =320)
         self.root = root
         self.pack()
         self.config(bg = 'Gray79')  

         self.campos_pelicula()
         self.desabilitar_campos()
   
         self.habilitar_campos()
 


# #boton inicial con imagen
         

     # #     self.boton_ingresar = tk.Button(self, text="INGRESAR", command= self.habilitar_campos)
     # #     self.boton_ingresar.config(width=40, font=('Times New Roman', 12), 
     # #             fg='#666666', bg='RED', cursor='hand2', activebackground='#666666')
     # #     self.boton_ingresar.grid(row=3, column=0, padx=10, pady=10)

     #       self.img1=tk.PhotoImage(file=" ")
     #       self.labelimagen1=tk.Label(self.   , imagen=self.img1).place(x=50, y=50,)

     # # def boton_ingresar(self):
     # #     self.ventana1.destroy
     # #     self.ventana1.withdraw()
     # #     self.ventana2=tk.Toplevel()


# ----segunda parte


     def campos_pelicula(self):
         self.label_nombre = tk.Label(self, text ='Nombre:')
         self.label_nombre.config (font =('Times New Roman', 12))
         self.label_nombre.grid(row=0, column= 0, padx=15, pady=10)
 
         self.label_puntacion = tk.Label(self, text ='Puntuación:')
         self.label_puntacion.config (font =('Times New Roman', 12))
         self.label_puntacion.grid(row=1, column= 0, padx=15, pady=10)
 
         self.label_genero =tk.Label (self, text='Género:')
         self.label_genero.config (font =('Times New Roman', 12))
         self.label_genero.grid(row=2, column= 0, padx=15, pady=10)



#entrys de cada campo
         self.mi_nombre= tk.StringVar()
         self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
         self.entry_nombre.config(width=50, font=('Times New Roman', 12))
         self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
         self.mi_puntacion= tk.StringVar()
         self.entry_puntacion = tk.Entry(self, textvariable = self.mi_puntacion)
         self.entry_puntacion.config(width=50, font=('Times New Roman',12))
         self.entry_puntacion.grid(row=1, column=1, padx=10, pady=10)
 
         self.mi_genero= tk.StringVar()
         self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
         self.entry_genero.config(width=50, font=('Times New Roman', 12))
         self.entry_genero.grid(row=2, column=1, padx=10, pady=10)
 
 
#botones nuevo
 
         self.boton_nuevo = tk.Button(self, text="Nuevo", command= self.habilitar_campos)
         self.boton_nuevo.config(width=20, font=('Times New Roman', 12, 'bold'), 
                 fg='black', bg='white', cursor='hand2', activebackground='gray63')
         self.boton_nuevo.grid(row=3, column=1, padx=10, pady=10)
 
#botones guardar
 
         self.boton_guardar = tk.Button(self, text="Guardar", command= self.guardar_datos)
         self.boton_guardar.config(width=20, font=('Times New Roman', 12, 'bold'), 
                 fg='#DAD5D6', bg='#666666', cursor='hand2', activebackground= 'gray63')
         self.boton_guardar.grid(row=4, column=2, padx=10, pady=10)
 
#botones cancelar
 
         self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.desabilitar_campos)
         self.boton_cancelar.config(width=20, font=('Times New Roman', 12, 'bold'),
                fg='#DAD5D6', bg='red', cursor='hand2', activebackground='gray63')
         self.boton_cancelar.grid(row=5, column=3, padx=10, pady=10)

     def habilitar_campos(self):
         
         self.mi_nombre.set('')
         self.mi_puntacion.set('')
         self.mi_genero.set('')

         self.entry_nombre.config(state='normal')
         self.entry_puntacion.config(state='normal')
         self.entry_genero.config(state='normal')

         self.boton_guardar.config(state='normal')
         self.boton_cancelar.config(state='normal')


     def desabilitar_campos(self):

         self.mi_nombre.set('')
         self.mi_puntacion.set('')
         self.mi_genero.set('')

         self.entry_nombre.config(state='disabled')
         self.entry_puntacion.config(state='disabled')
         self.entry_genero.config(state='disabled')

         self.boton_guardar.config(state='disabled')
         self.boton_cancelar.config(state='disabled')


     def guardar_datos(self):

         self.desabilitar_campos()

# tercera parte


         # def    (self):
         # destroy





