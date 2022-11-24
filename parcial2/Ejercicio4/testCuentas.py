from Cuentas import Cuenta_Bancaria, Cuenta_Joven

usuario = Cuenta_Bancaria("10542980", "Jaime Salazar")
joven = Cuenta_Joven("11007845", "Santiago Ortiz")
usuario.ingresar_cantidad(8000)
joven.ingresar_cantidad(-1200) #valor erróneo
joven.ingresar_cantidad(3000)
usuario.retirar_cantidad(6000) #error supera máximo reintegro
usuario.retirar_cantidad(3500)
joven.retirar_cantidad(4500) #error supera saldo
print(f"Cuenta: {usuario.get_numero_cuenta()}  Titular: {usuario.get_nombre_titular()} Saldo: {usuario.get_saldo()}  Número de operaciones: {usuario.get_numero_operaciones()}")
print(f"Cuenta: {joven.get_numero_cuenta()}  Titular: {joven.get_nombre_titular()} Saldo: {joven.get_saldo()}  Número de operaciones: {joven.get_numero_operaciones()}")