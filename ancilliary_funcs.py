import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def genera(df):
    columnas = df.columns
    columnas = list(columnas)
    columnas.remove('cname')
    columnas.remove('ccodealp')
    columnas.remove('ht_region')
    fu = lambda x: np.mean(df[x])
    analisis = list(map(fu,columnas))
    analisis = {columnas[i]:analisis[i] for i in range(len(columnas))}
    return analisis



def count_nan(df,var,print_list=False): 
    serie = df[var]
    cantidad = 0
    for i in serie:
        if i == 'Nan':   # Lo anterior por que en el sample csv los Nan eran string
            cantidad += 1
        elif type(i) == np.float:
            if np.isnan(i):
                cantidad +=1
    porcentaje = cantidad/len(serie)
    if (print_list):
        index_registro = []
        for i,j in serie.items():
            if type(j) == np.float or j == 'Nan':
                if j == 'Nan':
                    index_registro.append(i)
                elif np.isnan(j):
                    index_registro.append(i)
        return cantidad,porcentaje,index_registro
    return cantidad,porcentaje

def histograma(df,var,true_mean=False,sample_mean=False):
    
    plt.hist(df[var])
    bottom, top = plt.ylim()  # return the current ylim
    plt.ylim((bottom, top))   # set the ylim to bottom, top
    plt.ylim(bottom, top)
    if sample_mean:
        plt.axvline(df[var].mean(), color='k', linestyle='dashed', linewidth=1)
        plt.text(df[var].mean() + df[var].mean()/10, top-top/10, 'Mean: {:.2f}'.format(df[var].mean()))
    if true_mean:
        plt.axvline(df_o[var].mean(), color='r', linestyle='dashed', linewidth=1)
        plt.text(np.mean(df_o[var]) + np.mean(df_o[var])/10, top-top/5, 'True Mean: {:.2f}'.format(np.mean(df_o[var])),bbox=dict(facecolor='red', alpha=0.5))
    plt.show

def count_nan_df(base):
    columnas = base.columns
    fu = lambda x: count_nan(df= base,var =x)
    analisis = {columnas[i]:list(map(fu,columnas))[i] for i in range(len(columnas))}
    analisis = pd.DataFrame.from_dict(analisis)
    analisis.rename(index={0:'cantidad Nan',1:'porcentaje Nan'})
    return analisis

def gen_dot(df,plot_var,plot_by,global_stat=False,statistic='mean'):
    if statistic == 'mean':
        if global_stat:
            var1 = df.groupby(plot_by)[plot_var].mean()
            var = plot_var
            plt.plot(var1.values, var1.index, 'o')
            plt.axvline(df[var].mean(), color='k', linestyle='dashed', linewidth=1)
            plt.text(df[var].mean() + df[var].mean()/10, 5, 'Mean: {:.2f}'.format(df[var].mean()))
            plt.show()
        else:
            var1 = df.groupby(plot_by)[plot_var].mean()
            plt.plot(var1.values, var1.index, 'o')
            plt.show()
    if statistic == 'median':
        if global_stat:
            var1 = df.groupby(plot_by)[plot_var].median()
            var = plot_var
            plt.plot(var1.values, var1.index, 'o')
            plt.axvline(df[var].median(), color='k', linestyle='dashed', linewidth=1)
            plt.text(df[var].median() + df[var].median()/10, 5, 'Mediana: {:.2f}'.format(df[var].median()))
            plt.show()
        else:
            var1 = df.groupby(plot_by)[plot_var].median()
            plt.plot(var1.values, var1.index, 'o')
            plt.show()