from django.db import models

# Create your models here.
class Provincia(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=50)
    codigo_ag=models.IntegerField()
    capital_ag=models.CharField(max_length=50)
    idioma_ag=models.CharField(max_length=100)

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.nombre_ag, self.codigo_ag, self.capital_ag, self.idioma_ag)


class Tipo(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=50)
    categoria_ag=models.CharField(max_length=100)
    descripcion_ag=models.TextField()

    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.nombre_ag, self.categoria_ag, self.descripcion_ag)


class Ingrediente(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=50)
    marca_ag=models.CharField(max_length=100)
    stock_ag=models.IntegerField()
    fecha_ven_ag=models.DateField()
    indicacion_ag=models.TextField()

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.nombre_ag, self.marca_ag, self.fecha_ven_ag, self.indicacion_ag)


class Cliente(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=50)
    apellido_ag=models.CharField(max_length=50)
    numero_ag=models.IntegerField()
    email_ag=models.EmailField()

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.nombre_ag, self.apellido_ag, self.numero_ag, self.email_ag)

class Pedido(models.Model):
    id_ag=models.AutoField(primary_key=True)
    descripcion_ag=models.TextField()
    cantidad_ag=models.IntegerField()
    metodo_pago_ag=models.CharField(max_length=50)
    codigo_ag=models.IntegerField()

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.descripcion_ag, self.cantidad_ag, self.metodo_pago_ag, self.idioma_ag)


class Platillo(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=80)
    descripcion_ag=models.TextField()
    precio_ag=models.DecimalField(max_digits=5, decimal_places=2)
    fotografia_ag=models.FileField(upload_to='platillos', null=True,blank=True)

    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.nombre_ag, self.descripcion_ag, self.precio_ag)


class Detalle(models.Model):
    id_ag=models.AutoField(primary_key=True)
    fecha_ag=models.DateField()
    hora_ag=models.TimeField()
    total_ag=models.DecimalField(max_digits=10, decimal_places=2)
    notas_cliente = models.TextField()

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.fecha_ag, self.hora_ag, self.tiempo_preparacion_ag, self.total_ag)


class Receta(models.Model):
    id_ag=models.AutoField(primary_key=True)
    nombre_ag=models.CharField(max_length=100)
    instrucciones_ag = models.TextField()
    tiempo_preparacion_ag = models.TimeField()
    fecha_creacion_ag = models.DateTimeField()

    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.nombre_ag, self.tiempo_preparacion_ag, self.fecha_creacion_ag)
