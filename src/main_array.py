from DataStructures.dynamicArray import DynamicArray
import time
import random
start_time = time.time()

if __name__ == '__main__':
  
  with open("BDD.txt", "r") as fileData:
    data = fileData.readlines()

  list_of_data=DynamicArray()
  list_of_compare=DynamicArray()
  list_of_serials=DynamicArray()
  for line in data:
    line.strip()
    olx = line.split(", ")
    list_of_data.append((olx[0].strip(),olx[1].strip()))

  size_array=list_of_data.__len__()
  
  with open("serials_choice.txt","r") as fileData2:
    serial_random = fileData2.readlines()

  for line in serial_random:
    list_of_serials.append(line.strip())
  size_of_list_of_serials=list_of_serials.__len__()

  def read(arreglo, producto):
    for i in range(1, size_array):
      valor1, valor2 = arreglo[i]
      if producto in valor1:
        list_of_compare.append((valor1,valor2))
        
  def compare(arreglo):
    serial, minimo = arreglo[0]
    
    for i in range(2, size_array2):
      serial1, minimo1 = arreglo[i]
      if int(minimo1) < int(minimo):
          minimo = minimo1
          serial = serial1
    print(str("El identificador con valor mas bajo se encuentra en: ") + serial + str(" con valor: ") + minimo)
    
#Se ingresa un número determinado para la cantidad de tiendas
  
  productsQty = random.randint(1, 20)
  for item in range(productsQty):
    indice_aleatorio = random.randint(0, size_of_list_of_serials-1)
    desiredProduct = list_of_serials[indice_aleatorio]
    read(list_of_data,desiredProduct)
    size_array2=list_of_compare.__len__()
    compare(list_of_compare)
    list_of_compare=[]
    
end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")