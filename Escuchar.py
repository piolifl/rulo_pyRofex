import pyRofex, config
from Instrumentos import INSTRUMENTOS,AL30,gd30d_48,al30c_48
import time

pyRofex._set_environment_parameter(
    "url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter(
    "ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(config.user,
                   config.password,
                   config.account,
                   environment=pyRofex.Environment.LIVE)

inicial = 100
estado = 'No esta'
hora = ''


def pregunta(status,cantidad,ticker,precio,side):
    global hora, estado, cancelar
    consulta = pyRofex.get_all_orders_status()
    for i in consulta['orders']:
        if i['transactTime'] > hora:
            hora = i['transactTime']

        if i['status'] == status and i['orderQty'] == cantidad and i['instrumentId']['symbol'] == ticker and i['price'] == precio and i['side'] == side:
            estado = 'Si esta'
            print('Estado: {0}  // hora: {1}'.format(estado,hora))
            print(pyRofex.cancel_order(i["orderId"]))

        
pregunta('NEW',10,'MERV - XMEV - AL30C - CI',36.3,'SELL')
print(hora)

#consulta = pyRofex.get_all_orders_status()
#for i in consulta['orders']:
    #print(i)

#print(pyRofex.get_order_status(order))




'''
{'orderId': 'O06rI926iHnC-00871391', 'clOrdId': '366135418007192', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE06rI4C4CFr0', 
'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AL30C - CI'}, 'price': 36.15, 'orderQty': 100, 'ordType': 'LIMIT', 'side': 'SELL', 'timeInForce': 'DAY', 'transactTime': '20210729-13:17:13.832-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 100, 'status': 'CANCELLED', 'text': 'CANCELED', 'originatingUsername': 'ISV_PBCP'}'''

'''
{'orderId': 'O06rI926hqG6-00035533', 'clOrdId': 'tx6SoWV42mjXlHIy', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE06rI4C48IIr', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AL30C - CI'}, 'price': 35.79, 'orderQty': 1000, 'ordType': 'LIMIT', 'side': 'SELL', 'timeInForce': 'DAY', 'transactTime': '20210729-11:04:44.449-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 1000, 'iceberg': 'true', 'displayQty': 0, 'status': 'CANCELLED', 'text': 'Cancelled by Owner', 'numericOrderId': '00035533', 'origClOrdId': 'SV5mufVoTgtpbWCV', 'originatingUsername': 'ISV_MATRIZ4'}'''