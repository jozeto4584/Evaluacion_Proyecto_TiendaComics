import random

class TiendaComics:
    def __init__(self):
        self.inventario = []
        self.capacidad_maxima_por_zona = {'A': 50, 'B': 50, 'C': 50, 'D': 50}
        self.inventario_por_zona = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    def generar_id(self):
        return random.randint(1, 100)

    def registrar_producto(self):
        nombre = input("Nombre del Producto: ")
        while True:
            precio_input = input("Precio unitario del producto: ")
            if precio_input.replace('.', '', 1).isdigit():
                precio = float(precio_input)
                break
            else:
                print("Por favor, ingrese un precio válido (solo números).")
        
        ubicacion = input("Ubicación en la tienda (A, B, C o D): ").upper()
        while ubicacion not in ['A', 'B', 'C', 'D']:
            print("Ubicación no válida. Por favor, ingrese una ubicación válida (A, B, C o D).")
            ubicacion = input("Ubicación en la tienda (A, B, C o D): ").upper()

        total_unidades_zona = sum(producto['unidades'] for producto in self.inventario if producto['ubicacion'] == ubicacion)

        if total_unidades_zona >= self.capacidad_maxima_por_zona[ubicacion]:
            print(f"Error: La zona {ubicacion} ha alcanzado su capacidad máxima de 50 productos.")
            return

        nuevas_unidades = int(input(f"Ingrese el número de unidades de {nombre} a agregar (máximo {self.capacidad_maxima_por_zona[ubicacion] - total_unidades_zona}): "))
        if total_unidades_zona + nuevas_unidades > self.capacidad_maxima_por_zona[ubicacion]:
            print(f"Error: No se pueden agregar más de {self.capacidad_maxima_por_zona[ubicacion] - total_unidades_zona} unidades en la zona {ubicacion}.")
            return

        descripcion = input("Descripción del producto: ")
        casa = input("Casa a la que pertenece el producto (Marvel,Universal, Sony, Warner, etc): ")
        referencia = input("Referencia (código alfanumérico): ")
        pais = input("País de origen del producto: ")

        while True:
            garantia = input("Producto con garantía extendida (S/N): ").upper()
            if garantia in ['S', 'N']:
                break
            else:
                print("Por favor, Digite una respuesta correcta (S para sí, N para no).")

        producto = {
            'id': self.generar_id(),
            'nombre': nombre,
            'precio': precio,
            'ubicacion': ubicacion,
            'descripcion': descripcion,
            'casa': casa,
            'referencia': referencia,
            'pais': pais,
            'unidades': nuevas_unidades,
            'garantia': garantia
        }

        self.inventario.append(producto)
        self.inventario_por_zona[ubicacion] += nuevas_unidades
        print("Producto registrado con éxito. ID del producto:", producto['id'])
    
    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            for producto in self.inventario:
                print("ID:", producto['id'])
                print("Nombre:", producto['nombre'])
                print("Precio:", producto['precio'])
                print("Descripción:", producto['descripcion'])
                print("Unidades:", producto['unidades'])
                print("Garantía:", producto['garantia'])
                print()

    def buscar_producto(self):
        nombre = input("Digite  el nombre del producto que deasea  buscar: ")
        encontrado = False
        for producto in self.inventario:
            if producto['nombre'].lower() == nombre.lower():
                print("ID:", producto['id'])
                print("Nombre:", producto['nombre'])
                print("Precio:", producto['precio'])
                print("Descripción:", producto['descripcion'])
                print("Unidades:", producto['unidades'])
                print("Garantía:", producto['garantia'])
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")
    
    def modificar_unidades(self):
        nombre = input("Ingrese el nombre del producto a modificar: ")
        nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        for producto in self.inventario:
            if producto['nombre'].lower() == nombre.lower():
                self.inventario_por_zona[producto['ubicacion']] -= producto['unidades']
                producto['unidades'] = nuevas_unidades
                self.inventario_por_zona[producto['ubicacion']] += nuevas_unidades
                print("cantidad  modificada con éxito.")
                return
        print("Producto no Encontrado.")

    def eliminar_producto(self):
        nombre = input("Digite  el nombre del producto  Que desea Eliminar : ")
        for producto in self.inventario:
            if producto['nombre'].lower() == nombre.lower():
                self.inventario_por_zona[producto['ubicacion']] -= producto['unidades']
                self.inventario.remove(producto)
                print("Producto eliminado del Inventario.")
                return
        print("Producto no encontrado.")
    
    def ejecutar(self):
        while True:
            print("*****Bienvenido A Nuestro de inventario de la tienda de Cómics****")
            print("******----------------------------------------------------********")
            print("1. Registrar producto")
            print("2. Mostrar unidades de inventario")
            print("3. Buscar producto por nombre")
            print("4. Modificar unidades compradas")
            print("5. Eliminar Un producto")
            print("6. Salir")
            
            opcion = input("Seleccione una Opción: ")

            if opcion == '1':
                self.registrar_producto()
            elif opcion == '2':
                self.mostrar_inventario()
            elif opcion == '3':
                self.buscar_producto()
            elif opcion == '4':
                self.modificar_unidades()
            elif opcion == '5':
                self.eliminar_producto()
            elif opcion == '6':
                print("¡Te Esperamos De Nuevo  !")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    tienda = TiendaComics()
    tienda.ejecutar()
