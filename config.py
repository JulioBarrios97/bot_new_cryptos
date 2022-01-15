API_KEY = '...'
API_SECRET = '...'

# ----------------------------------------------
#                   Amounts

print("Ingrese la cantidad de capital que desee utilizar por operación")
# numBTC = int(input("Minimo 0.0013 BTC: "))
# numETH = int(input("Minimo 0.03 ETH: "))
# numUSDT = int(input("Minimo 20 USDT: "))
numBUSD = float(input("Minimo 20 BUSD: "))
# numBNB = int(input("Minimo 0.7 BNB: "))

# ----------------------------------------------
#               Risk Management

print("Ingrese parametros de gestión de riesgo")
take_profit = (100 + float(input("Take Proffit: "))) / 100
stop_loss = (100 + float(input("Stop Loss: "))) / 100


