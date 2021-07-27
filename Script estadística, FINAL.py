import pandas as pd
import matplotlib.pyplot as plt

#Función encargada de hacer los gráficos estadísticos
def graficos(stdr):
    print("GRÁFICA DE LA SERIE DE DATOS\n")
    plt.rcParams["figure.figsize"] = (20, 10)
    plt.plot(stdr.index,stdr.Valor)
    plt.show()
    stdr.Valor.plot.hist()
    print("HISTOGRAMA\n")
    plt.xlabel("Precipitación")
    plt.show()
    print("BOXPLOT\n")
    stdr.boxplot(column="Valor")
    plt.show()
    
    return


"""
resume todas las operaciones necesarias para gráficar los datos de una estación
y hacer su estadistica descriptiva.

"""
#La función base del codigo se llama estadisticahidrólogica.
"""
Notas para la compresión del código: 

dfd= Data frame diario.
dfm= Data frame mensual.
dfa= Data frame anual.

"""

def estadisticahidrologica(est):
    dfd = pd.read_csv(est, encoding='latin-1')
    print("Estadistica hidrólogica para la estación " + est + "\n")
    #Se aislan las columnas de interés (Fecha y valor)
    df = dfd.iloc[:,16:18]
    #Se obtiene la transpuesta del nuevo data frame
    df = df.transpose()
    #Se establecen nuevos encabezados de columnas, que correspondan a las fechas.
    df.columns = dfd.Fecha
    #Se eliminan las fechas como fila de valores.
    df = df.iloc[1:2,:]
    #Usando pandas, y con las fechas como encabezado de columna, se organizan los valores
    #haciendo una sumatoria mensual y otra anual
    dfm = df.groupby(pd.PeriodIndex(df.columns, freq='M'),axis=1).sum()
    dfa = df.groupby(pd.PeriodIndex(df.columns, freq='A'),axis=1).sum()
    #regresando dfm al formato original.
    dfm = dfm.transpose()
    dfm.reset_index(level=0, inplace=True)
    #regresando dfa al formato original
    dfa = dfa.transpose()
    dfa.reset_index(level=0, inplace=True)
    
    #Se invoca la función que contiene todos los gráficos solicitados 
    print("Estos son los gráficos generados para el Data Frame Diario\n")
    graficos(dfd)
    print("Estos son los gráficos generados para el Data Frame Mensual\n")
    graficos(dfm)
    print("Estos son los gráficos generados para el Data Frame Anual\n")
    graficos(dfa)
    
    print("\nESTADISTICA DESCRIPTIVA\n")
    
    #Se invoca la función que genera la estadística descriptiva
    print("Esta es la estadística descriptiva  para el Data Frame Diario\n")
    print(dfd.Valor.describe())
    print("\nEsta es la estadística descriptiva  para el Data Frame Mensual\n")
    print(dfm.Valor.describe())
    print("\nEsta es la estadística descriptiva  para el Data Frame Anual\n")
    print(dfa.Valor.describe())
    
    return

estadisticahidrologica("CATAM.csv")
estadisticahidrologica("INEM KENNEDY.csv")
    
    
   
