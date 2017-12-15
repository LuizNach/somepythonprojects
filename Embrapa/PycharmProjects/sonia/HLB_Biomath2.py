# HLB Biomath 2 - Modelo MBI
# Researchers: Sonia Ternes e Francisco Laranjeira
# Dev: Sonia Ternes, Luiz Nachtigall (PIBIC/CNPq), Matheus Galvao (PIBIC/CNPq)
# copy rights @Embrapa
# Date: Oct 2017

from parametros import *

from hospedeiro import Hospedeiro
from ninfa import InsetoNinfa
from inseto import InsetoAdulto

import numpy as np
import random as rd

file_output = open("pomar_output.txt", 'w')

alteracoes_insetos = []
#
# Impressao das duas primeiras colunas para teste da distribuicao inicial de insetos
#
def print_inicio():

    for i in range(LINHAS_PLANTIO):
        for j in range(COLUNAS_PLANTIO):
            if j == 1 or j == 0:
                print(str(pomar[i, j]))
                for k in range(len(pomar[i, j].lista_adultos)):
                    print(str(pomar[i, j].lista_adultos[k]))
    # -------------------------------------------------------------------------------------------

#
# Grava arquivo contendo o estado do pomar
#
def grava_pomar():
    """ guardar o estado do pomar no dia no arquivo file_output"""
    for i in range(LINHAS_PLANTIO):
        for j in range(COLUNAS_PLANTIO):
            print(pomar[i, j], file=file_output)
            for inseto in pomar[i, j].lista_ninfas:
                print(inseto, file=file_output)
            for inseto in pomar[i, j].lista_adultos:
                print(inseto, file=file_output)

    print("\n#-------------------------------------------------------------------------------------------\n",
          file=file_output)
    # -------------------------------------------------------------------------------------------

#
# Inicializa populacao de insetos aleatoriamente nas duas primeiras na esquerda da area de plantio
# Porcentagem de insetos infectivos = pip
# Status infectivo: metade adquirido na fase de ninfa e metade na fase adulta
#
def inicia_populacao_insetos():

    for i in range(num_insetos_inicio):
        aux_col = rd.randrange(2)  # print(auxcolum)
        aux_lin = rd.randrange(LINHAS_PLANTIO)  # print(auxline)
        # aux_time = int(-1 * tau_a * np.log((rd.randrange(1, 1001)) / 1000));  # print(aux_time)
        idade_max = int(-1 * tau_a * np.log(uniforme[rd.randrange(dim_uniforme)]))
        if idade_max == 0:
            idade_max = 1

        # aux_infeccao = rd.randrange(1, 1000) / 1000;  # print(auxinfecao)
        aux_infeccao = uniforme[rd.randrange(0,dim_uniforme)]
        if aux_infeccao <= p_infeccao_primaria:
            aux_infeccao = uniforme[rd.randrange(0, dim_uniforme)]
            if aux_infeccao <= 0.5:
                # infectivo desde a fase de ninfa
                pomar[aux_lin, aux_col].lista_adultos.append(
                    InsetoAdulto((aux_lin, aux_col), 1, rd.randrange(1, idade_max + 1), idade_max))
            else:
                # infectivo a partir da fase adulta
                pomar[aux_lin, aux_col].lista_adultos.append(
                    InsetoAdulto((aux_lin, aux_col), 2, rd.randrange(1, idade_max + 1), idade_max))
        else:
            pomar[aux_lin, aux_col].lista_adultos.append(
                InsetoAdulto((aux_lin, aux_col), 0, rd.randrange(1, idade_max + 1), idade_max))

        # atualiza capacidade de suporte corrente
        # pomar[aux_lin, aux_col].cap_cor += 1; # nao precisa guardar a capacidade corrente
    # -----------------------------------------------------------------------------

#
# Infecçao do hospedeiro a partir dos insetos pousados nele
#
def hospedeiro_infeccao(lin, col):

    # Se planta já infectada, incrementa numero de dias no estado epidemiologico
    if pomar[lin, col].status > 0:
        pomar[lin, col].status += 1

    # Se planta suscetível, verifica infecção pelos insetos
    if pomar[lin, col].status == 0:

        for inseto in pomar[lin, col].lista_adultos:

            # Testa infecção por inseto que adquiriu a bacteria na fase de ninfa
            if inseto.status == 1:
                # aux_infeccao = rd.randrange(100) / 100;
                aux_infeccao = uniforme[rd.randrange(dim_uniforme)]
                if aux_infeccao <= p_hn:
                    pomar[lin, col].status = 1

            # Testa infecção por inseto que adquiriu a bacteria na fase adulta
            if inseto.status == 2:
                # aux_infeccao = rd.randrange(100) / 100;
                aux_infeccao = uniforme[rd.randrange(dim_uniforme)]
                if aux_infeccao <= p_ha:
                    pomar[lin, col].status = 1

            # Se planta foi infectada, desnecessário checar demais insetos
            if pomar[lin, col].status > 0:
                break


