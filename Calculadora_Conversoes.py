#Decimal para hexadecimal
def decimalParahexadecimal():
    x=int(input("coloque um numero na Base 10 para hexadecimal:"))
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

#decimal para octal
def decimalParaoctal():
    x=int(input("coloque um numero:"))

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
    x = int(input("Coloque um número :"))
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
    # Certifica-se de que a string binária tenha um comprimento múltiplo de 3
    while len(binario) % 3 != 0:
        binario = '0' + binario

    octal = ""
    i = 0

    while i < len(binario):
        # Pega grupos de 3 dígitos binários
        grupo = binario[i:i + 3]

        # Converte o grupo em um dígito octal
        dígito_octal = int(grupo, 2)

        # Adiciona o dígito octal ao resultado
        octal += str(dígito_octal)

        i += 3

    return octal

#binario para hexadecimal
def binarioParahexadecimal():
    while len(binario) % 4 != 0:
        binario = '0' + binario

    hexadecimal = ""
    i = 0

    while i < len(binario):
        grupo = binario[i:i + 4]

        dígito_hexadecimal = hex(int(grupo, 2))[2:]

        hexadecimal += dígito_hexadecimal

        i += 4

    return hexadecimal



#octal para decimal
def octalParadecimal():
    x=str(input("coloque um numero :"))
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
    # Primeiro, convertemos o número octal para decimal
    decimal = 0
    expoente = 0

    for digito in reversed():
        decimal += int(digito) * (8 ** expoente)
        expoente += 1

    # Em seguida, convertemos o decimal para hexadecimal
    hexadecimal = hex(decimal).replace("0x", "").upper()

    return hexadecimal

#octal para binario
def octalParabinario():
    # Mapeia cada dígito octal para seu equivalente binário de 3 bits
    octal_para_binario_dict = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }

    # Converte cada dígito octal em binário e concatena os resultados
    binario = ''.join(octal_para_binario_dict[digito] for digito in octal)

    # Remove os zeros à esquerda, exceto um zero se o número for zero
    binario = binario.lstrip('0')
    if not binario:
        binario = '0'

    return binario



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
    try:
        if hex_string.startswith('0x'):
            hex_string = hex_string[2:]

        decimal_number = int(hex_string, 16)

        binary_string = bin(decimal_number)[2:]

        return binary_string
    except ValueError:
        return "Entrada inválida. Certifique-se de fornecer uma string hexadecimal válida."

# #hexa para octal
def hexadecimalParaoctal():
    binary = bin(int(hexadecimal, 16))[2:]

    # Em seguida, completamos com zeros à esquerda para garantir que tenha um número inteiro de dígitos octais
    while len(binary) % 3 != 0:
        binary = '0' + binary

    # Agora, dividimos o número binário em grupos de 3 dígitos e convertemos cada grupo para octal
    octal = ''
    for i in range(0, len(binary), 3):
        octal_group = binary[i:i+3]
        octal_digit = str(int(octal_group, 2))
        octal += octal_digit

    return octal




# #decimal2 para octal
def decimalParaoctal2(x):
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
    print("Escolha uma opção:")

    print("1. Decimal para Binário")
    print("2. Decimal para Octal")
    print("3. Decimal para Hexadecimal")

    print("4. Binário para Decimal")
    print("5. Binário para Octal")
    print("6. Binário para Hexadecimal")

    print("7. Octal para Decimal")
    print("8. Octal para Hexadecimal")
    print("9. Octal para Binario")

    print("10. Hexadecimal para Decimal")
    print("11. Hexadecimal para Binario")
    print("12. Hexadecimal para Octal")

    # print("---EXCESSOES---")
    # print("13. Binario para Hexadecimal fração")
    # print("14. Decimal para Binario fração")

    print("Fechar")

    inputUser=str(input("Digite sua opção: "))

    if inputUser == "1":
        print("decimal para Binario")
        x=decimalParabinario()
        print("Seu resutado é ",x)

    elif inputUser=="2":
        print("decimal para transformar Base 8")
        x=decimalParaoctal()
        print("Seu resutado é ",x)

    elif inputUser=="3":
        print("decimal para hexadecimal")
        x=decimalParahexadecimal()
        print("Seu resutado é ",x)

    elif inputUser=="4":
        print("Binario para decimal")
        x=binarioParadecimal()
        print("Seu resutado é ",x)

    elif inputUser=="5":
        print("binario para octal")
        x=binarioParaoctal()
        print("dasd",x)
        print("Seu resutado é ",x)

    elif inputUser=="6":
        print("binario para hexadecimal")
        x=binarioParahexadecimal()
        print("Seu resutado é ",decimaParahexa2(x))

    elif inputUser=="7":
        print("Octal para decimal")
        x=octalParadecimal()
        print("Seu resutado é ",x)

    elif inputUser=="8":
        print("octal para hexadecimal")
        x=octalParahexadecimal()
        print("Seu resutado é ",x)

    elif inputUser=="9":
        print("octal para binario")
        x=octalParabinario()
        print("Seu resutado é ",x)

    elif inputUser=="10":
        print("hexadecimal para decimal")
        x=hexadecimalParadecimal()
        print("Seu resutado é ",x)

    elif inputUser=="11":
        print("hexadecimal para binario")
        x=hexadecimalParabinario()
        print("Seu resutado é ",x)

    elif inputUser=="12":
       print("hexadecimal para octal")
       x=hexadecimalParaoctal()
       print("Seu resutado é ",x)


    # elif inputUser=="13":
    #     print("binario para hexadecimal fração")
    #     g=str(input("coloque um numero: "))
    #     separados = g.split(',')
    #     x=binarioParadecimal2(separados[0])
    #     y=binarioParadecimal2(separados[1])
    #     lista=[x,",",y]
    #     resutado = ''.join(str(elemento) for elemento in lista)
    #     print("Seu resutado é ",resutado)

    # elif inputUser=="14":
    #     print("decimal fração para binario fração")
    #     g=str(input("coloque um numero: "))
    #     separados = g.split(',')
    #     x=decimalParabinario2(int(separados[0]))
    #     y=decimalParabinario2(int(separados[1]))
    #     lista=[x,",",y]
    #     resutado = ''.join(str(elemento) for elemento in lista)
    #     print("Seu resutado é ",resutado)

    elif inputUser=="sair":
        print("Desligado")
        break