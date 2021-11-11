''' Meu primeiro metodo!

Aqui temos uma calculadora

'''

def calculadora_pacote(var1, var2, op='soma'):
    if op == 'soma':
        return var1 + var2
    
    if op == 'subtracao':
        return var1 - var2
    
    if op == 'multiplicacao':
        return var1 * var2
    
    if op == 'divisao':
        return var1 / var2