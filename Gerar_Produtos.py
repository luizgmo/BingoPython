import random

# Declarar vetores
nome_vetor = []
estoque_vetor = []
estoque_min_vetor = []
estoque_max_vetor = []
preco_custo_vetor = []
preco_venda_vetor = []
porcentagem_icms_vetor = []
porcentagem_ip_vetor = []

# Gerar os valores e colocar nos vetores
for i in range(10):
    numero = random.randint(1,100)
    nome = "Produto" + str(numero)
    nome_vetor.append(nome)
    
    estoque = random.randint(1,100)
    estoque_vetor.append(estoque)
    
    estoque_min = random.randint(1,100)
    estoque_min_vetor.append(estoque_min)
    
    estoque_max_vetor = [random.randint(valor, 100) for valor in estoque_min_vetor]

    preco_custo = random.randint(0,1000)
    preco_custo_vetor.append(preco_custo)

    preco_venda_vetor = [random.randint(valor + 1,1000) for valor in preco_custo_vetor]
    
    # Calcula o lucro subtraindo o preço de venda do preço de custo
    vetor_lucro = [venda - custo for venda, custo in zip(preco_venda_vetor, preco_custo_vetor)]
    
    porcentagem_icms = random.randint(1,100)
    porcentagem_icms_vetor.append(porcentagem_icms)

    porcentagem_ip = random.randint(1,100)
    porcentagem_ip_vetor.append(porcentagem_ip)
 
    print("Nome: ", nome_vetor)
    print("")

    print("Estoque       : ", estoque_vetor)
    print("Estoque Mínimo: ", estoque_min_vetor)
    print("Estoque Máximo: ", estoque_max_vetor)
    print("")

    print("Preço de custo: ", preco_custo_vetor)
    print("Preço de venda: ", preco_venda_vetor)
    print("Lucro total   : ", vetor_lucro)
    print("")

    print("Porcentagem de ICMS: ", porcentagem_icms_vetor)
    print("Porcentagem de IP  : ", porcentagem_ip_vetor)
    print("") 
    
# Descobrir o nome dos produtos que aparecerão na tabela
max_preco_nome = nome_vetor[preco_venda_vetor.index(max(preco_venda_vetor))]
min_preco_nome = nome_vetor[preco_venda_vetor.index(min(preco_venda_vetor))]

max_estoque_nome = nome_vetor[estoque_vetor.index(max(estoque_vetor))]
min_estoque_nome = nome_vetor[estoque_vetor.index(min(estoque_vetor))]

max_icms_nome = nome_vetor[porcentagem_icms_vetor.index(max(porcentagem_icms_vetor))]
min_icms_nome = nome_vetor[porcentagem_icms_vetor.index(min(porcentagem_icms_vetor))]

max_lucro_nome = nome_vetor[vetor_lucro.index(max(vetor_lucro))]
min_lucro_nome = nome_vetor[vetor_lucro.index(min(vetor_lucro))]



print("Produto de maior preço: ", max_preco_nome ,  "// R$", max(preco_venda_vetor))
print("Produto de menor preço: ", min_preco_nome ,  "// R$", min(preco_venda_vetor))
print("Produto com maior estoque: ", max_estoque_nome, "//", max(estoque_vetor))
print("Produto com menor estoque: ", min_estoque_nome, "//", min(estoque_vetor))
print("Produto com o maior ICMS: ", max_icms_nome, "//", max(porcentagem_icms_vetor), "%")
print("Produto com o menor ICMS: ", min_icms_nome, "//", min(porcentagem_icms_vetor), "%")
print("Produto com maior lucro: ", max_lucro_nome, "// R$", max(vetor_lucro))
print("Produto com menor lucro: ", min_lucro_nome, "// R$", min(vetor_lucro))
