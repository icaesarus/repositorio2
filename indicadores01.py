#indicadores Bollinger
def BollingerBands (array, ventana, factor):
    mm = array.rolling(ventana).mean()
    sd = array.rolling(ventana).std()
    upper = mm+factor*sd
    lower = mm-factor*sd
    return lower, upper
# Indicador media movil
def mediamovil (array, ventana):
    mm = array.rolling(ventana).mean()
    return mm
def standarddeviation (array, ventana):
    std = array.rolling(ventana).std()
    return std
def funCCI (close, high, low, ventana):
    PT=(close+high+low)/3
    mm = mediamovil(PT,ventana)
    std= standarddeviation(PT,ventana)
    CCI = (PT - mm)/(.015*std)
    return PT, CCI