#
# Envelhecimento diario da planta
#
def hospedeiro_envelhecimento(lin, col):
    pomar[lin, col].idade+=1

#
# Remocao da planta a cada 3 meses: remove de ninfas e marca insetos para voo
#
def hospedeiro_remocao(lin, col, alteracoes_insetos):
    # Se hospedeiro é sintomatico, verifica probabilidade de deteccao
    aux_deteccao = uniforme[rd.randrange(dim_uniforme)]

    remove = False
    if aux_deteccao <= p_deteccao_campo:
        # Mata ninfas existentes
        pomar[lin, col].lista_ninfas.clear()  # ??? Luiz: correto?

        # Marca insetos para migrar e remove da planta
        for inseto in pomar[lin, col].lista_adultos:
            inseto.mark_fly = 1
            alteracoes_insetos.append(inseto) 

        #pomar[lin, col].lista_adultos.clear()   # ??? Luiz: Remove apenas da planta(i,j) (não afeta a lista de alteracoes)?
        pomar[lin, col].tipo = -1    # planta removida
        removeu = True

    return(remove)

#
# Verifica se quantidade de insetos na planta está acima da capacidade maxima
#
def hospedeiro_capacidade(lin, col, alteracoes_insetos):

    capacidade_corrente = len(pomar[lin, col].lista_adultos)
    if capacidade_corrente > pomar[lin, col].cap_max:
        excesso = capacidade_corrente - pomar[lin,col].cap_max

        # Marca insetos a mais para migrar, retira da planta e insere na lista de alterações
        for k in range(excesso):
            indice = rd.randrange(len(pomar[lin, col].lista_adultos))
            pomar[lin, col].lista_adultos[indice].mark_fly = 1
            # pomar[lin, col].list_adultos.remove(indice)  # não pode remover, pois ainda vai percorrer vetor de insetos
            # alteracoes_insetos.append(indice)
            alteracoes_insetos.append(pomar[lin, col].lista_adultos[indice])    # ??? Luiz: inserção esta correta?


#
# Aquisicao da bacteria pelo inseto adulto
#
def inseto_aquisicao(inseto):
    lin, col = inseto.coord

    if pomar[lin, col].status >= tau_l:     # doenca no hospedeiro ja passou da fase de latencia
        aux_infeccao = uniforme[rd.randrange(dim_uniforme)]
        if pomar[lin, col].tipo == 1:
            if aux_infeccao <= p_vc:    # inseto adquire de citros
                inseto.status = 2
        else:
            if pomar[lin, col].tipo == 2:
                if aux_infeccao <= p_vm:    # inseto adquire de murta
                    inseto.status = 2

#
# Verifica reproducao de inseto adulto, criando novas ninfas
#
def inseto_reproducao(inseto):
    (linha, coluna) = inseto.coord
    if len(pomar[linha,coluna].lista_adultos) < pomar[linha,coluna].cap_max:
        aux_prob = uniforme[rd.randrange(dim_uniforme)]
        if aux_prob <= razao_sex:   # eh femea, entao reproduz
            for num in range(num_ovos):
                aux_prob = uniforme[rd.randrange(dim_uniforme)]
                if (aux_prob <= p_sucesso):
                    pomar[linha,coluna].lista_ninfas.append(InsetoNinfa((linha,coluna), 0, 0, tau_n))


#
# Testa se inseto decide migrar com determinada probabilidade
def inseto_migracao(inseto, alteracoes_insetos):
    aux_migracao = uniforme[rd.randrange(dim_uniforme)]
    if aux_migracao <= p_voo:
        if not alteracoes_insetos.__contains__(inseto):
            inseto.mark_fly = 1
            alteracoes_insetos.append(inseto)

#
# Verifica se inseto atingiu na idade maxima (morte)
#
def inseto_morte(idx, inseto, alteracoes_insetos):
    lin, col = inseto.coord
    if inseto.idade_cor >= inseto.idade_max:
        inseto.mark_death = 1
        # pomar[lin, col].list_adultos.remove(idx)
        # alteracoes_insetos.append(idx)
        alteracoes_insetos.append(inseto)   # Luiz: conferir (idem hospedeiro_capacidade()

#
# Atualiza numero de dias na fase adulta
#
def inseto_envelhecimento(inseto):
    inseto.idade_cor += 1

