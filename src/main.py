from DataStructures.dynamicArray import DynamicArray
from DataStructures.linkedList import LinkedList
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

if __name__ == '__main__':
  def UI():
    #Pantalla de 300x400
    root = tk.Tk()
    root.geometry("300x400")
    root.resizable(False,False)
    root.iconphoto(True, tk.PhotoImage(file='.//Resources//icon.png'))
    
    #Pantalla de inicio
    def inicio():
        root.title("Inicio")
        inicio_square_frame.grid(row=0,column=0)
        inicio_message_label.grid(row=1,column=0)
        inicio_sign_in_button.grid(row=2,column=0)
        inicio_logo_label.grid(row=0,column=0)
    
    #Borrar Pantalla de Inicio
    def delete_inicio():
        inicio_square_frame.grid_forget()
        inicio_message_label.grid_forget()
        inicio_sign_in_button.grid_forget()
        inicio_logo_label.grid_forget()
    
    #Pantalla Home
    def home():
        delete_inicio()
        delete_shoppingcart()
        root.title("Home")
        home_square_frame.place(x=50,y=20)
        home_text_box.place(x=65,y=140)
        home_agregar_button.place(x=85,y=185)
        home_eliminar_button.place(x=85,y=230)
        home_shoppingcart_button.place(x=85,y=275)
        home_buscar_button.place(x=85,y=320)
        pass
    
    #Borrar pantalla Home
    def delete_home():
        home_square_frame.place_forget()
        home_text_box.place_forget()
        home_agregar_button.place_forget()
        home_eliminar_button.place_forget()
        home_shoppingcart_button.place_forget()
        home_buscar_button.place_forget()
        elemento_agregado_label.place_forget()
    
    #Funcion que retorna lo escrito en una text box
    def get_text(text_box):
        texto=text_box.get()
        return texto
    
    #Agrega Producto
    def agregar():
        element=get_text(home_text_box)
        add_to_list(element)
        list_of_compare.clear()
        home_text_box.delete(0, tk.END)
    
        if element:
            elemento_agregado_label.config(text="El producto ha sido \n agregado correctamente.", font=("Arial", 10))
            elemento_agregado_label.place(x=63,y=30)
            elemento_agregado_label.after(3000,hide_message,elemento_agregado_label)
            return element
        else:
            elemento_agregado_label.config(text="El producto NO ha sido \n agregado correctamente.", font=("Arial", 10))
            elemento_agregado_label.place(x=63,y=30)
            elemento_agregado_label.after(3000,hide_message,elemento_agregado_label)
            pass
    
    def hide_message(message):
        message.config(text="")  # Clear the label
    
    #Borrar elemento de la lista
    def eliminar():
        element=get_text(home_text_box)
        delete_element_of_shoppingcart(element)
        home_text_box.delete(0, tk.END)
    
        if element:
            elemento_agregado_label.config(text="El producto ha sido \n eliminado correctamente.", font=("Arial", 10))
            elemento_agregado_label.place(x=63,y=30)
            elemento_agregado_label.after(3000,hide_message,elemento_agregado_label)
            return element
        else:
            elemento_agregado_label.config(text="El producto NO ha sido \n eliminado correctamente.", font=("Arial", 10))
            elemento_agregado_label.place(x=63,y=30)
            elemento_agregado_label.after(3000,hide_message,elemento_agregado_label)
        
    #Funcion para mostrar el shoppingcart
    def show_shoppingcart():
      productos_scrolled.configure(state='normal')
      productos_scrolled.delete('1.0', tk.END) 
      
      actual = list_of_products.head
      while actual is not None:
          productos_scrolled.insert(tk.END, f"Item {actual.serial}       {actual.data}\n")
          actual = actual.next
      
      productos_scrolled.configure(state='disabled')


    #Crear ventana del shoppingcart
    def shoppingcart():
        delete_home()
        root.title("Carrito")
        productos_scrolled.place(x=50,y=40)
        back_button.place(x=85,y=300)
        show_shoppingcart()
    
    #Borrar ventana del shoppingcart
    def delete_shoppingcart():
      productos_scrolled.configure(state='normal')
      productos_scrolled.delete('1.0', tk.END)
      productos_scrolled.configure(state='disabled')
      productos_scrolled.place_forget()
      back_button.place_forget()

    
    def buscar():
        element=get_text(home_text_box)
        home_text_box.delete(0, tk.END)
        return element
    
    #Estilo de botones
    style = ttk.Style()
    
    style.configure("StylizedButton.TButton",
                    relief="flat",
                    background="#E5FBF8",
                    foreground="black",
                    font=("Helvetica", 12),
                    padding=10,
                    borderwidth=1)
    
    #INICIO
    #Blue square-inicio
    inicio_square_frame = tk.Frame(root, width=350, height=250, bg="#00D4BB")
    #Mensaje de bienvenida-inicio
    inicio_message_label = tk.Label(root, text="Comencemos", font=("Arial", 14, "bold"), width=15,height=3)
    #Boton de Ingresar-inicio
    inicio_sign_in_button = ttk.Button(root, text="Ingresar",style="StylizedButton.TButton" ,command=home)
    #Logo Economerk
    inicio_logo_label= tk.Label(root, text="ECONOMERK", font=("Arial", 25, "italic", "bold"),fg="#FFD600", bg="#00D4BB", width=15,height=3)
    
    #HOME
    #Gray Square-home
    home_square_frame = tk.Frame(root, width=200, height=100, bg="#E5FBF8",highlightbackground="#000000", highlightthickness=1)
    #Caja de Texto-home
    home_text_box= tk.Entry(root)
    #Boton Agregar
    home_agregar_button = ttk.Button(root, text="Agregar",style="StylizedButton.TButton", command=agregar)
    #Boton Eliminar
    home_eliminar_button = ttk.Button(root, text="Eliminar",style="StylizedButton.TButton", command=eliminar)
    #Boton shoppingcart
    home_shoppingcart_button = ttk.Button(root, text="Carrito",style="StylizedButton.TButton", command=shoppingcart)
    #Boton Buscar
    home_buscar_button = ttk.Button(root, text="Buscar",style="StylizedButton.TButton", command=buscar)
    #Mensaje de estado
    elemento_agregado_label = tk.Label(root, text="",bg="#E5FBF8", font=("Arial", 12), width=20,height=3)
    
    #shoppingcart
    #lista  de productos
    productos_scrolled = ScrolledText(root, width=25, height=10)
    productos_scrolled.configure(state ='disabled')
    
    #Boton de regresar
    back_button= ttk.Button(root, text="Regresar",style="StylizedButton.TButton" ,command=home)
    
    inicio()
    
    root.mainloop()



  with open("cienmil_elementos.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data=DynamicArray()
  list_of_compare=DynamicArray()
  list_of_serials=DynamicArray()
  list_of_products=LinkedList()
  #METODO QUE AGREGA TODA LA BASE DE DATOS INICIAL A UN ARREGLO DINAMICO
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.append((olx[0].strip(),olx[1].strip()))

  size_array=list_of_data.__len__()
    
#FUNCIÓN QUE AGREGA A UN ARREGLO DINAMICO LOS PRECIOS Y SERIALES DEL MISMO PRODUCTO DE DIFERENTES TIENDAS
  
#BUSQUEDA DEL ARTÍCULO ENTRE LAS TIENDAS
  def read(arreglo, producto):
    for i in range(1, size_array):
      valor1, valor2 = arreglo[i]
      if producto in valor1:
        list_of_compare.append((valor1,valor2))
#FUNCION QUE COMPARA LOS PRECIOS DEL MISMO PRODUCTO EN DIFERENTES TIENDAS         
  def compare(arreglo,size_array2):
    if size_array2==0:
      print("No está el producto en el arreglo")
    else:
      serial, minimo = arreglo[0]
      for i in range(2, size_array2):
        serial1, minimo1 = arreglo[i]
        if int(minimo1) < int(minimo):
            minimo = minimo1
            serial = serial1
      list_of_products.append(serial,minimo)

  #FUNCIÓN PARA AGREGAR AL shoppingcart
  def add_to_list(product):
    read(list_of_data, product)
    size_array2=list_of_compare.__len__()
    compare(list_of_compare, size_array2)

  #FUNCIÓN PARA ELIMINAR LOS PRODUCTOS DEL shoppingcart
  def clean_shoppingcart():
    list_of_products.clear()

  #FUNCIÓN PARA ELIMINAR UN PRODUCTO DEL shoppingcart
  def delete_element_of_shoppingcart(product):
    actual=list_of_products.head 
    while actual is not None:
      if product in actual.serial:
        list_of_products.delete(actual.data)
      actual=actual.next

  UI()
