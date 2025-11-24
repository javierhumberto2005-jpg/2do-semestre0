inv = []
cat = []    
factoss = []          
#definimoss
def agregarproducto(codigo, nombre, categoria, cantidad, precio): #crear productos
    for p in inv:
        if p["codigo"] == codigo:
            return "Error codigo repetido."
    if categoria not in cat:
        return f"Error la categoría '{categoria}' no existe. Primero creala."
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": int(cantidad),
        "precio": float(precio)
    }
    inv.append(producto)
    return "Producto agregado correctamente."
def editar_producto(codigo, Nnombre, Ncategoria, Ncantidad, Nprecio): #editar los productos creados
    for p in inv:
        if p["codigo"] == codigo:
            p["nombre"] = Nnombre
            p["categoria"] = Ncategoria
            p["cantidad"] = int(Ncantidad)
            p["precio"] = float(Nprecio)
            return "Producto actualizado."
    return "Error hay producto con ese codigo."
def Bproducto(codigo): #buscar productos
    for p in inv:
        if p["codigo"] == codigo:
            return p
    return None
def Cfactos(lista_compras): #crear facturas
    factos = []
    total_general = 0
    for codigo, cantidad in lista_compras:
        producto = Bproducto(codigo)
        if producto and producto["cantidad"] >= cantidad:
            subtotal = producto["precio"] * cantidad
            factos.append((producto["nombre"], cantidad, producto["precio"], subtotal))
            producto["cantidad"] -= cantidad  # Se descuenta del inv
            total_general += subtotal
        else:
            factos.append((f"Producto {codigo} no disponible", 0, 0, 0))
    factoss.append((factos, total_general))
    return factos, total_general
def obtener_inv(): #inventario
    return [(p["codigo"], p["nombre"], p["categoria"], p["cantidad"], p["precio"]) for p in inv]
def agregar_categoria(nombre): #crear categorias
    if nombre in cat:
        return "categoria existente."
    cat.append(nombre)
    return "Categoría crada."
def obtener_cat(): #categorias
    return cat
def obtfactoss(): #facturas
    return factoss