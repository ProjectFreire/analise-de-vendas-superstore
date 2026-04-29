import pandas as pd
import matplotlib.pyplot as plt


caminho = 'dados/train.csv'
# Estrutura geral
df=pd.read_csv(caminho)

# Estatísticas básicas
print("\n=== ESTATÍSTICAS ===")
print(df.describe())

# Nome das colunas
print("\n=== COLUNAS ===")
print(df.columns)

#converter datas 
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

#criar coluna de tempo de entrega
df['Delivery Time'] = (df['Ship Date'] - df['Order Date']).dt.days

#verificar valores nulos
print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

print("=== INFORMAÇÕES ===")
print(df.info())

# Vendas por região
vendas_regiao = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

print("\n=== VENDAS POR REGIÃO ===")
print(vendas_regiao)



# Gráfico de vendas por região
vendas_regiao.plot(kind='bar')

plt.title('Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas')

# Salvar imagem
plt.savefig('imagens/vendas_por_regiao.png')

plt.show()

# Vendas por Região e Categoria
vendas_categoria = df.groupby(['Region', 'Category'])['Sales'].sum().sort_values(ascending=False)

print("\n=== VENDAS POR REGIÃO E CATEGORIA ===")
print(vendas_categoria)

# Vendas por Subcategoria
vendas_subcategoria = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)

print("\n=== VENDAS POR SUBCATEGORIA ===")
print(vendas_subcategoria)

# Top 10 subcategorias
top10 = vendas_subcategoria.head(10)

top10.plot(kind='bar')

plt.title('Top 10 Subcategorias por Vendas')
plt.xlabel('Subcategoria')
plt.ylabel('Total de Vendas')

plt.xticks(rotation=45)

plt.savefig('imagens/top10_subcategorias.png')

plt.show()

print("\n=== TEMPO DE ENTREGA ===")
print(df['Delivery Time'].describe())

# Classificar tempo de entrega
def classificar_entrega(dias):
    if dias <= 2:
        return 'Rápido'
    elif dias <= 5:
        return 'Médio'
    else:
        return 'Lento'

df['Tipo Entrega'] = df['Delivery Time'].apply(classificar_entrega)

# Vendas por tipo de entrega
vendas_entrega = df.groupby('Tipo Entrega')['Sales'].sum().sort_values(ascending=False)

print("\n=== VENDAS POR TIPO DE ENTREGA ===")
print(vendas_entrega)

# Gráfico tipo de entrega
vendas_entrega.plot(kind='bar')

plt.title('Vendas por Tipo de Entrega')
plt.xlabel('Tipo de Entrega')
plt.ylabel('Total de Vendas')

plt.savefig('imagens/vendas_tipo_entrega.png')

plt.show()