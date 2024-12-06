from django.db import models

# Modelo para Clientes
class Clientes(models.Model):
    nombre_cliente = models.CharField(max_length=20)
    apellido_cliente = models.CharField(max_length=20)
    email_cliente = models.EmailField(max_length=50)
    telefono_cliente = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente} - {self.email_cliente}"


# Modelo para Productos
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_producto} - ${self.precio}"


# Modelo para Pedidos
class Pedidos(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    direccion_entrega = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado_pedido} - Cliente: {self.id_cliente.nombre_cliente}"


# Modelo para DetallePedido
class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Pedido #{self.id_pedido.id} - Producto: {self.id_producto.nombre_producto}"


# Modelo para Pagos
class Pagos(models.Model):
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length=20)
    pago_pendiente = models.BooleanField()

    def __str__(self):
        return f"Pago #{self.id} - Pedido #{self.id_pedido.id} - {self.metodo_pago} - {self.estado_pago}"


# Modelo para CarritoVentas
class CarritoVentas(models.Model):
    id_usuario = models.ForeignKey('Trabajadores', on_delete=models.CASCADE)
    fecha_expiracion = models.DateField()

    def __str__(self):
        return f"Carrito #{self.id} - Usuario: {self.id_usuario.nombre_usuario}"


# Modelo para DetalleCarrito
class DetalleCarrito(models.Model):
    id_carrito = models.ForeignKey(CarritoVentas, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle de Carrito #{self.id_carrito.id} - Producto: {self.id_producto.nombre_producto}"


# Modelo para Trabajadores
class Trabajadores(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    apellido_usuario = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_usuario} {self.apellido_usuario} - {self.email}"


# Modelo para RolesTrabajadores
class RolesTrabajadores(models.Model):
    nombre_rol = models.CharField(max_length=20)

    def __str__(self):
        return f"Rol: {self.nombre_rol}"

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre_categoria}"

