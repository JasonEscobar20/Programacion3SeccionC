import graphviz

class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_at_empty_list(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("List isn't empty")
            
    def insert_at_first(self, data):
        if self.head is None:
            self.insert_at_empty_list(data)
            
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    
    
    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            
        pointer = self.head
        
        while pointer.next is not None:
            pointer = pointer.next
            
        new_node = Node(data)
        pointer.next = new_node
        new_node.previous = pointer
        
    
    def delete_by_carnet(self, carnet):
        if self.head is None:
            print('empty list')
            return
        
        if self.head.next is None:
            pointer_carnet = self.head.data.get('carnet')
            if pointer_carnet == carnet:
                self.head = None
                
            else:
                print("Element wasn't found")
        
        pointer_carnet = self.head.data.get('carnet')
        if pointer_carnet == carnet:
            
            if self.head is None:
                print("List doesn't have elements to delete")
                return
            
            if self.head.next is None:
                self.head = None
                
            self.head = self.head.next
            self.head.previous = None
        
        pointer = self.head
        
        while pointer.next is not None:
            if pointer.data.get('carnet') == carnet:
                break
            pointer = pointer.next
            
        if pointer.next is not None:
            pointer.previous.next = pointer.next
            pointer.next.previous = pointer.previous
            
        else:
            if pointer.data.get('carnet') == carnet:
                if self.head is None:
                    print("List doesn't have elements to delete")
                    return
                
                if self.head.next is None:
                    self.head = None
                    return 
                
                pointer = self.head
                
                while pointer.next is not None:
                    pointer = pointer.next
                    
                pointer.previous.next = None
         
         
    def display_list(self):
        if self.head is None:
            print("\nlista vacia\n")
            return 
        else:
            pointer = self.head
            start_graph = graphviz.Digraph("structs", filename='double_linked_list.gv', node_attr={'shape': 'plaintext'})
            
            counter = 1
            while pointer is not None:
                previous_node = pointer.previous.data if pointer.previous is not None else None
                next_node = pointer.next.data if pointer.next is not None else None
                # print(f"({previous_node}) <- ({pointer.data.get('nombre')}) -> ({next_node}) || " )
                previous_node_name = previous_node.get('nombre') if previous_node is not None else None
                next_node_name = next_node.get('nombre') if next_node is not None else None
                current_node_name = pointer.data.get('nombre')
                
                # start_graph.node(f'struct_{counter}', f'<f0> {previous_node_name}|<f1> {current_node_name}|<f2> {next_node_name}')
                start_graph.node(f'struct_{counter}', f'''<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                                    <TR>
                                        <TD PORT="f0">{str(previous_node_name)}</TD>
                                        <TD PORT="f1">{current_node_name}</TD>
                                        <TD PORT="f2">{str(next_node_name)}</TD>
                                    </TR>
                                    </TABLE>>''')
                pointer = pointer.next
                counter += 1
                
            edges = []
            for i in range(1, counter - 1):
                edges.append(
                    (f'struct_{i}', f'struct_{i + 1}')
                )
                
            print(edges, '=============')
            start_graph.edges(edges)
            start_graph.render('test/round-table.gv', view=True)
                
                
test = True
init_list = LinkedList()

while test:
    print("Bienvenido a como armar una lista doblemente enlazada")
    print("Acciones\n")
    print("1. Insertar al principio")
    print("2. Insertar al final")
    print("3. eliminar por carnet")
    print("4. mostrar lista")
    print("5. salir\n")
    eleccion = int(input("Ingresa su eleccion:  "))
    
    if eleccion == 1:
        print("Ingrese datos 1")
        nombre = input("nombre: ")
        while nombre == '': nombre = input('Nombre: ')
        
        apellido = input("apellido: ")
        while apellido == '': apellido = input("apellido: ")
        
        carnet = input("carnet: ")
        while carnet == '': carnet = input("carnet: ")
        
        new_data = {
            'nombre': nombre,
            'apellido': apellido,
            'carnet': carnet
        }
        init_list.insert_at_first(new_data)
        
    if eleccion == 2:
        print("Ingrese datos")
        nombre = input("nombre: ")
        while nombre == '': nombre = input('Nombre: ')
        
        apellido = input("apellido: ")
        while apellido == '': apellido = input("apellido: ")
        
        carnet = input("carnet: ")
        while carnet == '': carnet = input("carnet: ")
        
        new_data = {
            'nombre': nombre,
            'apellido': apellido,
            'carnet': carnet
        }
        init_list.insert_at_end(new_data)
        
    if eleccion == 3:
        carnet = input('ingrese el carnet a eliminar: ')
        while carnet == '': carnet = input("carnet: ")
        init_list.delete_by_carnet(carnet)
        
    if eleccion == 4:
        init_list.display_list()
        
    if eleccion == 5:
        test = False
        