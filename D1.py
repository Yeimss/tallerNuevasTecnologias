productos=[]
bandera=1
while bandera:
    opcion=int(input("""
    --------MENU--------
    1. Ingresar producto.
    2. Mostrar productos.
    3. Buscar por codigo un producto para editar el precio.
    4. Eliminar por codigo un producto y eliminar el producto.
    0. salir
    """))

    if opcion==1:
        producto={}
        codigo=int(input("Ingrese el codigo del producto: "))
        nombre=input("Ingrese el nombre del procuto: ")
        precio=float(input("Ingrese el precio del producto: "))
        producto['codigo']=codigo
        producto['nombre']=nombre
        producto['precio']=precio
        productos.append(producto)

    elif opcion==2:
        print(productos)
        for i in productos:
            print(f"\n\ncodigo: {i['codigo']}")
            print(f"nombre: {i['nombre']}")
            print(f"precio: {i['precio']}\n")
    
    elif opcion==3:
        buscar=int(input("Ingrese el codigo: "))
        encontrado=False
        for i in productos:
            if i['codigo']==buscar:
                precio=float(input(f"Ingrese el nuevo precio del producto {i['nombre']}: "))
                i['precio']=precio
                print("Precio del producto modificado con exito")
                encontrado=True
        if not encontrado:
            print("No se encontro el producto")

    elif opcion==4:
        buscar=int(input("Ingrese el codigo: "))
        encontrado=False
        for i in productos:
            if i['codigo']==buscar:
                productos.pop(productos.index(i))
                print("Producto eliminado!!")
                encontrado=True

        if not encontrado:
            print("No se encontro el producto")

    elif opcion==0:
        bandera=0
    else:
        print("Opcion incorrecta >.<")


