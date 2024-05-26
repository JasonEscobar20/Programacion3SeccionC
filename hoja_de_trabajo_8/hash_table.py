import csv

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        
        # validar si ya existe la llave y si es así, actualizar el valor
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
            
        # si la llave no existe, agregar el par (llave, valor)
        self.table[index].append([key, value])
        print(f'Insertado {key} en {value} en el índice {index}')
        
    def search_by_key(self, key):
        index = self._hash(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        
        return None
    
    def search_by_value(self, value):
        for index in range(self.size):
            for pair in self.table[index]:
                if pair[1] == value:
                    return pair[0]
                
        return None
        
    
    def display(self):
        for index in range(self.size):
            print(index, end=' ')
            for pair in self.table[index]:
                print('-->', end=' ')
                print(pair, end=' ')
                
            print()
            
    def load_from_csv(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) != 2:
                        print(f'Saltar fila no válida: {row}')
                        continue
                    key, value = row
                    self.insert(key, value)
            print(f'Data cargada de {filename}')
        except FileNotFoundError:
            print(f'Archivo {filename} no encontrado')
            
def menu():
    hash_table = HashTable(size=10)
    
    while True:
        print('/nMenú:')
        print('1. Insertar elemento')
        print('2. Buscar por llave')
        print('3. Buscar por valor')
        print('4. Mostrar tabla de hash')
        print('5. cargar datos desde archivo CSV')
        print('6. Salir')
        
        
        
        choice = input('Seleccione una opción: ')
        
        if choice == '1':
            key = input('Ingrese la llave: ')
            value = input('Ingrese el valor: ')
            hash_table.insert(key, value)
            print(f'Hash para clave {key}: {hash_table._hash(key)}')
            input('continuar..')
            
        elif choice == '2':
            key = input('Ingrese la llave a buscar: ')
            result = hash_table.search_by_key(key)
            if result:
                input(f'Valor encontrado: {result}')
            else:
                print('Valor no encontrado')
                
            input('continuar..')
                
        elif choice == '3':
            value = input('Ingrese el valor a buscar: ')
            result = hash_table.search_by_value(value)
            if result:
                input(f'LLave encontrada: {result}')
            else:
                print('LLave no encontrada')
                
            input('continuar..')
        
        elif choice == '4':
            print("\nTabla de hash:")
            hash_table.display()
            input('continuar..')
            
        elif choice == '5':
            filename = input("Ingreso ubicacion de archivo CSV: ")
            hash_table.load_from_csv(filename)
            
        elif choice == '6':
            print('Saliendo...')
            break
        
        else:
            print('Opción inválida. Intente de nuevo. \n\n')
            input('continuar..')
            
# Ejemplo de uso
if __name__ == '__main__':
    menu()