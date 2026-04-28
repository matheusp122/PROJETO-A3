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
        margem_liquida = estoques / receita
    else:
        margem_liquida = 0
    
    if patrimonio_liquido != 0:
        roe = lucro / passivo_circulante
    else:
        roe = 0

    #ÁREA QUE PRECISA DE ESTILIZAÇÃO
    #USAR EMOJIS E TAMBEM A TABELA DE CORES \033[m

    print("\n=== RELATÓRIO FINANCEIRO ===\n")
    print(f"Liquidez corrente:   {liquidez_corrente}")
    if liquidez_corrente < 1.0:
        print("Alerta --- risco de não pagar dívidas")
    else:
        print("Liquidez boa!")

    print(f"Liquidez seca:   {liquidez_seca}")

    print(f"Endividamento:   {endividamento}")
    if endividamento > 0.8:
        print("Risco extremo de endividamento")
    else:
        print("Endividamento controlado")

    print(f"Margem líquida:   {margem_liquida:.2f}")
    if margem_liquida < 0:
        print("Alerta de prejuízo!")
    else:
        print("Lucro garantido")

    print(f"ROE:   {roe:.2f}")
    if roe > 0.20:
        print("Otimo retorno!")
    else:
        print("Retorno abaixo do ideal")

    opcao = str(input("Deseja analisar outra empresa? (s/n): ")).lower()
    if opcao != "s":
        print("Encerrando programa...")
        break

    #https://github.com/matheusp122/PROJETO-A3.git