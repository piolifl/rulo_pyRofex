from Instrumentos import INSTRUMENTOS, AE38,AL29,AL30,AL35,AL41,GD29,GD30,GD35,GD38,GD41
from Instrumentos import al30_48,ae38_48,al29_48,al35_48,al41_48,gd29_48,gd30_48,gd35_48,gd38_48,gd41_48,s30g1_48
from Instrumentos import al30c_48,ae38c_48,al29c_48,al35c_48,al41c_48,gd29c_48,gd30c_48,gd35c_48,gd38c_48,gd41c_48,sg1c_48
from Instrumentos import al30d_48,ae38d_48,al29d_48,al35d_48,al41d_48,gd29d_48,gd30d_48,gd35d_48,gd38d_48,gd41d_48,sg1d_48
from Instrumentos import al30_ci,gd30_ci,s30g1_ci
from Instrumentos import al30c_ci,gd30c_ci,sg1c_ci
from Instrumentos import al30d_ci,gd30d_ci,sg1d_ci
import pyRofex
import time
import math

inicial = 10
venta_total = 0
limite = 20
gana_bonos = 0
gana_dolar = 0
gana_cable = 0
gana_pesos = 0
hora = ''
plazo = '48'

def cable_dolar(ticker1,ticker2,ticker3,ticker4):
    global vendo_cable, compro_cable, vendo_dolar, compro_dolar
    vendo_cable = round(((ticker1/100) * (1-0.005)) * inicial,2)
    compro_cable = round(vendo_cable / (ticker2/100),0)
    vendo_dolar = round(compro_cable * ((ticker3/100)* (1-0.005)),2)
    compro_dolar = round(vendo_dolar // (ticker4/100),0)
    print('CCL:',vendo_cable,end=" // ")
    print('Nom:',compro_cable,end=" // ")
    print('USD:',vendo_dolar,end=" /// ")
    print('Nom:',compro_dolar)
def dolar_pesos(ticker1,ticker2,ticker3,ticker4):
    global vendo_dolar, compro_dolar, vendo_pesos, compro_pesos
    vendo_dolar = round(((ticker1/100) * (1-0.005)) * inicial,2)
    compro_dolar = round(vendo_dolar / (ticker2/100),0)
    vendo_pesos = round(compro_dolar * ((ticker3/100)* (1-0.005)),2)
    compro_pesos = round(vendo_pesos // (ticker4/100),0)
    print('USD:',vendo_dolar,end=" /// ")
    print('Nom:',compro_dolar,end=" /// ")
    print('ARS:',vendo_pesos,end=" ///// ")
    print('Nom:',compro_pesos)
def cable_pesos(ticker1,ticker2,ticker3,ticker4):
    global vendo_cable, compro_cable, vendo_pesos, compro_pesos
    vendo_cable = round(((ticker1/100) * (1-0.005)) * inicial,2)
    compro_cable = round(vendo_cable / (ticker2/100),0)
    vendo_pesos = round(compro_cable * ((ticker3/100)* (1-0.005)),2)
    compro_pesos = round(vendo_pesos // (ticker4/100),0)
    print('CCL:',vendo_cable,end=" /// ")
    print('gd30c:',compro_cable,end=" /// ")
    print('ARS:',vendo_pesos,end=" ///// ")
    print('al30:',compro_pesos)

def pregunta(status,ticker,cantidad,pecio,side):
    global hora
    consulta = pyRofex.get_all_orders_status()
    for i in consulta['orders']:
        if i['transactTime'] > hora:
            hora = i['transactTime']     
        if i['status'] == status and i['orderQty'] == cantidad and i['instrumentId']['symbol'] == ticker and i['side'] == side:
            return 'si'
        else:
            return 'no'
           
while True:
    if plazo == '48':
        print('48: AL30C/GD30C/GD30/AL30',end = ' /// ') ####################################
        cable_pesos(al30c_48.precio_LA(),gd30c_48.precio_LA(),gd30_48.precio_LA(),al30_48.precio_LA())
        if  venta_total<limite and compro_pesos>=inicial - 1  and al30c_48.precio_LA() != 100:   

            AL30.vender(al30c_48,inicial,al30c_48.precio_LA()+1)
            #precio = al30c_48.precio_BI() + 1 
            if pregunta('FILLED','MERV - XMEV - AL30C - 48HS',inicial,al30c_48.precio_LA()+1,'SELL') == 'no':
                timeout = 5           
                while True:
                    time.sleep(2)
                    if pregunta('FILLED','MERV - XMEV - AL30C - 48HS',inicial,al30c_48.precio_LA()+1,'SELL') == 'si':
                        break
                    else:
                        if timeout > 0:
                            timeout -= 1
                            time.sleep(1)
                            print('Conteo para salir: {0}'.format(timeout),time.strftime("%H:%M:%S"))
                        else:
                            print('Se cancela la orden de compra')
                            break
            GD30.comprar(gd30c_48,compro_cable,gd30c_48.precio_LA())
            GD30.vender(gd30_48,vendo_pesos,gd30_48.precio_LA())
            AL30.comprar(al30_48,compro_pesos,al30_48.precio_LA())
                            
            venta_total += inicial
            gana_bonos += compro_pesos - inicial
            gana_cable += round(vendo_cable - (compro_cable * (gd30c_48.precio_LA()/100)),2)
            gana_pesos += round(vendo_pesos - (compro_pesos * (al30_48.precio_LA()/100)),2)
            #inicial += gana_bonos
            print('Vendido CCL:',venta_total,end=' // ')
            print('Bonos ARS:{0}'.format(gana_bonos),end=' // ')
            print('Ganancia CCL:',gana_cable,end=' // ')
            print('Ganancia ARS:',gana_dolar,end=' // ')
            print('')
            if venta_total == limite:
                print('No sigue la busqueda, limite alcanzado')
                break

    else:
        print('CI: AL30C/GD30C/GD30/AL30',end = ' /// ') ####################################
        cable_pesos(al30c_ci.precio_BI(),gd30c_ci.precio_BI(),gd30_ci.precio_BI(),al30_ci.precio_OF())
        if  venta_total<limite and compro_pesos>=inicial+1 and al30c_ci.precio_BI() != 100:   

            AL30.vender(al30c_ci,inicial,al30c_ci.precio_BI() +1)
            #precio = al30c_ci.precio_BI() + 1  
            if pregunta('FILLED','MERV - XMEV - AL30C - CI',inicial,al30c_ci.precio_BI() + 1 ,'SELL') == 'no':  
                timeout = 5           
                while True:
                    time.sleep(2)                   
                    if pregunta('FILLED','MERV - XMEV - AL30C - CI',inicial,al30c_ci.precio_BI() + 1 ,'SELL') == 'si':
                        break
                    else:
                        if timeout > 0:
                            timeout -= 1
                            time.sleep(1)
                            print('Conteo para salir: {0}'.format(timeout),time.strftime("%H:%M:%S"))
                        else:
                            print('Se cancela la orden de compra')
                            break
            GD30.comprar(gd30c_ci,compro_cable,gd30c_ci.precio_BI())
            GD30.vender(gd30_ci,vendo_pesos,gd30_ci.precio_BI())
            AL30.comprar(al30_ci,compro_pesos,al30_ci.precio_OF())
                            
            venta_total += inicial
            gana_bonos += compro_pesos - inicial
            gana_cable += round(vendo_cable - (compro_cable * (gd30c_ci.precio_BI()/100)),2)
            gana_pesos += round(vendo_pesos - (compro_pesos * (al30_ci.precio_OF()/100)),2)
            #inicial += gana_bonos
            print('Vendido CCL:',venta_total,end=' // ')
            print('Bonos ARS:{0}'.format(gana_bonos),end=' // ')
            print('Ganancia CCL:',gana_cable,end=' // ')
            print('Ganancia ARS:',gana_dolar,end=' // ')
            print('')
            if venta_total == limite:
                print('No sigue la busqueda, limite alcanzado')
                break

        else:
            print(('         Sigue la continua... busqueda'), time.strftime("%H:%M:%S"))
            time.sleep(1)
            if venta_total == limite:
                print('No sigue la busqueda, limite alcanzado')
                break

