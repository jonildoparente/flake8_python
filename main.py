from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila = FilaNormal()
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

print(fp.chama_cliente(cx1))
print(fp.chama_cliente(cx3))
print(fp.chama_cliente(cx2))
print(fp.chama_cliente(cx2))
print(fp.chama_cliente(cx1))
fp.reseta_fila()

est = fp.estatistica(27, 1055, "detail")

print(est)
