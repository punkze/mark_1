#La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones.

nombre = input("Ingrese su nombre: ")
comision = float(input("Cuanto vendio este mes?: "))
print(f"Trabajador:{nombre}\nSu comision:${comision*0.13}\nSueldo Total:${(comision*0.13)+comision}")

