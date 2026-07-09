from fastapi import FastApi

def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

def decimal_to_octal(decimal_num):
    return oct(decimal_num)[2:]

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:].upper()

def from_decimal(decimal_num, target_system):
    if target_system == "binario":
        return decimal_to_binary(decimal_num)
    elif target_system == "octal":
        return decimal_to_octal(decimal_num)
    elif target_system == "hexadecimal":
        return decimal_to_hexadecimal(decimal_num)
    else:
        return "Sistema numérico de destino no válido"

def to_decimal(num, source_system):
    if source_system == "binario":
        return int(num, 2)
    elif source_system == "octal":
        return int(num, 8)
    elif source_system == "hexadecimal":
        return int(num, 16)
    else:
        return "Sistema numérico de origen no válido"

def main():
    cantidad = input("Ingrese la cantidad a convertir: ")
    sistema_origen = input("Ingrese el sistema numérico de la cantidad (binario, octal, hexadecimal o decimal): ").lower()

    if sistema_origen == "decimal":
        cantidad_decimal = int(cantidad)
    else:
        cantidad_decimal = to_decimal(cantidad, sistema_origen)

    sistema_destino = input("Ingrese el sistema numérico de destino (binario, octal, hexadecimal o decimal): ").lower()

    resultado = from_decimal(cantidad_decimal, sistema_destino)

    print(f"El resultado de la conversión es: {resultado}")

if __name__ == "__main__":
    main()