import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Localiza a base junto ao programa para evitar caminhos específicos do computador.
pasta_projeto = Path(__file__).resolve().parent
arquivo_dados = pasta_projeto / "Tabela4.csv"

# Leitura da tabela: ponto e vírgula separa as colunas e vírgula representa os decimais.
dados = pd.read_csv(
    arquivo_dados,
    sep=";",
    decimal=",",
    encoding="latin1",
    header=1
)

# Organização inicial da tabela.
dados = dados.dropna(axis=1, how="all")
dados.columns = dados.columns.astype(str).str.strip()

# Identifica automaticamente as colunas que representam anos.
colunas_ano = [col for col in dados.columns if col.isnumeric()]
dados[colunas_ano] = dados[colunas_ano].apply(pd.to_numeric, errors="coerce")

print("Período analisado:", ", ".join(colunas_ano))
print("Total de unidades federativas:", len(dados))

# Ranking do IDH registrado em 2024.
ranking_2024 = (
    dados[["Sigla", "Estado", "2024"]]
    .sort_values(by="2024", ascending=False)
    .reset_index(drop=True)
)

print("\nIDH de 2024 por unidade federativa:")
print(ranking_2024.to_string(index=False))

# Calcula a variação do indicador entre o primeiro e o último ano da análise.
dados["variacao_idh"] = dados["2024"] - dados["1991"]
maior_avanco = dados.loc[dados["variacao_idh"].idxmax()]

print("\nMaior crescimento entre 1991 e 2024:")
print(f"Estado: {maior_avanco['Estado']} ({maior_avanco['Sigla']})")
print(f"1991: {maior_avanco['1991']:.3f}")
print(f"2024: {maior_avanco['2024']:.3f}")
print(f"Variação: {maior_avanco['variacao_idh']:.3f}")

# Verifica se alguma unidade apresentou queda no indicador.
quedas = dados.loc[
    dados["variacao_idh"] < 0,
    ["Sigla", "Estado", "1991", "2024", "variacao_idh"]
]

if quedas.empty:
    print("\nNenhuma unidade federativa apresentou queda no período.")
else:
    print("\nUnidades com queda:")
    print(quedas.to_string(index=False))

# Converte a tabela para o formato adequado às séries temporais.
identificadores = [col for col in dados.columns if col not in colunas_ano]
serie = dados.melt(
    id_vars=identificadores,
    value_vars=colunas_ano,
    var_name="Ano",
    value_name="IDH"
)

serie["Ano"] = serie["Ano"].astype(int)
serie["IDH"] = pd.to_numeric(serie["IDH"], errors="coerce")

# Série histórica de Minas Gerais.
serie_mg = (
    serie.loc[serie["Sigla"].eq("MG")]
    .sort_values("Ano")
)

fig, eixo = plt.subplots(figsize=(10, 6))
eixo.plot(
    serie_mg["Ano"],
    serie_mg["IDH"],
    marker="o",
    linewidth=2
)
eixo.set(
    title="Evolução do IDH — Minas Gerais",
    xlabel="Ano",
    ylabel="IDH"
)
eixo.set_ylim(0.3, 0.9)
eixo.grid(alpha=0.3)
fig.tight_layout()
plt.show()

# Comparação da evolução de todas as unidades federativas.
fig, eixo = plt.subplots(figsize=(12, 7))

for sigla, grupo in serie.groupby("Sigla"):
    grupo = grupo.sort_values("Ano")
    eixo.plot(
        grupo["Ano"],
        grupo["IDH"],
        marker="o",
        markersize=3,
        linewidth=1.5,
        label=sigla
    )

eixo.set(
    title="Evolução do IDH das Unidades Federativas (1991–2024)",
    xlabel="Ano",
    ylabel="IDH"
)
eixo.set_ylim(0.3, 0.9)
eixo.legend(
    ncol=3,
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    title="UF"
)
fig.tight_layout()
plt.show()
