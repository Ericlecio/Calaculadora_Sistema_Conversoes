import tkinter as tk

def decimalParaBase(x, base):
    lista = []
    while x > 0:
        a = x % base
        x = x // base
        if a <= 9:
            lista.append(a)
        else:
            lista.append(chr(ord('A') + a - 10))
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    return resultado
def abrir_tela_decimal(base):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(f"Tela Decimal para Base {base}")
    nova_janela.geometry("500x500")

    
    label = tk.Label(nova_janela, text=f"Escolha uma das opções para Base {base}")
    decimal_button = tk.Button(nova_janela, text=f"Decimal para Base {base}", command=lambda: converterParaBase(base))
    
    label.pack()
    decimal_button.pack()
    
    result_label = tk.Label(nova_janela, text="")
    result_label.pack()
    
    entry = tk.Entry(nova_janela)
    entry.pack()
    
    def converterParaBase(base):
        x = int(entry.get())
        resultado = decimalParaBase(x, base)
        result_label.config(text=resultado)


def hexadecimalParaBase(hexadecimal, base):
    decimal = 0
    for digit in hexadecimal:
        if '0' <= digit <= '9':
            decimal = decimal * 16 + int(digit)
        elif 'A' <= digit <= 'F':
            decimal = decimal * 16 + ord(digit) - ord('A') + 10
        else:
            raise ValueError("Hexadecimal inválido")

    lista = []
    while decimal > 0:
        a = decimal % base
        decimal = decimal // base
        if a <= 9:
            lista.append(a)
        else:
            lista.append(chr(ord('A') + a - 10))
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    return resultado
def abrir_tela_hexadecimal(base):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(f"Tela Hexadecimal para Base {base}")
    nova_janela.geometry("500x500")

    label = tk.Label(nova_janela, text=f"Escolha uma das opções para Base {base}")
    decimal_button = tk.Button(nova_janela, text=f"Hexadecimal para Base {base}", command=lambda: converterParaBase(base))
    
    label.pack()
    decimal_button.pack()
    
    result_label = tk.Label(nova_janela, text="")
    result_label.pack()
    
    entry = tk.Entry(nova_janela)
    entry.pack()
    
    def converterParaBase(base):
        hexadecimal = int(entry.get())
        resultado = decimalParaBase(hexadecimal, base)
        result_label.config(text=resultado)


def binarioParaBase(binario, base):
    # Converte o número binário para decimal
    decimal = int(binario, 2)
    
    # Usa a função decimalParaBase para converter o número decimal para a base desejada
    resultado = decimalParaBase(decimal, base)
    
    return resultado
def abrir_tela_binario(base):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(f"Tela Binario para Base {base}")
    nova_janela.geometry("500x500")

    label = tk.Label(nova_janela, text=f"Escolha uma das opções para Base {base}")
    decimal_button = tk.Button(nova_janela, text=f"Binario para Base {base}", command=lambda: converterParaBase(base))
    
    label.pack()
    decimal_button.pack()
    
    result_label = tk.Label(nova_janela, text="")
    result_label.pack()
    
    entry = tk.Entry(nova_janela)
    entry.pack()
    
    def converterParaBase(base):
        binario = int(entry.get())
        resultado = decimalParaBase(binario, base)
        result_label.config(text=resultado)


def octalParaBase(octal, base):
    decimal = 0
    for digit in octal:
        decimal = decimal * 8 + int(digit)
    
    lista = []
    while decimal > 0:
        a = decimal % base
        decimal = decimal // base
        if a <= 9:
            lista.append(str(a))
        else:
            lista.append(chr(ord('A') + a - 10))
    
    lista.reverse()
    resultado = ''.join(lista)
    return resultado
def abrir_tela_octal(base):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(f"Tela Octal para Base {base}")
    nova_janela.geometry("500x500")

    label = tk.Label(nova_janela, text=f"Escolha uma das opções para Base {base}")
    decimal_button = tk.Button(nova_janela, text=f"Octal para Base {base}", command=lambda: converterParaBase(base))
    
    label.pack()
    decimal_button.pack()
    
    result_label = tk.Label(nova_janela, text="")
    result_label.pack()
    
    entry = tk.Entry(nova_janela)
    entry.pack()
    
    def converterParaBase(base):
        octal = int(entry.get())
        resultado = decimalParaBase(octal, base)
        result_label.config(text=resultado)


root = tk.Tk()
root.title("CONVERSOR DE BASES NUMERICAS")
root.geometry("1000x1000")

b1 = tk.Button(root, text="Decimal para Hexadecimal", command=lambda: abrir_tela_decimal(16))
b1.grid(row=1, column=6, padx=20, pady=20)

b2 = tk.Button(root, text="Decimal para Octal", command=lambda: abrir_tela_decimal(8))
b2.grid(row=1, column=7, padx=20, pady=20)

b3 = tk.Button(root, text="Decimal para Binario", command=lambda: abrir_tela_decimal(2))
b3.grid(row=1, column=8, padx=20, pady=20)



b4 = tk.Button(root, text="Binario para Hexadecimal", command=lambda: abrir_tela_binario(16))
b4.grid(row=2, column=6, padx=20, pady=20)

b5 = tk.Button(root, text="Binario para Octal", command=lambda: abrir_tela_binario(8))
b5.grid(row=2, column=7, padx=20, pady=20)

b6 = tk.Button(root, text="Binario para Decimal", command=lambda: abrir_tela_binario(10))
b6.grid(row=2, column=8, padx=20, pady=20)



b7 = tk.Button(root, text="Octal para Hexadecimal", command=lambda: abrir_tela_octal(16))
b7.grid(row=3, column=6, padx=20, pady=20)

b8 = tk.Button(root, text="Octal para Decimal", command=lambda: abrir_tela_octal(10))
b8.grid(row=3, column=7, padx=20, pady=20)

b9 = tk.Button(root, text="Octal para Binario", command=lambda: abrir_tela_octal(2))
b9.grid(row=3, column=8, padx=20, pady=20)



b10 = tk.Button(root, text="Hexadecimal para Octal", command=lambda: abrir_tela_hexadecimal(8))
b10.grid(row=4, column=6, padx=20, pady=20)

b11 = tk.Button(root, text="Hexadecimal para Decimal", command=lambda: abrir_tela_hexadecimal(10))
b11.grid(row=4, column=7, padx=20, pady=20)

b12 = tk.Button(root, text="Hexadecimal para Binario", command=lambda: abrir_tela_hexadecimal(2))
b12.grid(row=4, column=8, padx=20, pady=20)



root.mainloop()