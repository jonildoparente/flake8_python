from fabrica_fila import FabricaFila


fila_nm = FabricaFila.pega_fila('normal')
fila_nm.atualiza_fila()
fila_nm.atualiza_fila()
fila_nm.atualiza_fila()

fila_pr = FabricaFila.pega_fila('prioritaria')
fila_pr.atualiza_fila()
fila_pr.atualiza_fila()

cx1 = 1
cx2 = 2
cx3 = 3


print(fila_pr.chama_cliente(cx1))
print(fila_pr.chama_cliente(cx3))
print(fila_nm.chama_cliente(cx2))
print(fila_pr.chama_cliente(cx2))
print(fila_nm.chama_cliente(cx1))
