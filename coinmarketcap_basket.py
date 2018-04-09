import coinmarketcap
import json
import pandas as pd
import time

market = coinmarketcap.Market()

ethereum = market.ticker("ethereum")
bitcoin = market.ticker("bitcoin")
bitcoin_cash = market.ticker("bitcoin-cash")
stellar = market.ticker("stellar")
ethereum_classic = market.ticker("ethereum-classic")
vechain = market.ticker("vechain")
iota = market.ticker("iota")
icon = market.ticker("icon")
nano = market.ticker("nano")
zcash = market.ticker("zcash")
dash = market.ticker("dash")

eth = ethereum[0]['price_usd']
btc = bitcoin[0]['price_usd']
bch = bitcoin_cash[0]['price_usd']
xlm = stellar[0]['price_usd']
etc = ethereum_classic[0]['price_usd']
ven = vechain[0]['price_usd']
miota = iota[0]['price_usd']
icx = icon[0]['price_usd']
xrb = nano[0]['price_usd']
zec = zcash[0]['price_usd']
dsh =  dash[0]['price_usd']

total_price = float(eth) + float(btc) + float(bch) + float(xlm) + float(etc) + float(ven) + float(miota) + float(icx) + float(xrb) + float(zec) + float(dsh)


print total_price
