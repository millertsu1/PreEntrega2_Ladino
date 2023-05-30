class Client:
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.purchased_products = []

    def add_product(self, product):
        self.purchased_products.append(product)
        print(f"El producto '{product}' ha sido agregado a la lista de compras de {self.name}.")

    def show_information(self):
        print(f"Información del cliente:")
        print(f"Nombre: {self.name}")
        print(f"Correo electrónico: {self.email}")
        print(f"Dirección: {self.address}")
        print(f"Teléfono: {self.phone}")

    def show_list(self):
        print(f"Esta es la lista de productos actualmente el en carrito de compras {self.purchased_products}")

    def __str__(self):
        return self.name

# Ejemplo de uso del programa
client1 = Client("Miller ladino", "millerladino@gmail.com", "Calle 4#163 22", "3229399534")
client1.add_product("zapatillas")
client1.add_product("gabardina")
client1.show_information()
client1.show_list()
print(client1)  # Imprime el nombre del cliente utilizando el método __str__()

