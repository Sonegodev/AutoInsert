import pandas as pd

arquivo_csv = 'caminhoDoArquivo.csv'

df = pd.read_csv(arquivo_csv, dtype=str, sep=';')

colunas = [
    'coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5',
    'coluna 6', 'coluna 7', 'coluna 8', 'coluna 9', 'coluna 10',
    'coluna 11', 'coluna 12', 'coluna 13', 'coluna 14', 'coluna 15',
    'coluna 16', 'coluna 17', 'coluna 18', 'coluna 19', 'coluna 20'
]

df = df[colunas]

arquivo_sql = 'insert_dados.sql'

with open(arquivo_sql, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        valores = []
        for valor in row:
            if pd.isna(valor):
                valores.append('NULL')
            else:
                valor_limpo = str(valor).replace("'", "''")
                valores.append(f"'{valor_limpo}'")
        linha_insert = f"INSERT INTO #Dados ({', '.join(colunas)}) VALUES ({', '.join(valores)});\n"
        f.write(linha_insert)

print(f"arquvio '{arquivo_sql}' feito com sucesso com {len(df)} INSERTs.")

# sql auto insert
# teste