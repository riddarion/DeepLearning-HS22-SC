
#Deep Learning Aufgabe 11
#________________________


import numpy as np
from d2l import tensorflow as d2l

#Funktion
def f(x):
    y = x**3 - 1/x
    return y

#Ableitung
def Df(x):
    h = (3*x**2) + (1/x**2)
    return h

#Grenzwert
def numerical_lim(f, x, h):
 return (f(x-h) - f(x) / h)


#h = Df(1)
# for i in range(5):
#     print(f'h={h:.5f}, numerical lim={numerical_lim(f, 1, h):.5f}')
#     h *= 0.1


#Y-Achsenabschnitt für die Tangente bei x1 = 1 berechnen
#Geradengleichung Grundform: y = h*x + b
x1 = 1
h = Df(1)
b = h*x1 - f(x1)

#Verallgemeinerung
def b_(x, h):
    b = h*x - f(x)
    return b

#Tangente
def tangente(x, h, b):
        y = h*x - b
        return y


#Vorbereitung für die Visualisierung im Koordinatensystem
def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()



def plot(X, Y=None, xlabel=None, ylabel=None, legend=None,
         xlim=None, ylim=None, xscale='linear', yscale='linear',
         fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
    if legend is None:
        legend=[]

        axes = axes if axes else d2l.plt.gca()

    def has_one_axis(X):
        return (hasattr(X, 'ndim') and X.ndim == 1 or
                isinstance(X, list) and not hasattr(X[0], '__len__'))

    if has_one_axis(X):
        X=[X]
        if Y is None:
            X, Y = [[]] * len(X), X
        elif has_one_axis(Y):
            Y=[Y]
        if len(X) != len(Y):
            X = X * len(Y)
        axes.cla()
        for x, y, fmt in zip(X, Y, fmts):
            if len(x):
                axes.plot(x, y, fmt)
            else:
                axes.plot(y, fmt)
            set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

#Funktion zeichnen
x = np.arange(0.1, 3, 0.1)
d2l.plot(x, [f(x), tangente(x, Df(x1), b_(x1, Df(x1)))], 'x', 'f(x)', legend=['f(x)', 'Tangent-Line'])

d2l.plt.show()


