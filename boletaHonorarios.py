# cálculo de valores para una boleta de honorarios

retencion2022 = 12.25
retencion2023 = 13
retencion2024 = 13.75
retencion2025 = 14.5
retencion2026 = 15.25
retencion2027 = 16
retencion2028 = 17
anoRetencion = input("En que año estamos: ")
tipoBoleta = input("¿Ingresará un valor bruto o líquido? (ingrese la letra b ó l): ")


if tipoBoleta == 'l':
    valorLiquido = input("Ingrese el valor líquido de la Boleta: ")
    if anoRetencion == "2022":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2022))
    elif anoRetencion == "2023":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2023))
    elif anoRetencion == "2024":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2024))
    elif anoRetencion == "2025":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2025))
    elif anoRetencion == "2026":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2026))
    elif anoRetencion == "2027":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2027))
    elif anoRetencion == "2028":
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2028))
    else:
        valorBruto = (int(valorLiquido) * 100) / (100 - float(retencion2028))
    print("El valor bruto de la boleta es: " + str(float(valorBruto)))
    
elif tipoBoleta == "b":
    valorBruto = input("Ingrese el valor bruto de la Boleta: ")
    if anoRetencion == "2022":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2022))) / 100
    elif anoRetencion == "2023":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2023))) / 100
    elif anoRetencion == "2024":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2024))) / 100
    elif anoRetencion == "2025":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2025))) / 100
    elif anoRetencion == "2026":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2026))) / 100
    elif anoRetencion == "2027":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2027))) / 100
    elif anoRetencion == "2028":
        valorLiquido = (int(valorBruto) * (100 - float(retencion2028))) / 100
    else:
        valorLiquido = (int(valorBruto) * (100 - float(retencion2028))) / 100
    print("El valor líquido de la boleta es: " + str(float(valorLiquido)))
else:
    print("Error, vuelva a ejecutar el programa")