#
# Migra um inseto específico, usando voo de Kobori
# Direções: norte = 0; sul = 1; oeste = 2; leste = 3
#
def move_adulto(inseto, count):
    (linha,coluna) = inseto.coord
    direcao = rd.randrange(4)  # sorteia direcao de voo.Obs: se fordentro do while(), inseto faz zig-zag

    voou = False
    while not voou:
        distancia = voo_kobori[rd.randrange(dim_voo)]  # sorteia distancia de voo

        if direcao == 0:
            # Norte: usa espaco_entre_linhas
            dist_voo = (int)(distancia/espaco_entre_linhas)  # quantidade de células a voar
            if dist_voo < 1:
                dist_voo = 1    # voa no mínimo para planta vizinha naquela direcao
            lin_voo = linha - dist_voo
            if lin_voo < 0:
                # inseto saiu do sistema pelo Norte
                count[0] += 1
                voou = True
            else:
                # se tipo > 0 (citros ou murta) e capacidade de suporte ok, emigra
                # se tipo > 0 e capacidade de suporte não ok ou tipo <= 0 procura nova planta
                if (pomar[lin_voo, coluna].tipo > 0) and (
                            len(pomar[lin_voo, coluna].lista_adultos) < pomar[lin_voo, coluna].cap_max):
                    inseto.coord = (lin_voo, coluna)  # atualiza posicao do inseto apos voo
                    pomar[lin_voo, coluna].lista_adultos.append(inseto)  # insere inseto no novo hospedeiro
                    voou = True
                else:
                    linha = lin_voo  # move inseto para "planta inexistente", para preparar novo voo
                    voou = False

        elif direcao == 1:
            # Sul: usa espaco_entre_linhas
            dist_voo = (int)(distancia / espaco_entre_linhas)  # quantidade de células a voar
            if dist_voo < 1:
                dist_voo = 1    # voa no mínimo para planta vizinha naquela direcao
            lin_voo = linha + dist_voo
            if lin_voo >= LINHAS_PLANTIO:
                # inseto saiu do sistema pelo Sul
                count[0] += 1
                voou = True
            else:
                # se tipo > 0 (citros ou murta) e capacidade de suporte ok, emigra
                # se tipo > 0 e capacidade de suporte não ok ou tipo <= 0 procura nova planta
                if (pomar[lin_voo, coluna].tipo > 0) and (
                            len(pomar[lin_voo, coluna].lista_adultos) < pomar[lin_voo, coluna].cap_max):
                    inseto.coord = (lin_voo, coluna)  # atualiza posicao do inseto apos voo
                    pomar[lin_voo, coluna].lista_adultos.append(inseto)  # insere inseto no novo hospedeiro
                    voou = True
                else:
                    linha = lin_voo
                    voou = False
        elif direcao == 2:
            # Oeste: usa espaco_entre_colunas
            dist_voo = (int)(distancia / espaco_entre_colunas)  # quantidade de células a voar
            if dist_voo < 1:
                dist_voo = 1  # voa no mínimo para planta vizinha naquela direcao
            col_voo = coluna - dist_voo
            if col_voo < 0:
                # inseto saiu do sistema pelo Oeste
                count[0] += 1
                voou = True
            else:
                # se tipo > 0 (citros ou murta) e capacidade de suporte ok, emigra
                # se tipo > 0 e capacidade de suporte não ok ou tipo <= 0 procura nova planta
                if (pomar[linha, col_voo].tipo > 0) and (
                            len(pomar[linha,col_voo].lista_adultos) < pomar[linha, col_voo].cap_max):
                    inseto.coord = (linha, col_voo)  # atualiza posicao do inseto apos voo
                    pomar[linha, col_voo].lista_adultos.append(inseto)  # insere inseto no novo hospedeiro
                    voou = True
                else:
                    coluna = col_voo
                    voou = False
        else:
            # Leste: usa espaco_entre_colunas
            dist_voo = (int)(distancia / espaco_entre_colunas)  # quantidade de células a voar
            if dist_voo < 1:
                dist_voo = 1  # voa no mínimo para planta vizinha naquela direcao
            col_voo = coluna + dist_voo
            if col_voo >= COLUNAS_PLANTIO:
                # inseto saiu do sistema pelo Leste
                count[0] += 1
                voou = True
            else:
                # se tipo > 0 (citros ou murta) e capacidade de suporte ok, emigra
                # se tipo > 0 e capacidade de suporte não ok ou tipo <= 0 procura nova planta
                if (pomar[linha, col_voo].tipo > 0) and (
                            len(pomar[linha, col_voo].lista_adultos) < pomar[linha, col_voo].cap_max):
                    inseto.coord = (linha, col_voo)  # atualiza posicao do inseto apos voo
                    pomar[linha, col_voo].lista_adultos.append(inseto)  # insere inseto no novo hospedeiro
                    voou = True
                else:
                    coluna = col_voo
                    voou = False

