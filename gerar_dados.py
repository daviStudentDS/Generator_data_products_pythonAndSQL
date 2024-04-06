import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Função para gerar uma data aleatória
def random_date(start, end):
    return start + timedelta(
        seconds=np.random.randint(0, int((end - start).total_seconds()))
    )

# Parâmetros de geração
num_items = 50000
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

# Gerando os dados
data = {
    "ID_Produto": np.random.randint(1, 10000, num_items), # Supondo que temos 10.000 produtos
    "Quantidade": np.random.randint(1, 10, num_items),
    "Preco_Unitario": np.round(np.random.uniform(10, 100, num_items), 2),
    "Data_Venda": [random_date(start_date, end_date) for _ in range(num_items)]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando no arquivo CSV
df.to_csv("vendas_produtos.csv", index=False)