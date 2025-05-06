
from gerador_loteria import gerador_megasena
from gerador_loteria import gerador_lotofacil

print("=====" * 16)
print("===" * 8, "  GERADOR DE APOSTA LOTERIA  ", "===" * 8)
print("=====" * 16)

print(">> QUAL JOGO DESEJA APOSTAR?")
jogo = int(input("[1] MEGASENA]\n[2] LOTOFÁCIL]\n[3] LOTOMANIA]\n[4] DUPLASENA]\n>> "))

if jogo == 1:
  gerador_megasena()
elif jogo == 2:
  gerador_lotofacil()
elif jogo == 3:
  gerador_lotomania()
elif jogo == 4:
  gerador_duplasena()
else:
  print("!!! ERRO, OPÇÃO INVALIDA !!! ")


