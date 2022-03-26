# import joblib
# from datetime import datetime, timedelta
# import time
# import requests
# import pandas as pd
# import numpy as np
# import os

# from crypto_data_fetcher.binance_future import BinanceFutureFetcher

import ccxt
import traceback

#CCXTを使ったBinance先物のAPI設定
binance = ccxt.binance({"apiKey":"○○○○○○○○",   #apiKeyを入力
                         "secret":"○○○○○○○○",  #secretKeyを入力
                         "options": {"defaultType": "future"},
                         "enableRateLimit": True})

#特定の銘柄のポジション情報を取得する関数
def get_binance_position(binance,searchSymbol):
    position = binance.fapiPrivateGetPositionRisk() #全銘柄のポジション情報を取得
    #print(position)

    onlySymbolName = [d.get('symbol') for d in position]  #沢山の辞書データから銘柄の名称だけを順番に抽出
    #print(onlySymbolName)
    
    searchSymbol_index = onlySymbolName.index(searchSymbol) #知りたい銘柄のポジション情報が何番目の辞書に存在するかを特定
    #print("\n{0}のポジション情報は{1}番目に存在".format(str(searchSymbol),str(searchSymbol_index)))
    print("\n現在の{0}のポシジョン情報↓↓↓\n{1}".format(str(searchSymbol),str(position[searchSymbol_index]))) #知りたい銘柄だけの詳細なポジション情報を取得

    positionAmt = float(position[searchSymbol_index]['positionAmt']) #知りたい銘柄のポジションサイズを抽出
    positionSide = str(position[searchSymbol_index]['positionSide']) #知りたい銘柄のポジションサイドを抽出

    if positionAmt == 0:
        positionSide = 'NONE' #ポジションを持ってない時、デフォだとBOTHになってしまい分かりづらいのでNONEに変更
    elif positionAmt > 0:
        positionSide = 'BUY'
    else:
        positionSide = 'SELL'
    return {'positionSide':positionSide, 'positionAmt':positionAmt}


#例としてXRPUSDTのポジション情報を取得する
searchSymbol = "XRPUSDT"
position_XRP = get_binance_position(binance, searchSymbol)

#例:ポジションサイドとポジションサイズだけをそれぞれ取得したい場合
print("\n現在の{0}のポジションサイド:{1}".format(str(searchSymbol),str(position_XRP['positionSide'])))
print("現在の{0}のポジションサイズ:{1}".format(str(searchSymbol),str(position_XRP['positionAmt'])))
