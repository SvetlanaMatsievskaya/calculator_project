
from fractions import Fraction



def data_formatting(data):
    data_type, value_a, operation, value_b = data

    if data_type == '1':

        value_a = complex(value_a)

        value_b = complex(value_b)

    elif data_type == '2':

        a = value_a
        value_a = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = value_b
        right_value = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (value_a, operation, value_b)