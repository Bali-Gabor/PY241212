from moduls import *

print('LOTTÓSORSOLÁS')
tipus=int(input('Szia, milyen tipusú lottót szeretnél játszani [5,6,7]?  '))


a=szelveny(tipus)
b,c=sorsolas(tipus)
eredmeny(a, b, c, tipus)