#
# Processa alteraçoes na lista de insetos ao final do dia da simulação
#
# OBS: insetos que vao migrar precisam voltara ter mark_fly = 0 (e mark_death = 0 ?
# retirar objeto da planta onde ele estava e inserir na nova planta
def executa_alteracoes(alteracoes_insetos, count):
    for inseto in alteracoes_insetos:
        (aux_linha, aux_coluna) = inseto.coord
        if inseto.mark_death == 1:
            inseto.mark_death = 0;
            print("chegou no death")
            count[0] += 1
            pomar[aux_linha, aux_coluna].lista_adultos.remove(inseto)  # ??? Luiz: vai remover da nova planta?
        else:
            if inseto.mark_fly == 1:
                print("chegou no fly")
                inseto.mark_fly = 0
                move_adulto(inseto, count)   # insere inseto na nova planta ou fora do sistema, conforme voo Kobori
                pomar[aux_linha,aux_coluna].lista_adultos.remove(inseto)    # ??? Luiz: vai remover da nova planta?
            else:
                # inseto inserido em alteracoes_inseto() de modo errado
                print("ERRO!")
                break

    alteracoes_insetos.clear()  # ??? Luiz: vai deletar os insetos que foram inseridos com append em move_adulto()?

#
# Implementar:
# 1) imigracao: para cada inseto que sai do sistema, um outro chega pelas plantas da borda
# 2) pop. minima: contabiliza mortes e se populacao final do dia é menor que inicial, faz chegar nvos insetos pela borda
#

def check_populacao_dia(count):
    pass

#
# Simulacao principal
#

def simulacao():

    # Distribui a populacao inicial de insetos nas colunas 1 e 2 da area de plantio
    inicia_populacao_insetos()

    # Imprime primeiras duas colunas do pomar
    print_inicio()

    # ??? Luiz porque não usou tempo_simulacao (ao inves de dias)?
    for dia in range(1,dias+1):

        # Grava em arquivo "fotografia" do pomar no dia corrente
        # Futuramente: fazer isso a cada 10 dias
        print("Dia: ", dia, file=file_output)
        grava_pomar()  # ??? Luiz: porque grava só um dia ?

        # Inicializa lista contendo alteracoes em insetos a serem efetivadas no final do dia
        # Verificar se sera necessario o mesmo tratamento para ninfa
        alteracoes_insetos = list()

        # Inicializa quantidade de insetos que deixarao o sistema no final do dia, para manter pop. minima
        count = [0,0]   # (count_emigra,count_morte)

        # -----o loop principal, avaliando cada hospedeiro no pomar
        for i in range(LINHAS_PLANTIO):
            for j in range(COLUNAS_PLANTIO):

                # Avalia somente citros e murta
                if pomar[i, j].tipo > 0:

                    #
                    # Processos relativos ao Hospedeiro
                    #
                    '''# debug print("dia "+str(dia))'''
                    '''#debug print("dias "+str(dias))'''
                    # Testa remocao a cada 90 dias
                    removeu = False;
                    if (dia % periodo_remocao == 0) :    # ?? Luiz: resto da divisao: porque segundo dia tem -1?
                        '''#debug print("Entrou na remocao: "+str(i)+' '+str(j)+' '+str(pomar[i, j].tipo))'''
                        removeu = hospedeiro_remocao(i, j, alteracoes_insetos)
                        '''#debug print("Entrou na remocao: "+str(i)+' '+str(j)+' '+str(pomar[i, j].tipo))'''
                        '''#debug input()'''
                    # Executa demais eventos para planta não removida
                    if not removeu:
                        hospedeiro_infeccao(i, j)

                        hospedeiro_capacidade(i, j, alteracoes_insetos)

                        hospedeiro_envelhecimento(i, j)


                    #
                    # Processos relativos às Ninfas
                    #
                    # pensar nos insetos novos criados na maturidade de ninfas (total da populacao)

                    for ninfa in pomar[i, j].lista_ninfas:
                        pass

                    #
                    # Processos relativos ao Inseto Adulto
                    #
                    for idx, inseto in enumerate(pomar[i, j].lista_adultos):
                        # pensar nas repeticoes do vetor alteracoes_insetos

                        if inseto.status == 0:
                            inseto_aquisicao(inseto)

                        inseto_reproducao(inseto)

                        inseto_migracao(inseto, alteracoes_insetos)

                        inseto_morte(idx, inseto, alteracoes_insetos)   # talvez retirar idx

                        inseto_envelhecimento(inseto)

        #
        # Processa alterações marcadas nos Insetos e Ninfas (final do dia)
        #
        executa_alteracoes(alteracoes_insetos, count)   # ok
        # apos execucao, limpar os 3 parametros desta desta funcao

        #
        # Executa processos externos ao sistema: a) garantir pop. minima de insetos (usar count_emigra e count_morte)
        check_populacao_dia(count)
        #

    # -------------------------------------------------------------------------------------------

