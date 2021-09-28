class Intervalle:
    def __init__(self,borneInf,borneSup):
        self.borneInf = borneInf
        self.borneSup = borneSup

    def est_vide(self):
        if self.borneInf>self.borneSup:
            return True
        else:
            return False

    def __str__(self):
        if self.est_vide()==True:
            return "[]"
        else:
            return f"[{self.borneInf},{self.borneSup}]" 

    def __len__(self): 
        if self.borneInf>self.borneSup:
            return 0
        else:
            return self.borneSup-self.borneInf

    def __contient__(self,x):
        if self.borneInf<=x<=self.borneSup:
            return True
        else:
            return False

    def __eq__(self,interv2):
        ################# on s'épare notre tuple #################
        interv2_borneInf,interv2_borneSup = interv2
        if self.__len__() == (interv2_borneSup - interv2_borneInf):
            return True

    def __le__(self,interv2):
        ################# on s'épare notre tuple #################
        interv2_borneInf,interv2_borneSup = interv2
        if self.borneInf<=interv2_borneInf and self.borneSup>=interv2_borneSup:
            return True

    def intersection(self,interv2):
        ################# on s'épare notre tuple #################
        interv2_borneInf,interv2_borneSup = interv2
        ################# on verifie si l'un des nombre du nouvellle intervalle est compris dans l'autre ################# 
        if self.__contient__(interv2_borneInf) == True or self.__contient__(interv2_borneSup) == True:
            ################# on créer une liste contenant tous les nombres #################
            ascending_list  = [self.borneSup,self.borneInf,interv2_borneSup,interv2_borneInf]
            ################# on la tire dans l'ordre croissant #################
            ascending_list.sort()
            ################# on retourn l'intervale (soit les deux termes du millieux) #################
            return ascending_list[1],ascending_list[2]


    def union(self,interv2):
        ################# on s'épare notre tuple #################
        interv2_borneInf,interv2_borneSup = interv2
        ################# on créer une liste contenant tous les nombres #################
        ascending_list  = [self.borneSup,self.borneInf,interv2_borneSup,interv2_borneInf]
        ################# on la tire dans l'ordre croissant #################
        ascending_list.sort()
        ################# on vérifie si notre intervale est bien compris dans l'autre interval en regardant s'il n'est pas exclu #################
        if (interv2_borneInf == ascending_list[2] and interv2_borneSup == ascending_list[3]) or (interv2_borneInf == ascending_list[0] and interv2_borneSup == ascending_list[1]):
            return
        ################# on retourn l'union (soit le premier terme et le dernier) #################
        return ascending_list[0],ascending_list[3]

        
def main():
    e=Intervalle(3,8)
    print(e.est_vide())
    print(e.__str__())
    print(e.__len__()) 
    print(e.__contient__(6))
    print(e.__eq__((4,9)))
    print(e.__le__((4,7)))
    print(e.intersection((5,11)))
    print(e.union((1,7)))

main()