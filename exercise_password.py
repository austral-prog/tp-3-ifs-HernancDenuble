def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    papassword = input("")
    num_check = "0" in papassword or "1" in papassword or "2" in papassword or "3" in papassword or "4" in papassword or "5" in papassword or "6" in papassword or "7" in papassword or "8" in papassword or "9" in papassword

    if len(papassword) >= 8 and num_check == True:
        print("Contraseña valida")
    elif len(papassword) < 8 and num_check == True:
        print ("Contraseña muy corta")
    elif len(papassword) >= 8 and num_check == False:
        print ("Debe contener un numero")
    else:
        print ("Contraseña muy corta\nDebe contener un numero")

#password()