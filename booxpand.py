from booparser import booparse
from boolexer import boolex


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def expand(s):
    '''
    # booexand() is the book version of EXPAND. 
    # We make a small change to add a wrapper that first checks that s is enclosed in parentheses 
    # and terminated with semi colon before passing 's' to the lexer / parser. The reuslting lexed 
    # and parsed s (now a dicitonary) is then passed into booexpand()

    Parameters
    ----------
    A boolean as a string (preferentially enclosed in parnetheses and semicolon terminated)

    Returns
    -------
     Dictionary:  {psi: ... , distinguished literal :..., cnt: (not useful)}

    >>> expand("(!(x1+(x2.!x3)));")
    ... # doctest: +NORMALIZE_WHITESPACE 
    {'psi': 'x1.!y0+ y2.!y0+ !x1.!y2.y0 +!x2y2 + !!x3y2 + x2.!x3.!y2', \
     'dl': '!y0', 'cnt': 0}
    '''
    def booexpand(typ, val, cnt=0):

        if typ == "literal":
            return {'psi': '0', 'dl':val, 'cnt' : str(cnt)}
        elif typ == "!":
            typ, val = val[0],val[1]
            dct = booexpand(typ,val,cnt)
            dct['dl'] = '!' + dct['dl']
            return dct
        elif typ == "dnf":
            val0, val1 = val[0], val[1]
            dct0 = booexpand(val0[0],val0[1],cnt+1)
            dct1 = booexpand(val1[0],val1[1],cnt+2)
            yi = '.y'+ str(cnt)
            yib = '.!'+ 'y' + str(cnt) + '+'
            psii = dct0['dl'] + yib + ' ' + dct1['dl'] + yib + ' ' +  \
                    '!'+ dct0['dl'] + '.!' + dct1['dl'] + yi
            if dct0['psi'] is not '':
                psii += ' +' + dct0['psi']
            if dct1['psi'] is not '':
                psii += ' +' + dct1['psi']
            return {'psi':psii, 'dl': yi[1:], 'cnt':cnt}
        elif typ == "cnf":
            val0, val1 = val[0], val[1]
            dct0 = booexpand(val0[0],val0[1],cnt+1)
            dct1 = booexpand(val1[0],val1[1],cnt+2)
            yi = 'y'+ str(cnt)
            yib = '.!' + 'y' + str(cnt)
            psii = '!' + dct0['dl'] + yi + ' + ' + '!' +  dct1['dl'] + yi + ' + ' +  \
                    dct0['dl'] + '.' + dct1['dl'] + '.!' + yi
            if dct0['psi'] is not '':
                psii += ' +' + dct0['psi']
            if dct1['psi'] is not '':
                psii += ' +' + dct1['psi']       
            return {'psi':psii, 'dl': yi, 'cnt':cnt}
        elif typ == "term":
            typ = val[0][0]
            if typ is "dnf" or typ is "cnf":
                val = (val[0][1], val[0][2])
            else:
                val = val[0][1]
            return booexpand(typ, val , cnt)
        else:
            raise Exception("Unexpected token: " + str((typ, val)))

    if s[0] != "(":
        s = s + ")"
    if s[-2:] != ");":
        s += ");"
    s_iter = booparse(boolex(s))  # call lexer and parse on input string s
    typ, val = next(s_iter)
    dct = booexpand(typ, val)
    return dct

s = "(x1.x2);"
print(expand(s))