# HLB Biomath 2 - Modelo MBI
# Researchers: Sonia Ternes e Francisco Laranjeira
# Dev: Sonia Ternes, Luiz Nachtigall (PIBIC/CNPq), Matheus Galvao (PIBIC/CNPq)
# copy rights @Embrapa
# Date: Oct 2017

class InsetoNinfa():
    def __init__(self, tupla, status, idade_cor, idade_max):
        self.coord = tupla          # posição (i,j) do hospedeiro
        self.status = status        # 0:não infectiva  1:infectiva
        self.idade_cor = idade_cor  # idade corrente
        self.idade_max = idade_max  # idade máxima na fase de ninfa (passagem para adulto)

    def __str__(self):
        # print("\tNinfa",end="| ");
        # print("Coord: ",end='');print(self.coord,end='|');
        # print("Status: ", end='');print(self.status, end='|');
        # print("Idade Corre: ", end='');print(self.idade_corrente, end='|');
        # print("Idade Max: ", end='');print(self.idade_corrente_max,end='|');
        this_str = "\tNinfa| "
        this_str += "Coord: " + str(self.coord) + '|'
        this_str += "Status: " + str(self.status) + '|'
        this_str += "Idade Corre: " + str(self.idade_cor) + '|'
        this_str += "Idade Max: " + str(self.idade_max) + '|'
        return this_str
