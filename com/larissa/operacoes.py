import sys

class ImprimirLinhas():

    def linhaSimples(self,a):
        for b in range(a):
            sys.stdout.write("-")
        sys.stdout.write("\n")
        return 2