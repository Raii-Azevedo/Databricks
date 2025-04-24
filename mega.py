import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re

# Nome do arquivo com os dados brutos
input_file = 'MEGA.txt'

# Função para processar o arquivo e extrair os números
def process_file(file):
    # Abrir o arquivo e processar linha por linha
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # Lista para armazenar os números sorteados
    data = []
    
    for line in lines:
        # Usar regex para capturar os números após os dois-pontos
        match = re.search(r': (.+)', line)
        if match:
            # Remover espaços em excesso e caracteres indesejados como '.' antes de converter
            numbers = [int(num.strip().replace('.', '')) for num in match.group(1).split(',')]
            data.append(numbers)
    
    # Criar um DataFrame com os dados processados
    df = pd.DataFrame(data, columns=['N1', 'N2', 'N3', 'N4', 'N5', 'N6'])
    return df

# Processar o arquivo e carregar os dados
df = process_file(input_file)

# Consolidar todos os números sorteados em uma única lista
all_numbers = df.values.flatten()

# Contar a frequência de cada número
number_counts = Counter(all_numbers)

# Ordenar os números mais frequentes
most_common_numbers = number_counts.most_common(6)

# Exibir os resultados
print("Números mais prováveis de acordo com a análise histórica:")
for num, count in most_common_numbers:
    print(f"Número: {num}, Frequência: {count}")

# Plotando um gráfico de frequências (opcional)
import matplotlib.pyplot as plt

# Ordenar todos os números por frequência
sorted_counts = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)
numbers, frequencies = zip(*sorted_counts)

plt.bar(numbers, frequencies, color='skyblue')
plt.xlabel('Números')
plt.ylabel('Frequência')
plt.title('Frequência de Números Sorteados')
plt.show()
