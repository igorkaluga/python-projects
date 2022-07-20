def inv_casc(n):
        #grow from first number to last
        grow(n)
        #return n unchanced
        print(n)
        #start shrinking
        shrink(n)

def f_then_g(f,g,n):
        if n:
                f(n) #recursively keep calling f on n until n == 0
                g(n) #then start calling g on n's of that frame (the print in this case)

# in grow frist you grow the number (keep decreasing n until 0) and then start printing the frames n
# by calling the function g (print in this case)
grow = lambda n: f_then_g(grow, print, n // 10)
# similar to grow, but now you will print n // 10 first and then recursively keep calling g to
# decrease the n // 10 each recursive call.
shrink = lambda n: f_then_g(print, shrink, n // 10)
