#Decimal para hexadecimal
def decimalParahexadecimal():
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    lista = []
    while x > 0:
        a = x % 16
        x = x // 16
        if a <= 9:
            lista.append(str(a))
        elif a == 10:
            lista.append("a")
        elif a == 11:
            lista.append("b")
        elif a == 12:
            lista.append("c")
        elif a == 13:
            lista.append("d")
        elif a == 14:
            lista.append("e")
        elif a == 15:
            lista.append("f")
    
    lista.reverse()
    resultado = ''.join(lista)
    return resultado

#decimal para octal
def decimalParaoctal():
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    lista=[]
    while x>0:
        a=x%8
        x=x//8
        lista.append(a)
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado

#decimal para binario
def decimalParabinario():
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    lista = []
    while x > 0:
        a = x % 2
        x = x // 2
        lista.append(a)
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    resultado = '{:0>4}'.format(resultado)
    return resultado


#Binario para decimal
def binarioParadecimal():
    x=str(input("coloque um numero: "))
    if not x.isdigit() or any(digit not in '01' for digit in x):
        print("Entrada inválida. Por favor, insira apenas números binários.")
        return "NONE"
    
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=2**g
        x=item*y
        resutado.append(x)

    resutado.reverse()
    return sum(resutado)

#binario para octal
def binarioParaoctal():
    x=str(input("coloque um numero: "))
    if not x.isdigit() or any(digit not in '01' for digit in x):
        print("Entrada inválida. Por favor, insira apenas números binários.")
        return "NONE"
    
    while len(x) % 3 != 0:
        x = '0' + x

    octal = ""
    i = 0

    while i < len(x):
        grupo = x[i:i + 3]
        dígito_octal = int(grupo, 2)
        octal += str(dígito_octal)
        i += 3
    return octal

#binario para hexadecimal
def binarioParahexadecimal():
    x=str(input("coloque um numero: "))
    if not x.isdigit() or any(digit not in '01' for digit in x):
        print("Entrada inválida. Por favor, insira apenas números binários.")
        return "NONE"

    while len(x) % 4 != 0:
        x = '0' + x
    hexadecimal = ""
    i = 0

    while i < len(x):
        grupo = x[i:i + 4]
        dígito_hexadecimal = hex(int(grupo, 2))[2:]
        hexadecimal += dígito_hexadecimal
        i += 4
    return hexadecimal


#octal para decimal
def octalParadecimal():
    x = input("Digite um número octal: ")
    if not x.isdigit() or any(int(digit) >= 8 for digit in x):
        print("Entrada inválida. Digite apenas números inteiros na base 8.")
        return NONE   
    lista=[]
    resutado=[]
    for caractere in x:
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=8**g
        x=item*y
        resutado.append(x)

    resutado.reverse()
    return sum(resutado)

#octal para hexadecimal
def octalParahexadecimal():
    x = input("Digite um número octal: ")
    if not x.isdigit() or any(int(digit) >= 8 for digit in x):
        print("Entrada inválida. Digite apenas números inteiros na base 8.")
        return NONE 
    
    decimal = 0
    expoente = 0
    x = x[::-1]
    for digito in x:
        decimal += int(digito) * (8 ** expoente)
        expoente += 1

    digitosHexadecimais = "0123456789ABCDEF"
    resultadoHexadecimal = ""

    while decimal > 0:
        resto = decimal % 16
        resultadoHexadecimal = digitosHexadecimais[resto] + resultadoHexadecimal
        decimal //= 16

    return resultadoHexadecimal

#octal para binario
def octalParaBinario():
    x = input("Digite um número octal: ")
    if not x.isdigit() or any(int(digit) >= 8 for digit in x):
        print("Entrada inválida. Digite apenas números inteiros na base 8.")
        return NONE
    resultadoBinario = ""

    for dígito in x:
        valorOctal = int(dígito)
        binário = ""
        
        for i in range(2, -1, -1):
            if valorOctal >= 2**i:
                binário += "1"
                valorOctal -= 2**i
            else:
                binário += "0"
        resultadoBinario += binário
    resultadoBinario = resultadoBinario.lstrip('0')

    if resultadoBinario == "":
        resultadoBinario = "0"
    return resultadoBinario


