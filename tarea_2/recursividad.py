
def integer_to_binary(n):
    
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return integer_to_binary(n//2) + str(n % 2)
    

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)
    

def get_square_root(n, guess=1.0):
    # Para calcular la raíz cuadrada de un número n, se puede usar el método de Newton
    if abs(guess * guess - n) < 0.0001:
        return guess
    else:
        return get_square_root(n, (guess + n / guess) / 2)
    

def roman_to_decimal(roman_number):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    
    if len(roman_number) == 0:
        return result
    
    if len(roman_number) == 1:
        return roman_numerals[roman_number]
    
    else:
        first_value = roman_numerals[roman_number[0]]
        second_value = roman_numerals[roman_number[1]]
        
        if first_value < second_value:
            result = second_value - first_value
            return result + roman_to_decimal(roman_number[2:])
        else:
            result = first_value
            return result + roman_to_decimal(roman_number[1:])
        

def sum_integers(n):
    if n == 1:
        return 1
    else:
        return n + sum_integers(n-1)


def menu():
    print("1. Convertir un número entero a binario")
    print("2. Contar los dígitos de un número")
    print("3. Calcular la raíz cuadrada de un número")
    print("4. Convertir un número romano a decimal")
    print("5. Sumar los n números enteros")
    print("6. Salir")
    option = int(input("Seleccione una opción: "))
    return option


def main():
    option = menu()
    while option != 6:
        if option == 1:
            n = int(input("Ingrese un número entero:"))
            print(f"\nEl número {n} en binario es: {integer_to_binary(n)}\n")
        elif option == 2:
            n = int(input("Ingrese un número entero: "))
            print(f"\nEl número {n} tiene {count_digits(n)} dígitos\n")
        elif option == 3:
            n = float(input("Ingrese un número: "))
            print(f"\nLa raíz cuadrada de {n} es: {get_square_root(n):.2f}\n")
        elif option == 4:
            roman_number = input("Ingrese un número romano: ")
            print(f"\nEl número romano {roman_number} en decimal es: {roman_to_decimal(roman_number)}\n")
        elif option == 5:
            n = int(input("Ingrese un número entero: "))
            print(f"\nLa suma de los primeros {n} números enteros es: {sum_integers(n)}\n")
        else:
            print("Opción no válida")
        option = menu()
    print("Fin del programa")
    
main()