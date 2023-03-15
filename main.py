from iqoptionapi.stable_api import IQ_Option
import numpy as np
import pandas as pd
import time
from colorama import Fore, Style

API = IQ_Option("mail@gmail.com","pwd")

API.connect()

# Definindo o ativo e o período de tempo desejado
asset = "AUDJPY"
timeframe = 5

# Obtendo os últimos 10 candles
candles = API.get_candles(asset, timeframe * 60, 100, time.time())
candles_list = candles

print("\n Obtendo últimas 100 velas... \n")
time.sleep(1)
# Obtendo a cor de cada candle
qtdVermelhas = 0
qtdverdes = 0

for candle in candles_list:
    candle_open = candle["open"]
    candle_close = candle["close"]
    if candle_open < candle_close:
        print( Fore.GREEN +  "verde" + Style.RESET_ALL)
        qtdverdes +=1
    elif candle_open > candle_close:
        print(Fore.RED + "vermelho" + Style.RESET_ALL)
        qtdVermelhas +=1 
    else:
        print("DOGE")
    time.sleep(0.1)

operacao = ''
if qtdVermelhas > qtdverdes:
    operacao = "CALL"
else:
    operacao = "PUT"

print("\n operação sugerida: " + Fore.YELLOW + operacao + Style.RESET_ALL + "\n")