#hexa para decimal
def hexadecimalParadecimal():
    x=str(input("coloque um numero: "))
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
        else:
            lista.append(caractere)
    for i in range(len(lista)):
        if lista[i] in ["a", "A"]:
            lista[i] = 10
        elif lista[i] in ["b", "B"]:
            lista[i] = 11
        elif lista[i] in ["c", "C"]:
            lista[i] = 12
        elif lista[i] in ["d", "D"]:
            lista[i] = 13
        elif lista[i] in ["e", "E"]:
            lista[i] = 14
        elif lista[i] in ["f", "F"]:
            lista[i] = 15
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=16**g
        x=item*y
        resutado.append(x)
    return sum(resutado)

#hexa para binario
def hexadecimalParabinario():
    x=str(input("coloque um numero: "))
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
        else:
            lista.append(caractere)
    for i in range(len(lista)):
        if lista[i] in ["a", "A"]:
            lista[i] = 10
        elif lista[i] in ["b", "B"]:
            lista[i] = 11
        elif lista[i] in ["c", "C"]:
            lista[i] = 12
        elif lista[i] in ["d", "D"]:
            lista[i] = 13
        elif lista[i] in ["e", "E"]:
            lista[i] = 14
        elif lista[i] in ["f", "F"]:
            lista[i] = 15
    a=0
    resultadoBinario = ""

    for dígito in lista:
        valorHexadecimal = int(dígito)
        binário = ""
        for i in range(3, -1, -1):
            if valorHexadecimal >= 2**i:
                binário += "1"
                valorHexadecimal -= 2**i
            else:
                binário += "0"

        resultadoBinario += binário
    resultadoBinario = resultadoBinario.lstrip('0')

    if resultadoBinario == "":
        resultadoBinario = "0"

    return resultadoBinario

# #hexa para octal
def hexadecimalParaOctal(numeroHexadecimal):
    # Dicionário para mapear dígitos hexadecimais para binário
    hexa_para_binario = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Converter o número hexadecimal em binário
    binario = ""
    for digito in numeroHexadecimal:
        binario += hexa_para_binario.get(digito, '')

    # Adicionar zeros à esquerda para garantir que a representação tenha múltiplos de 3 dígitos
    while len(binario) % 3 != 0:
        binario = '0' + binario

    # Converter o binário em octal agrupando em grupos de 3 dígitos
    octal = ""
    for i in range(0, len(binario), 3):
        grupo = binario[i:i+3]
        octal += str(int(grupo, 2))

    return octal

def inputHexadecimal():
        while True:
            entrada = input("Digite um número hexadecimal: ")
            entrada = entrada.upper()
            if all(digito in '0123456789ABCDEF' for digito in entrada):
                return hexadecimalParaOctal(entrada)
            else:
                print("Entrada inválida. Por favor, digite um número hexadecimal válido.")


# #decimal2 para octal
def decimalParaoctal2(x):
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    lista=[]
    while x>0:
        a=x%8
        x=x//8
        lista.append(a)
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado

#Decimal para hexadecimal2
def decimaParahexa2(x):
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    lista=[]
    while x>0:
        a=x%16
        x=x//16
        if a<=9:
            lista.append(a)
        elif a==10:
            lista.append("a")
        elif a==11:
            lista.append("b")
        elif a==12:
            lista.append("c")
        elif a==13:
            lista.append("d")
        elif a==14:
            lista.append("e")
        elif a==15:
            lista.append("f")
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado

#binario fraçao decimal
def binarioParadecimal2(x):
    x=str(input("coloque um numero: "))
    if not x.isdigit() or any(digit not in '01' for digit in x):
        print("Entrada inválida. Por favor, insira apenas números binários.")
        return "NONE"
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=2**g
        x=item*y
        resutado.append(x)

    resutado.reverse()
    return sum(resutado)

