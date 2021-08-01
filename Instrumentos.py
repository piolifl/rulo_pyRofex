import pyRofex
from Pass import config

pyRofex._set_environment_parameter(
    "url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter(
    "ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(config.user,
                   config.password,
                   config.account,
                   environment=pyRofex.Environment.LIVE)

class INSTRUMENTOS:
    def __init__(self, ticker):
        self.ticker = ticker
      
    def precio_LA(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.LAST])
            instrumento = var['marketData']['LA']['price']
        except:
            instrumento = 100
        return instrumento
    def precio_OF(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.OFFERS])
            instrumento = var['marketData']['OF'][0]['price']
        except:
            instrumento = 100
        return instrumento
    def precio_BI(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.BIDS])
            instrumento = var['marketData']['BI'][0]['price']
        except:
            instrumento = 100
        return instrumento
    def vender(self,cantidad,precio):
        pyRofex.send_order(
            ticker=self.ticker,
            side=pyRofex.Side.SELL, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)   
        return self
    def comprar(self,cantidad,precio):
        pyRofex.send_order(
            ticker=self.ticker,
            side=pyRofex.Side.BUY, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)   
        return self
    def __str__(self):
        return self.ticker

class AL30(INSTRUMENTOS):
    pass
class AL29(INSTRUMENTOS):
    pass
class AE38(INSTRUMENTOS):
    pass
class AL35(INSTRUMENTOS):
    pass
class AL41(INSTRUMENTOS):
    pass
class GD29(INSTRUMENTOS):
    pass
class GD30(INSTRUMENTOS):
    pass
class GD35(INSTRUMENTOS):
    pass
class GD38(INSTRUMENTOS):
    pass
class GD41(INSTRUMENTOS):
    pass
class S30G1(INSTRUMENTOS):
    pass
class AAPL(INSTRUMENTOS):
    pass

ae38_48 = AE38('MERV - XMEV - AE38 - 48hs')
ae38c_48 = AE38('MERV - XMEV - AE38C - 48hs')
ae38d_48 = AE38('MERV - XMEV - AE38D - 48hs')
al29_48 = AL29('MERV - XMEV - AL29 - 48hs')
al29c_48 = AL29('MERV - XMEV - AL29C - 48hs')
al29d_48 = AL29('MERV - XMEV - AL29D - 48hs')
al30_ci = AL30('MERV - XMEV - AL30 - CI')
al30c_ci = AL30('MERV - XMEV - AL30C - CI')
al30d_ci = AL30('MERV - XMEV - AL30D - CI')
al30_48 = AL30('MERV - XMEV - AL30 - 48hs')
al30c_48 = AL30('MERV - XMEV - AL30C - 48hs')
al30d_48 = AL30('MERV - XMEV - AL30D - 48hs')
al35_48 = AL35('MERV - XMEV - AL35 - 48hs')
al35c_48 = AL35('MERV - XMEV - AL35C - 48hs')
al35d_48 = AL35('MERV - XMEV - AL35D - 48hs')
al41_48 = AL41('MERV - XMEV - AL41 - 48hs')
al41c_48 = AL41('MERV - XMEV - AL41C - 48hs')
al41d_48 = AL41('MERV - XMEV - AL41D - 48hs')


gd29_48 = GD29('MERV - XMEV - GD29 - 48hs')
gd29c_48 = GD29('MERV - XMEV - GD29C - 48hs')
gd29d_48 = GD29('MERV - XMEV - GD29D - 48hs')
gd30_ci = GD30('MERV - XMEV - GD30 - CI')
gd30c_ci = GD30('MERV - XMEV - GD30C - CI')
gd30d_ci = GD30('MERV - XMEV - GD30D - CI')
gd30_48 = GD30('MERV - XMEV - GD30 - 48hs')
gd30c_48 = GD30('MERV - XMEV - GD30C - 48hs')
gd30d_48 = GD30('MERV - XMEV - GD30D - 48hs')
gd35_48 = GD35('MERV - XMEV - GD35 - 48hs')
gd35c_48 = GD35('MERV - XMEV - GD35C - 48hs')
gd35d_48 = GD35('MERV - XMEV - GD35D - 48hs')
gd38_48 = GD38('MERV - XMEV - GD38 - 48hs')
gd38c_48 = GD38('MERV - XMEV - GD38C - 48hs')
gd38d_48 = GD38('MERV - XMEV - GD38D - 48hs')
gd41_48 = GD41('MERV - XMEV - GD41 - 48hs')
gd41c_48 = GD41('MERV - XMEV - GD41C - 48hs')
gd41d_48 = GD41('MERV - XMEV - GD41D - 48hs')


s30g1_ci = S30G1('MERV - XMEV - S30G1 - CI')
sg1c_ci = S30G1('MERV - XMEV - SG1C - CI')
sg1d_ci = S30G1('MERV - XMEV - SG1D - CI')
s30g1_48 = S30G1('MERV - XMEV - S30G1 - 48HS')
sg1c_48 = S30G1('MERV - XMEV - SG1C - 48HS')
sg1d_48 = S30G1('MERV - XMEV - SG1D - 48HS')
