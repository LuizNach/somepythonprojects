# HLB Biomath 2 - Modelo MBI
# Researchers: Sonia Ternes e Francisco Laranjeira
# Dev: Sonia Ternes, Luiz Nachtigall (PIBIC/CNPq), Matheus Galvao (PIBIC/CNPq)
# copy rights @Embrapa
# Date: Oct 2017

class InsetoAdulto():
    def __init__(self, tupla, status, idade_cor, idade_max):
        self.coord = tupla
        self.status = status  # 0: não infectivo; 1: infectivo desde fase de ninfa; 2: infectivo fase adulta
        self.idade_cor = idade_cor
        self.idade_max = idade_max
        self.mark_death = 0
        self.mark_fly = 0

    def __str__(self):
        # print("\tinsetoAdulto",end="| ");
        # print("Coord: ",end='');print(self.coord,end='|');
        # print("Status: ", end='');print(self.status, end='|');
        # print("Idade Corre: ", end='');print(self.idade_corrente, end='|');
        # print("Idade Max: ", end='');print(self.idade_corrente_max,end='|');
        this_str = "\tinsetoAdulto| "
        this_str += "Coord: " + str(self.coord) + '|'
        this_str += "Status: " + str(self.status) + '|'
        this_str += "Idade Corre: " + str(self.idade_cor) + '|'
        this_str += "Idade Max: " + str(self.idade_max) + '|'
        return this_str