#decimal fração
def decimalParabinario2(x):
    while True:
        try:
            x = int(input("Coloque um número na Base 10 para hexadecimal: "))
            if x >= 0:
                break
            else:
                print("Por favor, insira um número inteiro não negativo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    lista = []
    while x >0:
        a = x % 2
        x = x // 2
        lista.append(a)
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    resultado = '{:0>4}'.format(resultado)
    return resultado


while True:
    print("                             ")
    print("CALCULADORA DE CONVERSÕES DE BASES NUMERICAS")
    print("Escolha uma das opções:")
    print("-"*35)
    print("                             ")
    print("1. Decimal para Binário")
    print("2. Decimal para Octal")
    print("3. Decimal para Hexadecimal")
    print("-"*35)
    print("                             ")
    print("4. Binário para Decimal")
    print("5. Binário para Octal")
    print("6. Binário para Hexadecimal")
    print("-"*35)
    print("                             ")
    print("7. Octal para Decimal")
    print("8. Octal para Hexadecimal")
    print("9. Octal para Binario")
    print("-"*35)
    print("                             ")
    print("10. Hexadecimal para Decimal")
    print("11. Hexadecimal para Binario")
    print("12. Hexadecimal para Octal")
    print("                             ")
    print("---------EXCESSOES-----------")
    print("13. Binario para Hexadecimal fração")
    print("14. Decimal para Binario fração")
    print("-"*35)
    print("Sair")

    inputUser=str(input("Digite sua opção: "))

    if inputUser == "1":
        print("Decimal para Binario")
        x=decimalParabinario()
        print("O Resultado é: ",x)

    elif inputUser=="2":
        print("Decimal para Octal")
        x=decimalParaoctal()
        print("O Resultado é: ",x)

    elif inputUser=="3":
        print("Decimal para Hexadecimal")
        x=decimalParahexadecimal()
        print("O Resultado é: ",x)

    elif inputUser=="4":
        print("Binario para Decimal")
        x=binarioParadecimal()
        print("O Resultado é: ",x)

    elif inputUser=="5":
        print("Binario para Octal")
        x=binarioParaoctal()
        print("dasd",x)
        print("O Resultado é: ",x)

    elif inputUser=="6":
        print("Binario para Hexadecimal")
        x=binarioParahexadecimal()
        print("O Resultado é:" , x)

    elif inputUser=="7":
        print("Octal para Decimal")
        x=octalParadecimal()
        print("O Resultado é: ",x)

    elif inputUser=="8":
        print("Octal para Hexadecimal")
        x=octalParahexadecimal()
        print("O Resultado é: ",x)

    elif inputUser=="9":
        print("Octal para Binario")
        x=octalParaBinario()
        print("O Resultado é: ",x)

    elif inputUser=="10":
        print("Hexadecimal para Decimal")
        x=hexadecimalParadecimal()
        print("O Resultado é: ",x)

    elif inputUser=="11":
        print("Hexadecimal para Binario")
        x=hexadecimalParabinario()
        print("O Resultado é: ",x)

    elif inputUser=="12":
       print("Hexadecimal para Octal")
       x=inputHexadecimal()
       print("O Resultado é: ",x)

    elif inputUser=="13":
        print("Binario para Hexadecimal fração")
        g=str(input("coloque um numero: "))
        separados = g.split(',')
        x=binarioParadecimal2(separados[0])
        y=binarioParadecimal2(separados[1])
        lista=[x,",",y]
        resutado = ''.join(str(elemento) for elemento in lista)
        print("O Resutado é: ",resutado)

    elif inputUser=="14":
        print("Decimal fração para Binario fração")
        g=str(input("coloque um numero: "))
        separados = g.split(',')
        x=decimalParabinario2(int(separados[0]))
        y=decimalParabinario2(int(separados[1]))
        lista=[x,",",y]
        resutado = ''.join(str(elemento) for elemento in lista)
        print("O Resutado é: ",resutado)

    elif inputUser=="Sair" or "sair":
        print("Obrigado por utilizar")
        break