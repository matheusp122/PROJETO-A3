print("=== ANALISADOR FINANCEIRO ===\n")

while True:
    try:
        ativo_circulante = float(input("Ativo circulante: "))
        ativo_nao_circulante = float(input("Ativo NÃO circulante: "))
        passivo_circulante = float(input("Passivo circulante: "))
        passivo_nao_circulante = float(input("Passivo NÃO circulante: "))
        patrimonio_liquido = float(input("Patrimonio liquido: "))
        estoques = float(input("Estoques: "))
        receita = float(input("Receita: "))
        lucro = float(input("Lucro: "))

    except:
        print("Error... digite apenas números")
        continue

    ativo_total = ativo_circulante + ativo_nao_circulante
    passivo_total = passivo_circulante + passivo_nao_circulante

    if ativo_total != (passivo_total + patrimonio_liquido):
        print("Entrada rejeitada...\nOs dados passivo total + patrimonio liquido não é igual ao ativo total.")
        continue

    if passivo_circulante != 0:
        liquidez_corrente = ativo_circulante / passivo_circulante
    else:
        liquidez_corrente = 0

    if passivo_circulante != 0:
        liquidez_seca = (ativo_circulante - estoques) / passivo_circulante
    else:
        liquidez_seca = 0

    if ativo_total != 0:
        endividamento = (passivo_circulante + passivo_nao_circulante) / ativo_total
    else:
        endividamento = 0

    if receita != 0:
        margem_liquida = lucro / receita
    else:
        margem_liquida = 0
    
    if patrimonio_liquido != 0:
        roe = lucro / patrimonio_liquido
    else:
        roe = 0

    print("\n===== RELATÓRIO FINANCEIRO =====\n")
    print(f"Liquidez corrente:   {liquidez_corrente:.2f}")
    if liquidez_corrente > 1.0:
        print("✅ BOM --- tem mais dinheiro do que dívida!")
    elif liquidez_corrente >= 1.0:
        print("⚠️ ALERTA --- no limite")
    else:
        print("❌ PERIGO --- risco de não pagar dívidas")

    print(f"\nLiquidez seca:   {liquidez_seca:.2f}")
    if liquidez_seca > 1:
        print("✅ Muito boa")
    elif liquidez_seca == 1:
        print("⚠️ No limite")
    else:
        print("❌ Baixa")

    print(f"\nEndividamento:   {endividamento:.2f}")
    if endividamento < 0.5:
        print("✅ BOM --- saudável")
    elif endividamento <= 0.8:
        print("⚠️ ALERTA --- atenção")
    else:
        print("❌ PERIGO --- risco extremo")

    print(f"\nMargem líquida:   {margem_liquida:.2f}")
    if margem_liquida > 0:
        print("✅ BOM --- lucro")
    elif margem_liquida == 0:
        print("⚠️ ALERTA --- empate")
    else:
        print("❌ PERIGO --- prejuízo")

    print(f"\nROE:   {roe:.2f}")
    if roe > 0.20:
        print("EXCELENTE")
    elif roe > 0.10:
        print("BOM")
    elif roe > 0:
        print("FRACO")
    else:
        print("PREJUÍZO")

    opcao = str(input("\nDeseja analisar outra empresa? (s/n): ")).lower()
    if opcao != "s":
        print("Encerrando programa...")
        break