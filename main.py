import SQLconnection

cursor = SQLconnection.db.cursor()

buscar_ruta = False
ingreso_camion = False
ingreso_chofer = False
ingreso_acoplado = False
ingreso_carga = False
ingreso_ruta = False
lista_chofer = False
lista_camion = False
lista_ruta = False
buscar_chofer = False
seguir = True
total_id = 0

while seguir:
    print("----- Menú principal -----")
    print("1. Introducir Camion\n2. Introducir Chofer\n3. Introducir Acoplado")
    print("4. Introducir Carga\n5. Introducir Hoja de ruta\n6. Ver choferes")
    print("7. Ver camiones\n8. Ver hojas de ruta\n9. Buscar chofer")
    print("10. Buscar hoja de ruta\n11. Salir")
    pregunta = int(input('Que desea realizar?: '))

    if pregunta == 1:
        ingreso_camion = True
    if pregunta == 2:
        ingreso_chofer = True
    if pregunta == 3:
        ingreso_acoplado = True
    if pregunta == 4:
        ingreso_carga = True
    if pregunta == 5:
        ingreso_ruta = True
    if pregunta == 6:
        lista_chofer = True
    if pregunta == 7:
        lista_camion = True
    if pregunta == 8:
        lista_ruta = True
    if pregunta == 9:
        buscar_chofer = True
    if pregunta == 10:
        buscar_ruta = True
    if pregunta == 11:
        seguir = False

    while ingreso_camion:
        # ////////////////////////INGRESO CAMION////////////////////////

        sql = 'INSERT INTO camion(patente, modelo_fk,acoplado_fk) values (%s, %s, %s);'

        patente = str(input('Ingrese patente : '))

        cursor.execute('''
        select modelo.ID, modelo.NOMBRE, fabricante.NOMBRE as 'Fabricante' from modelo
        JOIN fabricante on modelo.FABRICANTE_FK = fabricante.ID;
        ''')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        modelo = int(input('Ingrese id del modelo: '))

        cursor.execute('select * from vista_acoplado')

        resultado = cursor.fetchall()

        print('PATENTE  |  ACOPLADO  |   DESCRIPCION')

        for x in resultado:
            print(x)

        acoplado = str(input('Ingrese placa del acoplado[Sensible a mayusculas]: '))

        val = (patente, modelo, acoplado)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        print('...Camion ingresado con exito...\n')

        pregunta = str(input('Desea ingresar otro camion?[S/n]'))

        if pregunta.upper() == 'S':
            ingreso_camion = True
        else:
            ingreso_camion = False

    # ////////////////////////INGRESO CHOFER////////////////////////
    while ingreso_chofer:

        sql = 'INSERT INTO chofer VALUES (%s, %s, %s, %s, %s);'

        rut = str(input('Ingrese RUT: '))

        nombre = str(input('Ingrese nombre: '))

        apellido = str(input('Ingrese apellido: '))

        edad = int(input('Ingrese edad: '))

        while edad <= 0:
            print('<...Ingrese valores positivos...>')
            edad = int(input('Ingrese edad: '))

        licencia = str(input('Ingrese tipo de licencia: '))

        val = (rut, nombre, apellido, edad, licencia)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        print('...Chofer ingresado con exito...\n')

        pregunta = str(input('Desea ingresar otro chofer?[S/n]'))

        if pregunta.upper() == 'S':
            ingreso_chofer = True
        else:
            ingreso_chofer = False

    # ////////////////////////INGRESO ACOPLADO////////////////////////
    while ingreso_acoplado:
        sql = 'INSERT INTO acoplado VALUES (%s, %s, %s);'

        patente = str(input('Ingrese patente: '))

        cursor.execute('SELECT * FROM tipo_ac;')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        tipo_ac = int(input('Ingrese id del tipo de acoplado: '))

        cursor.execute('SELECT * FROM carga;')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        carga = int(input('Ingrese id de la carga: '))

        val = (patente, tipo_ac, carga)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        print('...Acoplado ingresado con exito...\n')

        pregunta = str(input('Desea ingresar otro acoplado?[S/n]'))

        if pregunta.upper() == 'S':
            ingreso_acoplado = True
        else:
            ingreso_acoplado = False

    # ////////////////////////INGRESO CARGA////////////////////////
    while ingreso_carga:
        sql = "insert into CARGA(DESCRIPCION) values (%s)"

        desc = input("Introduzca una descripción: ")

        cursor.execute(sql, (desc, ))
        SQLconnection.db.commit()
        print('...Carga ingresada con exito...\n')

        pregunta = str(input('Desea ingresar otra carga?[S/n]'))

        if pregunta.upper() == 'S':
            ingreso_carga = True
        else:
            ingreso_carga = False
    # ////////////////////////INGRESO RUTA////////////////////////
    while ingreso_ruta:
        sql = "insert into RUTA(DETALLE, FECHA, CHOFER_FK, CAMION_FK, ORIGEN_FK, DESTINO_FK) values (%s, %s, %s, %s, %s, %s)"

        deta = input("Detalles de la ruta: ")
        fech = input("Fecha: ")
        # ********DESPLEGAR LISTA DE CHOFERES********
        cursor.execute("select * from vista_chofer;")

        resultado = cursor.fetchall()

        print('RUT   |   NOMBRE   |   LICENCIA')

        for x in resultado:
            print(x)
        chof = input("Rut del chofer a cargo: ")
        # ********DESPLEGAR LISTA DE CAMIONES********
        cursor.execute('SELECT * FROM VISTA_CAMION')

        resultado = cursor.fetchall()

        print('PATENTE  |  MARCA Y MODELO')

        for x in resultado:
            print(x)
        cami = input("Patente del camión: ")
        # ********DESPLEGAR LISTA DE LOCACIONES********
        cursor.execute('SELECT * FROM locacion;')

        resultado = cursor.fetchall()

        print('ID | DIRECCION')

        for x in resultado:
            print(x)
        orig = input("ID origen: ")
        dest = input("ID destino: ")
        val = (deta, fech, chof, cami, orig, dest)

        cursor.execute(sql, val)
        SQLconnection.db.commit()

        print('...Ruta ingresada con exito...\n')
        pregunta = str(input('Desea ingresar otra ruta?[S/n]'))

        if pregunta.upper() == 'S':
            ingreso_ruta = True
        else:
            ingreso_ruta = False
        # ////////////////////////LISTA CHOFERES////////////////////////
    if lista_chofer is True:
        cursor.execute("select * from vista_chofer;")

        resultado = cursor.fetchall()

        print(' RUT   |    NOMBRE    |  LICENCIA  ')

        for x in resultado:
            print(x)

        continuar = input('Presione Enter para continuar...')

        lista_chofer = False
        # ////////////////////////LISTA CAMIONES////////////////////////
    if lista_camion is True:
        cursor.execute('SELECT * FROM VISTA_CAMION')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        continuar = input('Presione Enter para continuar...')

        lista_camion = False
    # ////////////////////////LISTA RUTAS////////////////////////
    if lista_ruta is True:
        cursor.execute('SELECT * FROM vista_ruta_2')

        resultado = cursor.fetchall()

        print('FOLIO|RUT | PATENTE |             ORIGEN             |             DESTINO             |         DETALLE')

        for x in resultado:
            print(x)

        continuar = input('Presione Enter para continuar...')

        lista_ruta = False
    # ////////////////////////BUSCAR CHOFER////////////////////////
    while buscar_chofer:
        sql = "select rut, CONCAT(nombre,' ',apellido), edad, licencia from CHOFER where RUT = (%s)"

        rut = input("Introduzca rut del chofer: ")

        cursor.execute(sql, (rut, ))

        result = cursor.fetchall()

        print(' RUT   |   NOMBRE   |EDAD|  LICENCIA  ')

        for x in result:
            print(x)

        pregunta = str(input('Desea buscar otro chofer?[S/n]'))

        if pregunta.upper() == 'S':
            buscar_chofer = True
        else:
            buscar_chofer = False
    # ////////////////////////BUSCAR HOJA////////////////////////
    while buscar_ruta:

        sql = '''SELECT * FROM vista_ruta WHERE FOLIO = (%s)'''

        fol = input("Introduzca el número de folio: ")

        print('ID |   FECHA    |NOMBRE CONDUCTOR|PLACA CAMION|       ORIGEN       |     DESTINO     ')

        cursor.execute(sql, (fol,))
        result = cursor.fetchall()

        for x in result:
            print(x)

        pregunta = str(input('Desea ingresar otra hoja de ruta?[S/n]'))

        if pregunta.upper() == 'S':
            buscar_ruta = True
        else:
            buscar_ruta = False
print('\n...Hasta luego!...')
