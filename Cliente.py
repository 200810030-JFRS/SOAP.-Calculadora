from zeep import Client

wsdl_url = "http://127.0.0.1:8000/?wsdl"

try:
    cliente = Client(wsdl_url)
    print("Cliente conectado al WSDL", wsdl_url)

    resultado_suma = cliente.service.sumar(5, 5)
    print("Resultado de la suma:", resultado_suma)

    resultado_resta = cliente.service.restar(5, 5)
    print("Resultado de la resta:", resultado_resta)

    resultado_multiplicacion = cliente.service.multiplicador(8, 2) 
    print("Resultado de la multiplicación:", resultado_multiplicacion)

    resultado_division = cliente.service.dividir(6, 7)
    print("Resultado de la división:", resultado_division)

    try:
        resultado_division_cero = cliente.service.dividir(6, 0)
        print("Resultado de la división por cero:", resultado_division_cero)
    except Exception as e:
        print("Error al dividir por cero:", e)

except Exception as e:
    print("Error al conectar con el WSDL:", e)
    exit(1)