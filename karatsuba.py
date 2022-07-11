x = 31415926535897932384626433832795028841971693993751058209749445922222100000
y = 271828182845904523536028747135266249775724709369995957496696762787213231

def karat(n1, n2):
    if len(str(n1)) == 1 or len(str(n2)):
        return n1 * n2
    else:
        numLen = max(len(str(n1)), len(str(n2)))
        
        midLen = numLen // 2
        
        a = n1 // 10 ** (midLen)
        b = n1 % 10 ** (midLen)
        
        c = n2 // 10 ** (midLen)
        d = n2 % 10 ** (midLen)
        
        ac = karat(a,c)
        bd = karat(b,d)
        
        ad_plus_bc = karat(a+b, c+d) - ac - bd
        
        prod = ac * 10**(2*midLen) + (ad_plus_bc * 10**midLen) + bd
    
        return prod

z = karat(x,y)

print(z == (x * y))
