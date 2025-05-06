
from gerador_loteria import gerador_megasena, gerador_lotofacil, gerador_quina, gerador_lotomania

print("=====" * 16)
print("===" * 8, "  GERADOR DE APOSTA LOTERIA  ", "===" * 8)
print("=====" * 16)

print(">> QUAL JOGO DESEJA APOSTAR?")
jogo = int(input("[1] MEGASENA]\n[2] LOTOFÁCIL]\n[3] QUINA]\n[4] LOTOMANIA]\n>> "))

if jogo == 1:
  gerador_megasena()
elif jogo == 2:
  gerador_lotofacil()
elif jogo == 3:
  gerador_quina()
elif jogo == 4:
  gerador_lotomania()
else:
  print("!!! ERRO, OPÇÃO INVALIDA !!! ")


