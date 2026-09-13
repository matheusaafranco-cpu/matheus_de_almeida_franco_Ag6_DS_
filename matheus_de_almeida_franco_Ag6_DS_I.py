# ============================================================
# Programa: Sistema de Desconto Progressivo
# Curso: Desenvolvimento de Sistemas - I (Agenda 6)
# ============================================================

def calcular_desconto():
    """
    Realiza o cálculo do desconto progressivo com base no valor digitado.
    """
    print("\n--- SISTEMA DE DESCONTO PROGRESSIVO ---")
    
    # Entrada de dados com tratamento para evitar erros de digitação
    try:
        valor_compra = float(input("Informe o valor total da compra (R$): "))
        
        # Validação para garantir que o valor não seja negativo
        if valor_compra < 0:
            print("Erro: O valor da compra não pode ser negativo.")
            return

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
        return

    # Aplicação das regras de desconto progressivo
    if valor_compra < 200.00:
        percentual_desconto = 0.05  # 5% de desconto
    elif valor_compra < 300.00:
        percentual_desconto = 0.10  # 10% de desconto
    else:
        percentual_desconto = 0.15  # 15% de desconto

    # Cálculo dos valores finais
    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    # Exibição dos resultados formatados em Moeda (R$)
    print("\n---------------- RESUMO DA COMPRA ----------------")
    print(f"Valor original:     R$ {valor_compra:.2f}")
    print(f"Desconto ({int(percentual_desconto * 100)}%):    R$ {valor_desconto:.2f}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
    print("--------------------------------------------------")


# Execução do programa com ciclo continuo
if __name__ == "__main__":
    while True:
        calcular_desconto()
        
        # Laço para validar se o usuário quer rodar novamente (apenas s ou n)
        while True:
            resposta = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()
            
            if resposta == 's':
                break  # Sai do laço interno e reinicia o cálculo
            elif resposta == 'n':
                print("\nPrograma encerrado. Até mais!")
                exit()  # Encerra a execução do script
            else:
                print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")