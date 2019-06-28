# saldoActual = clientes[int(cuenta)]['cuenta']['saldo']
# clientes[int(cuenta)]['cuenta']['saldo'] = saldoActual + int(cantidad)

clientes = []
numCuentas = 0
saldo = 0


def crearCuenta(numCuentas):
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apelido: ')
    cuenta = {'nombre': nombre, 'apellido': apellido, 'cuenta': {'saldo': saldo, 'numeroCuenta': numCuentas}}
    clientes.append(cuenta)
    numCuentas += 1
    print("Cuenta creada")
    return clientes, numCuentas
crearCuenta(123)
#crearCuenta(543)


def realizarIngreso(clientes):
    if len(clientes) > 0:
        for cliente in clientes:
            cuenta = input('Por favor indique el número de la cuenta a depositar el dinero: ')
            cantidad = input('Por favor indique la cantidad a ingresar: ')
            if cliente['cuenta']['numeroCuenta'] == int(cuenta):
                saldoActual = cliente['cuenta']['saldo']
                cliente['cuenta']['saldo'] += saldoActual + int(cantidad)
                print('Se ha realizado el ingreso')
            else:
                print('Número de cuenta no existe')
    else:
        print('No hay clientes para ingresar valores')
#realizarIngreso(clientes)


def visualizarCuenta(clientes):
    if len(clientes) > 0:
        for cliente in clientes:
            print('Nombre: ' + cliente['nombre'])
            print('Apellido: ' + cliente['apellido'])
            print('Numero de cuenta: ' + str(cliente['cuenta']['numeroCuenta']))
            print(('Saldo actul: ' + str(cliente['cuenta']['saldo'])))
            print(('\n'))
    else:
        print('No sxisten cuentas para listar')
#visualizarCuenta(clientes)

def verSaldo(clientes):
    if len(clientes) > 0:
        cuenta = input("Por favor indique el número de cuenta: ")
        print('El saldo de la cuenta ' + int(cuenta) + 'es de: ' + int(clientes[int(cuenta)]['cuenta']['saldo']) + ' Euros')
    else:
        print('No existe cuentas')

verSaldo(clientes)