if __name__ == "__main__":

    #
    # Inicializa pomar
    # Obs: preparada para area de plantio contendo 9 pomares dispostos numa matriz 3 x 3
    #
    if cenario == 0:
        # Cenario 0 = teste: um pomar 20x48 com citros
        for i in range(LINHAS_PLANTIO):
            for j in range(COLUNAS_PLANTIO):
                pomar.append(Hospedeiro(tipo=1, tupla=(i, j), idade=IDADE_HOSPEDEIRO, cap_max=capacidade[rd.randrange(dim_capacidade)]))

    elif cenario == 1:
        # Cenario 1: nove pomares 20x48 cada um, com citros
        for i in range(LINHAS_PLANTIO):
            for j in range(COLUNAS_PLANTIO):
                # insere citros
                pomar.append(Hospedeiro(tipo=1, tupla=(i, j), idade=IDADE_HOSPEDEIRO, cap_max=capacidade[rd.randrange(dim_capacidade)]))

    elif cenario == 2:
        # Cenario 2: 9 pomares 20x48 cada, murta nas bordas externas da area toda e citros nas demais posicoes
        for i in range(LINHAS_PLANTIO):
            for j in range(COLUNAS_PLANTIO):

                if i == 0 or i == (LINHAS_PLANTIO-1) or j == 0 or j == (COLUNAS_PLANTIO - 1):
                    # Murraya
                    pomar.append(Hospedeiro(tipo=2, tupla=(i, j), idade=IDADE_HOSPEDEIRO,
                                            cap_max=capacidade[rd.randrange(dim_capacidade)]))
                else:
                    if i == LINHAS_PLANTIO or i == (2*LINHAS_PLANTIO + 1) or j == COLUNAS_PLANTIO or j == (2*COLUNAS_PLANTIO + 1):
                        # Corredor
                        pomar.append(Hospedeiro(tipo=0, tupla=(i, j)))
                    else:
                        # Citros
                        pomar.append(Hospedeiro(tipo=1, tupla=(i, j), idade=IDADE_HOSPEDEIRO,
                                                cap_max=capacidade[rd.randrange(dim_capacidade)]))
    else:
        # Cenario 3: 9 pomares 20x48 cada,murta nas bordas de cada talhao e citros nas demais posicoes
        for i in range(LINHAS_PLANTIO):
            for j in range(COLUNAS_PLANTIO):

                if i == 0 or i == (LINHAS_PLANTIO - 1) or i == (LINHAS_PLANTIO + 1) or \
                                i == (2*LINHAS_PLANTIO - 1) or i == (2*LINHAS_PLANTIO + 1) or \
                                j == 0 or j == (COLUNAS_PLANTIO - 1) or j == (COLUNAS_PLANTIO + 1) or \
                                j == (2*COLUNAS_PLANTIO - 1) or j == (2*COLUNAS_PLANTIO + 1):
                    # Murraya
                    pomar.append(Hospedeiro(tipo=2, tupla=(i, j), idade=IDADE_HOSPEDEIRO,
                                            cap_max=capacidade[rd.randrange(dim_capacidade)]))
                else:
                    if i == LINHAS_PLANTIO or i == (2*LINHAS_PLANTIO + 1) or j == COLUNAS_PLANTIO or \
                                    j == (2*COLUNAS_PLANTIO + 1):
                        # Corredor
                        pomar.append(Hospedeiro(tipo=0, tupla=(i, j)))
                    else:
                        # Citros
                        pomar.append(Hospedeiro(tipo=1, tupla=(i, j), idade=IDADE_HOSPEDEIRO,
                                                cap_max=capacidade[rd.randrange(dim_capacidade)]))

    # coloca a matriz do pomar sob a forma matricial indexada
    pomar = np.array(pomar, dtype=Hospedeiro).reshape(LINHAS_PLANTIO, COLUNAS_PLANTIO)

    # Inicia o looping de simulacao principal
    simulacao()
