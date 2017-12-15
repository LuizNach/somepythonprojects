# HLB Biomath 2 - Modelo MBI
# Researchers: Sonia Ternes e Francisco Laranjeira
# Dev: Sonia Ternes, Luiz Nachtigall (PIBIC/CNPq), Matheus Galvao (PIBIC/CNPq)
# copy rights @Embrapa
# Date: Oct 2017

class Hospedeiro():
    def __init__(self, tipo=0, tupla=(-1, -1), status=0, idade=0, cap_cor=0, cap_max=0):
        self.tipo = tipo               # -1:removido  0:corredor 1:citrus 2:murraya
        self.coord = tupla             # posição (i,j) no pomar
        self.status = status           # estado epidemiológico
        self.idade = idade             # idade da planta
        # self.cap_cor = cap_cor         # capacidade de suporte corrente
        self.cap_max = cap_max         # capacidade de suporte máxima
        self.lista_ninfas = []         # ninfas localizadas no hospedeiro
        self.lista_adultos = []        # adultos localizados no hospedeiro

    def __str__(self):
        this_str = "Hospedeiro| "
        this_str += "Tipo: " + str(self.tipo) + "|"
        this_str += "Coord: " + str(self.coord) + '|'
        this_str += "Idade: " + str(self.idade) + '|'
        # this_str += "Cap_Corrente: " + str(self.cap_cor) + "|"
        this_str += "Cap_Max: " + str(self.cap_max) + "|"
        this_str += "List_Ninfa: " + str(len(self.lista_ninfas)) + "|"
        this_str += "List_Adulto: " + str(len(self.lista_adultos)) + "|"
        return this_str
