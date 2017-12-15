# HLB Biomath 2 - Modelo MBI
# Researchers: Sonia Ternes e Francisco Laranjeira
# Dev: Sonia Ternes, Luiz Nachtigall (PIBIC/CNPq), Matheus Galvao (PIBIC/CNPq)
# copy rights @Embrapa
# Date: Oct 2017

import numpy as np
import random as rd

#
# Parâmetros provenientes da interface grafica
#
anos = 5     # tempo de simulação em anos
tempo_simulacao = 360*anos   #tempo de simulação em dias

tau_l = 30   # tempo de duracao da fase de latencia na planta: 30 ou 60 dias
tau_i = 180  # tempo de duracao da fase de incubacao na planta: 180 a 540 dias

p_deteccao_campo = 0.476    # 0 ou 0.476 por dia
p_infeccao_primaria = 0.30  # regiao baixa incidência: 0.01; média: 0.15; alta: 0.30 por dia

proporcao_psilideos = 0.41  # 0.41 ou 5 psilideos por planta no inicio da simulacao

cenario = 0     # Cenario a ser simulado: 0 (teste), 1 (citros), 2 (citros+murta tipo 1) ou 3 (citros+murta tipo 2)

#
# Constantes
#

LINHAS_TALHAO = 20   # Número de linhas no talhão: 20
COLUNAS_TALHAO = 42  # Número de colunas no talhão: 42

quantidade_talhoes = 1  # Número de talhoes na simulacao (matriz quadrada)
talhoes_em_linha = (int)(np.sqrt(quantidade_talhoes))

LINHAS_PLANTIO = talhoes_em_linha*LINHAS_TALHAO + talhoes_em_linha - 1       # Total de linhas na area de plantio
COLUNAS_PLANTIO = talhoes_em_linha*COLUNAS_TALHAO + talhoes_em_linha - 1     # Total de colunas na area de plantio

IDADE_HOSPEDEIRO = 6*360    # Idade das plantas hospedeiras


#
# Parametros biológicos fixos
#

tau_n = 17  # tempo maximo de duracao da fase ovo+ninfa (dias)
tau_a = 32  # expectativa de vida do inseto adulto (dias)

p_voo = 0.739        # prob. inseto decidir voar (por dia)
p_sucesso = 0.921    # sucesso fase ovo+ninfa (por dia)
p_morte = 1 - p_sucesso

p_ha = 0.035    # prob. infeccao hospedeiro por inseto  infectivo na fase adulta (por dia)
p_hn = 0.67     # prob. infeccao hospedeiro por inseto infectivo desde fase ninfa (por dia)
p_vc = 0.43     # prob. aquisicao de inseto adulto em citros (por dia)
p_vm = 0.18     # prob. aquisicao de inseto adulto em murta (por dia)
p_nc = 0.94     # prob. aquisicao de ninfa em citros (por dia)
p_nm = 0.39     # prob. aquisicao de ninfa em murta (por dia)

num_ovos = 15         # numero medio de ovos por femea (por dia)
razao_sex = 0.556     # razao sexual da especie

periodo_remocao = 90    # inspecao no campo a cada 3 meses

distancia_voo_kobori = 5.5263  # media de distancia de voo de acordo com Kobori

espaco_entre_linhas = 6
espaco_entre_colunas = 4

#
# Outras variaveis globais
#
pomar = []   # representa a matriz da área de plantio

dias = 3  # 10*360     #simulacao correra 150 ciclos; #?? ver com Luiz

num_plantas_inicio = LINHAS_PLANTIO*COLUNAS_PLANTIO
num_insetos_inicio = int(0.05*proporcao_psilideos*num_plantas_inicio)
num_insetos_corrente = num_insetos_inicio

#
# Geração do vetor de capacidade de suporte: Normal(media, desvio)
#
media = 100
desvio = 15

dim_capacidade = 12     # uma capacidade de suporte para cada mês do ano

capacidade = list(range(dim_capacidade))
for i in range(dim_capacidade):
    capacidade[i] = int(rd.normalvariate(media, desvio))

#
# Geração do vetor de distribuição Uniforme
#
dim_uniforme = 100000

uniforme = list(range(dim_uniforme))
for i in range(dim_uniforme):
    uniforme[i] = rd.uniform(0, 1)

#
# Geração do vetor contendo distâncias de voo seguindo Kobori
#

dim_voo = 10000
voo_kobori = list(range(dim_voo))
for i in range(dim_voo):
    voo_kobori[i] = -1*distancia_voo_kobori*np.log(uniforme[rd.randrange(dim_uniforme)])
