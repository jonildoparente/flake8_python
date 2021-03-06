from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


cx1 = 1
cx2 = 2
cx3 = 3

fila_nm = FabricaFila.pega_fila('prioritaria')
fila_nm.atualiza_fila()
fila_nm.atualiza_fila()
fila_nm.atualiza_fila()

fila_pr = FabricaFila.pega_fila('prioritaria')
fila_pr.atualiza_fila()
fila_pr.atualiza_fila()

print(fila_pr.chama_cliente(cx1))
print(fila_pr.chama_cliente(cx3))
print(fila_nm.chama_cliente(cx2))
print(fila_pr.chama_cliente(cx2))
print(fila_nm.chama_cliente(cx1))

print(fila_nm.estatistica(EstatisticaResumida('10', 1098)))
