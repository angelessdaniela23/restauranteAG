from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Provincia, Tipo, Ingrediente, Cliente, Pedido, Platillo, Detalle, Receta

# CREAR VISTA PROVINCIA
def listadoProvincias(request):
    provinciasBdd=Provincia.objects.all()
    return render(request, 'listadoProvincias.html', {'provincias':provinciasBdd})


def guardarProvincia(request):
    nombre_ag=request.POST["nombre_ag"]
    codigo_ag=request.POST["codigo_ag"]
    capital_ag=request.POST["capital_ag"]
    idioma_ag=request.POST["idioma_ag"]
    #Insertando datos mediante el ORM de django
    provincia =Provincia.objects.create(nombre_ag=nombre_ag,codigo_ag=codigo_ag,capital_ag=capital_ag,idioma_ag=idioma_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarProvincia(request,id_ag):
    provinciaEliminar=Provincia.objects.get(id_ag=id_ag)
    provinciaEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarProvincia(request,id_ag):
    provinciaEditar=Provincia.objects.get(id_ag=id_ag)
    return render(request,'editarProvincia.html',{'provincia':provinciaEditar})

def procesarActualizacionProvincia(request):
    id_ag=request.POST["id_ag"]
    nombre_ag=request.POST["nombre_ag"]
    codigo_ag=request.POST["codigo_ag"]
    capital_ag=request.POST["capital_ag"]
    idioma_ag=request.POST["idioma_ag"]
    #Insertando datos mediante el ORM de DJANGO
    provinciaEditar=Provincia.objects.get(id_ag=id_ag)
    provinciaEditar.nombre_ag=nombre_ag
    provinciaEditar.codigo_ag=codigo_ag
    provinciaEditar.capital_ag=capital_ag
    provinciaEditar.idioma_ag=idioma_ag
    provinciaEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA TIPOS
def listadoTipos(request):
    tiposBdd=Tipo.objects.all()
    return render(request, 'listadoTipos.html', {'tipos':tiposBdd})


def guardarTipo(request):
    nombre_ag=request.POST["nombre_ag"]
    categoria_ag=request.POST["categoria_ag"]
    descripcion_ag=request.POST["descripcion_ag"]
    #Insertando datos mediante el ORM de django
    tipo =Tipo.objects.create(nombre_ag=nombre_ag,categoria_ag=categoria_ag,descripcion_ag=descripcion_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarTipo(request,id_ag):
    tipoEliminar=Tipo.objects.get(id_ag=id_ag)
    tipoEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarTipo(request,id_ag):
    tipoEditar=Tipo.objects.get(id_ag=id_ag)
    return render(request,'editarTipo.html',{'tipo':tipoEditar})

def procesarActualizacionTipo(request):
    id_ag=request.POST["id_ag"]
    nombre_ag=request.POST["nombre_ag"]
    categoria_ag=request.POST["categoria_ag"]
    descripcion_ag=request.POST["descripcion_ag"]
    #Insertando datos mediante el ORM de DJANGO
    tipoEditar.nombre_ag=cedula
    tipoEditar.categoria_ag=apellido
    tipoEditar.descripcion_ag=nombre
    tipoEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA INGREDIENTES
def listadoIngredientes(request):
    ingredientesBdd=Ingrediente.objects.all()
    return render(request, 'listadoIngredientes.html', {'ingredientes':ingredientesBdd})


def guardarIngrediente(request):
    nombre_ag=request.POST["nombre_ag"]
    marca_ag=request.POST["marca_ag"]
    stock_ag=request.POST["stock_ag"]
    fecha_ven_ag=request.POST["fecha_ven_ag"]
    indicacion_ag=request.POST["indicacion_ag"]
    #Insertando datos mediante el ORM de django
    ingrediente =Ingrediente.objects.create(nombre_ag=nombre_ag,marca_ag=marca_ag,stock_ag=stock_ag,fecha_ven_ag=fecha_ven_ag, indicacion_ag=indicacion_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarIngrediente(request,id_ag):
    ingredienteEliminar=Ingrediente.objects.get(id_ag=id_ag)
    ingredienteEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarIngrediente(request,id_ag):
    ingredienteEditar=Ingrediente.objects.get(id_ag=id_ag)
    return render(request,'editarIngrediente.html',{'ingrediente':ingredienteEditar})

def procesarActualizacionIngrediente(request):
    nombre_ag=request.POST["nombre_ag"]
    marca_ag=request.POST["marca_ag"]
    stock_ag=request.POST["stock_ag"]
    fecha_ven_ag=request.POST["fecha_ven_ag"]
    indicacion_ag=request.POST["indicacion_ag"]
    #Insertando datos mediante el ORM de DJANGO
    ingredienteEditar=Ingrediente.objects.get(id_ag=id_ag)
    ingredienteEditar.nombre_ag=nombre_ag
    ingredienteEditar.marca_ag=codigo_ag
    ingredienteEditar.stock_ag=capital_ag
    ingredienteEditar.fecha_ven_ag=idioma_ag
    ingredienteEditar.indicacion_ag=idioma_ag
    ingredienteEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')



# CREAR VISTA CLIENTES
def listadoClientes(request):
    clientesBdd=Cliente.objects.all()
    return render(request, 'listadoClientes.html', {'clientes':clientesBdd})


def guardarCliente(request):
    nombre_ag=request.POST["nombre_ag"]
    apellido_ag=request.POST["apellido_ag"]
    numero_ag=request.POST["numero_ag"]
    email_ag=request.POST["email_ag"]
    #Insertando datos mediante el ORM de django
    cliente =Cliente.objects.create(nombre_ag=nombre_ag,apellido_ag=apellido_ag,numero_ag=numero_ag,email_ag=email_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarCliente(request,id_ag):
    clienteEliminar=Cliente.objects.get(id_ag=id_ag)
    clienteEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarCliente(request,id_ag):
    clienteEditar=Cliente.objects.get(id_ag=id_ag)
    return render(request,'editarCliente.html',{'cliente':clienteEditar})

def procesarActualizacionCliente(request):
    id_ag=request.POST["id_ag"]
    nombre_ag=request.POST["nombre_ag"]
    apellido_ag=request.POST["apellido_ag"]
    numero_ag=request.POST["numero_ag"]
    email_ag=request.POST["email_ag"]
    #Insertando datos mediante el ORM de DJANGO
    clienteEditar=cliente.objects.get(id_ag=id_ag)
    clienteEditar.nombre_ag=nombre_ag
    clienteEditar.apellido_ag=apellido_ag
    clienteEditar.numero_ag=numero_ag
    clienteEditar.email_ag=email_ag
    clienteEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA PEDIDOS
def listadoPedidos(request):
    pedidosBdd=Pedido.objects.all()
    return render(request, 'listadoPedidos.html', {'pedidos':pedidosBdd})


def guardarPedido(request):
    descripcion_ag=request.POST["descripcion_ag"]
    cantidad_ag=request.POST["cantidad_ag"]
    metodo_pago_ag=request.POST["metodo_pago_ag"]
    codigo_ag=request.POST["codigo_ag"]
    #Insertando datos mediante el ORM de django
    pedido =Pedido.objects.create(descripcion_ag=descripcion_ag,cantidad_ag=cantidad_ag,metodo_pago_ag=metodo_pago_ag,codigo_ag=codigo_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarPedido(request,id_ag):
    pedidoEliminar=Pedido.objects.get(id_ag=id_ag)
    pedidoEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarPedido(request,id_ag):
    pedidoEditar=Pedido.objects.get(id_ag=id_ag)
    return render(request,'editarPedido.html',{'pedido':pedidoEditar})

def procesarActualizacionPedido(request):
    id_ag=request.POST["id_ag"]
    descripcion_ag=request.POST["descripcion_ag"]
    cantidad_ag=request.POST["cantidad_ag"]
    metodo_pago_ag=request.POST["metodo_pago_ag"]
    codigo_ag=request.POST["codigo_ag"]
    #Insertando datos mediante el ORM de DJANGO
    pedidoEditar=pedido.objects.get(id_ag=id_ag)
    pedidoEditar.descripcion_ag=descripcion_ag
    pedidoEditar.cantidad_ag=cantidad_ag
    pedidoEditar.metodo_pago_ag=metodo_pago_ag
    pedidoEditar.codigo_ag=codigo_ag
    pedidoEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA PLATILLOS
def listadoPlatillos(request):
    platillosBdd=Platillo.objects.all()
    return render(request, 'listadoPlatillos.html', {'platillos':platillosBdd})


def guardarPlatillo(request):
    nombre_ag=request.POST["nombre_ag"]
    descripcion_ag=request.POST["descripcion_ag"]
    precio_ag=request.POST["precio_ag"]
    fotografia_ag=request.POST["fotografia_ag"]
    #Insertando datos mediante el ORM de django
    platillo =Platillo.objects.create(nombre_ag=nombre_ag,descripcion_ag=descripcion_ag,precio_ag=precio_ag,fotografia_ag=fotografia_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarPlatillo(request,id_ag):
    platilloEliminar=Platillo.objects.get(id_ag=id_ag)
    platilloEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarPlatillo(request,id_ag):
    platilloEditar=Platillo.objects.get(id_ag=id_ag)
    return render(request,'editarPlatillo.html',{'platillo':platilloEditar})

def procesarActualizacionPlatillo(request):
    id_ag=request.POST["id_ag"]
    nombre_ag=request.POST["nombre_ag"]
    descripcion_ag=request.POST["descripcion_ag"]
    precio_ag=request.POST["precio_ag"]
    fotografia_ag=request.POST["fotografia_ag"]
    #Insertando datos mediante el ORM de DJANGO
    platilloEditar=Platillo.objects.get(id_ag=id_ag)
    platilloEditar.nombre_ag=nombre_ag
    platilloEditar.descripcion_ag=descripcion_ag
    platilloEditar.precio_ag=precio_ag
    platilloEditar.fotografia_ag=fotografia_ag
    platilloEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA DETALLES
def listadoDetalles(request):
    detallesBdd=Detalle.objects.all()
    return render(request, 'listadoDetalles.html', {'detalles':detallesBdd})


def guardarDetalle(request):
    fecha_ag=request.POST["fecha_ag"]
    hora_ag=request.POST["hora_ag"]
    total_ag=request.POST["total_ag"]
    notas_cliente=request.POST["notas_cliente"]
    #Insertando datos mediante el ORM de django
    detalle =Detalle.objects.create(fecha_ag=fecha_ag,hora_ag=hora_ag,total_ag=total_ag,notas_cliente=notas_cliente)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarDetalle(request,id_ag):
    detalleEliminar=Detalle.objects.get(id_ag=id_ag)
    detalleEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarDetalle(request,id_ag):
    detalleEditar=Detalle.objects.get(id_ag=id_ag)
    return render(request,'editarDetalle.html',{'detalle':detalleEditar})

def procesarActualizacionDetalle(request):
    id_ag=request.POST["id_ag"]
    fecha_ag=request.POST["fecha_ag"]
    hora_ag=request.POST["hora_ag"]
    total_ag=request.POST["total_ag"]
    notas_cliente=request.POST["notas_cliente"]
    #Insertando datos mediante el ORM de DJANGO
    detalleEditar=Detalle.objects.get(id_ag=id_ag)
    detalleEditar.fecha_ag=fecha_ag
    detalleEditar.hora_ag=hora_ag
    detalleEditar.total_ag=total_ag
    detalleEditar.notas_cliente=notas_cliente
    detalleEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')


# CREAR VISTA RECETAS
def listadoRecetas(request):
    recetasBdd=Receta.objects.all()
    return render(request, 'listadoRecetas.html', {'recetas':recetasBdd})


def guardarReceta(request):
    nombre_ag=request.POST["nombre_ag"]
    instrucciones_ag=request.POST["instrucciones_ag"]
    tiempo_preparacion_ag=request.POST["tiempo_preparacion_ag"]
    fecha_creacion_ag=request.POST["fecha_creacion_ag"]
    #Insertando datos mediante el ORM de django
    receta =Receta.objects.create(nombre_ag=nombre_ag,instrucciones_ag=instrucciones_ag,tiempo_preparacion_ag=tiempo_preparacion_ag,fecha_creacion_ag=fecha_creacion_ag)
    messages.success(request,'DATOS GUARDADOS EXITOSAMENTE')
    return redirect('/')


def eliminarReceta(request,id_ag):
    recetaEliminar=Receta.objects.get(id_ag=id_ag)
    recetaEliminar.delete()
    messages.success(request,'DATO ELIMINADO EXITOSAMENTE')
    return redirect('/')

def editarReceta(request,id_ag):
    recetaEditar=Receta.objects.get(id_ag=id_ag)
    return render(request,'editarReceta.html',{'receta':recetaEditar})

def procesarActualizacionReceta(request):
    id_ag=request.POST["id_ag"]
    nombre_ag=request.POST["nombre_ag"]
    instrucciones_ag=request.POST["instrucciones_ag"]
    tiempo_preparacion_ag=request.POST["tiempo_preparacion_ag"]
    fecha_creacion_ag=request.POST["fecha_creacion_ag"]
    #Insertando datos mediante el ORM de DJANGO
    recetaEditar=Receta.objects.get(id_ag=id_ag)
    recetaEditar.nombre_ag=nombre_ag
    recetaEditar.instrucciones_ag=instrucciones_ag
    recetaEditar.tiempo_preparacion_ag=tiempo_preparacion_ag
    recetaEditar.fecha_creacion_ag=fecha_creacion_ag
    recetaEditar.save()
    messages.success(request,
      'Datos ACTUALIZADOS Exitosamente')
    return redirect('/')
