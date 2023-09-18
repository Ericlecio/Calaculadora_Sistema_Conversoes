import tkinter as tk
# decimal para octal


def decimalParabinario():
    x = int(entry.get())
    resultado_binario = ""

    if x == 0:
        resultado_binario = "0"
    else:
        while x > 0:
            resultado_binario = str(x % 2) + resultado_binario
            x = x // 2

    resultado.set(resultado_binario)

# decimal para octal


def decimalParaoctal():

    x = int(entry.get())
    resultado_octal = oct(x).replace("0o", "")
    resultado.set(resultado_octal)

# Decimal para hexadecimal


def decimalParahexadecimal():
    x = int(entry.get())
    resultado_hexadecimal = hex(x).replace("0x", "").upper()
    resultado.set(resultado_hexadecimal)


# Configuração da janela
window = tk.Tk()
window.title("Conversor de Bases")

# Entrada de texto
entry_label = tk.Label(window, text="Digite um número decimal:")
entry_label.pack()

entry = tk.Entry(window)
entry.pack()

# Botões de conversão
convert_button_binario = tk.Button(
    window, text="Decimal para Binário", command=decimalParabinario)
convert_button_binario.pack()

convert_button_octal = tk.Button(
    window, text="Decimal para Octal", command=decimalParaoctal)
convert_button_octal.pack()

convert_button_hexadecimal = tk.Button(
    window, text="Decimal para Hexadecimal", command=decimalParahexadecimal)
convert_button_hexadecimal.pack()

# Resultado da conversão
resultado = tk.StringVar()
result_label = tk.Label(window, textvariable=resultado)
result_label.pack()

# Loop principal da interface gráfica
window.mainloop()
