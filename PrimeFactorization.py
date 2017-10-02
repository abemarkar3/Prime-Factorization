import os
'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

while True:

    try:

        checker = 0
        num = input('enter number of which you want prime factors: ')
        origNum = num
        primeFactors = []

        for x in [2,3,5,7]:
            if num%x == 0:
                pass
            else:
                checker += 1
            if checker == 4:
                print '{} is Prime'.format(num)
                primeFactors.append(num)
                primeFactors.append(1)

        def makeFactors(which):
            global num

            while num%which == 0:
                num = num/which
                primeFactors.append(which)

        for x in [2,3,5,7]:
            makeFactors(x)

        print 'Prime factors of {} are {} and 1'.format(origNum, primeFactors)

    except NameError:
        print 'please enter a number'
