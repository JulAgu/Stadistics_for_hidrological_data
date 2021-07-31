import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import dateutil

"""
Summarizes all the operations necessary to graph the data of a station
and do your descriptive statistics
"""
# The base function of the code is called hydrological_statistics
"""
Main variables: 
ddf: Daily Data frame.
mdf: Mensual Data frame.
adf: Annual Data frame.
"""


# Function in charge of making statistical graphics
def graphic(dataframe):
    plt.rcParams["figure.figsize"] = (7, 7)
    # Bar graph
    plt.title("Gráfica de la serie de datos")
    plt.plot(dataframe.index, dataframe.Valor)
    plt.show()
    # Histogram
    plt.title("Histograma")
    dataframe.Valor.plot.hist()
    plt.xlabel("Precipitación")
    plt.show()
    # Boxplot
    plt.title("Diagrama de caja")
    dataframe.boxplot(column="Valor")
    plt.show()


# Function in charge of making descriptive statistics
def hydrological_statistics(file_path):
    # Master DataFrame
    dataframe = pd.read_csv(file_path)
    # Convert from String to DateTime
    dataframe['Fecha'] = dataframe['Fecha'].apply(
        dateutil.parser.parse, dayfirst=True)
    # Columns of interest are isolated (Date and value)
    columns = ['Fecha', 'Valor']
    df = dataframe.loc[:, pd.Index(columns)]
    # Define the value by which you want to group the data
    my_key = columns[0]
    df.set_index(my_key)
    # The dates of the Data Frames are grouped by day, month and year
    ddf = df
    mdf = df.groupby(pd.Grouper(key=my_key, freq='M')).sum()
    adf = df.groupby(pd.Grouper(key=my_key, freq='A')).sum()
    # Descriptive statistics
    dstr = str(ddf.Valor.describe())
    tk.messagebox.showinfo(message=dstr, title="Data frame diario")
    graphic(ddf)
    mstr = str(mdf.Valor.describe())
    tk.messagebox.showinfo(message=mstr, title="Data frame mensual")
    graphic(mdf)
    astr = str(adf.Valor.describe())
    tk.messagebox.showinfo(message=astr, title="Data frame anual")
    graphic(adf)


if __name__ == '__main__':
    # Select .csv file
    path = tk.filedialog.askopenfilename(title='Seleccione archivo')
    if path.find('.csv') != -1:
        hydrological_statistics(path)
    else:
        tk.messagebox.showinfo(
            message="El archivo no es de tipo .csv", title="Error")
