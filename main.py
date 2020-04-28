from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria

fila = Filanormal()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()

cx1 = 1
cx2 = 2
cx3 = 3

#print(fila.chama_cliente(1))
#print(fila.chama_cliente(3))

fp = FilaPrioritaria()
fp.atualiza_fila()
fp.atualiza_fila()
fp.atualiza_fila()
fp.atualiza_fila()
fp.atualiza_fila()
fp.atualiza_fila()

fp.chama_cliente(cx1)
fp.chama_cliente(cx3)
fp.chama_cliente(cx2)
fp.chama_cliente(cx2)
fp.chama_cliente(cx1)

est = fp.estatistica(27, 1054, "detail")

print(est)
