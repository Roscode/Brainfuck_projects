""" text to brainfuck """

def factoraprime (prime):
    """factors primes separately to more closely control addnecessity data structure"""
    number = prime-1
    factors = []
    for fac in range(2, 9)[::-1]:
        if number%fac==0:
            factors.append(fac)
            factors.append(number/fac)
            break
    return factors

def factoring (number):
    """factors a number to factors below 9 and returns addnecessity if a prime is reduced then factored"""
    factors=[]
    addnec = [] #addition necessity when factoring primes
    for fac in range(2, 9)[::-1]:
        if number%fac==0:
            addnec = [0]
            factors.append(fac)
            factors.append(number/fac)
            break
    if not factors:
        addnec += [1]
        kansw = factoraprime(number)
        factors += kansw
    tempfac = factors
    for boop in tempfac:
        if boop>8 or boop<-8:
            pansw = factoring(boop)
            factors.remove(boop)
            factors=factors+pansw[0]
            addnec = addnec+pansw[1]
    return [factors, addnec]

def factordecide(number):
    if number>8:
        return factoring(number)
    elif number<=8:
        return [[number], [0]]

def TTBconditionals(faco, addne):
    """this function is made obsolete by the for loop function below but it may be useful in the future as a reference for the template"""
    if len(faco)==2:
        return (('+'*faco[0])+'[->'+('+'*faco[1])+'<]>'+('+'*addne[0])+'.\n>')
    if len(faco)==3:
        return (('+'*faco[0])+'[->'+('+'*faco[1])+'<]>'+('+'*addne[0])+'[->'+('+'*faco[2])+'<]>'+('+'*addne[1])+'.\n>')
    if len(faco)==4:
        return (('+'*faco[0])+'[->'+('+'*faco[1])+'<]>'+('+'*addne[0])+'[->'+('+'*faco[2])+'<]>'+('+'*addne[1])+'[->'+('+'*faco[3])+'<]>'+('+'*addne[2])+'.\n>')
    if len(faco)==5:
        return (('+'*faco[0])+'[->'+('+'*faco[1])+'<]>'+('+'*addne[0])+'[->'+('+'*faco[2])+'<]>'+('+'*addne[1])+'[->'+('+'*faco[3])+'<]>'+('+'*addne[2])+'[->'+('+'*faco[4])+'<]>'+('+'*addne[3])+'.\n>')

def TTBfor(faco, addne):
    """Applies factors and addnecessities to brainfuck template"""
    final = ('+'*faco[0])
    adcount = 0
    for fac in faco[1::]:
        final = final + '[->' + ('+'*fac)+'<]>'+('+'*addne[adcount])
        adcount += 1
    final += '.\n>'
    return final

def texttobrainfuck (text):
    """controls the structure of the final brainfuck string"""
    asciiarray = list(ord(i) for i in list(text))
    fullstore = []
    for character in asciiarray:
        temphold = factoring(character)
        facorder = temphold[0][::-1]
        addnecorder = temphold[1][::-1]
        fullstore.append(TTBfor(facorder, addnecorder))
    fullansw = ''
    for piece in fullstore:
        fullansw+=piece
    return fullansw

"""def TTBnew(text):
    """"""Control program for condensed brainfuck strings idea""""""
    asciiwhole = list(ord(i) for i in list(text))
    asciirelative = [asciiwhole[0]]
    count = 0
    for x in asciiwhole[1::]:
        asciirelative.append(x-asciiwhole[count])
        count += 1
    for num in asciirelative:
        if num<0:"""




#print(factoring(9))
print(texttobrainfuck("Hey, look what I did!"))
#print(TTBnew("The quick brown fox jumps over the lazy dog."))
