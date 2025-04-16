# coding: utf-8
# https://www.youtube.com/watch?v=RZBhSi_PwHU&ab_channel=Stand-upMaths
# Calculate Pi inspired by Matt Parker youtube video linked above.
# 2024

from random import random, randint, gauss
from time import sleep, time
from math import gcd, sqrt, pi, floor, ceil, log
import sys
import termplotlib as tpl
import numpy as np
from collections import defaultdict


def fmt_time(Total):
    mins, secs = divmod(Total, 60) 
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    s = ''
    i=0
    for x in [days, hours, mins, secs]: 
        if x>0: 
            s += str(int(x)) + ('' if i==3 else ':') 
        i+=1     
    return s            

if __name__ == '__main__':
    if len(sys.argv) > 1 and 'help' in sys.argv[1].lower():
        print("""Usage: 
`python calculate_pi.py [time] [faces] [graph_w] [graph_h]`
> Calculate pi by simulating repeatedly tossing a random die with [faces] number of faces every [time] seconds.
> time, faces, graph_w, graph_h are optional parameters, with defaults of 5 seconds and 6 faces, and 150x39 graph dimensions.
> eg: 
`python calculate_pi.py 10 64`
> Calculate pi by tossing a D64 every 10 seconds
""")
        exit()
    # random ticker
    i = 0
    Total = 0
    start = time()
    T = .001 if len(sys.argv) < 2  else float(sys.argv[1]) / 2

    # calculating pi 
    Max = 64 if len(sys.argv) < 3 else float(sys.argv[2]) 
    coprimes = 0
    guesses = []

    graph_w = 150 if len(sys.argv) < 4 else float(sys.argv[3]) 
    graph_h = 39  if len(sys.argv) < 5 else float(sys.argv[4])
    tail_f = 0.025 if len(sys.argv) < 6 else float(sys.argv[5])

    errors = []
    gcds = defaultdict(lambda:1)
    gcds_list=[]
    
    while True:
        # random ticker
        x1=abs(gauss(T, T/2.6))
        x2=abs(gauss(T, T/2.6))
        sleep(x1)
        Total += x1

        # calculating pi
        i += 1
        a=randint(1,Max) 
        b=randint(1,Max)
        
        cd = gcd(a,b)
        if cd == 1:
            coprimes += 1
        x = coprimes/i
        our_pi = sqrt(6/x) if x > 0 else 2

        err = (our_pi - pi) / pi * 100
        aerr = abs(err) 
        err_s = ('+'if err>=0 else '') + str(round(err, 0 if aerr >= 10 else 1 if aerr >= 1 else 2 if aerr >= .1 else 3 if aerr >= .01 else 4 if aerr >= .001 else 5)) 

        guesses.append(our_pi)
        errors.append(err)
        gcds[cd]+=1
        gcds_list.append(cd)

        
        x = np.arange(ceil(i/2),i)
        y = np.array(guesses)[x]
        fig1 = tpl.figure()
        fig1.plot(x, y, width=graph_w, height=graph_h, xlabel="Iteration")

        y = np.array(errors)[x]
        fig2 = tpl.figure()
        fig2.plot(x, y, width=graph_w, height=graph_h/2, xlabel="Iteration")


        sorted_gcds = sorted(gcds)
        use = len(sorted_gcds)
        tmp_counter = 0
        for j,g in enumerate(sorted_gcds):
            tmp_counter += gcds[g]
            if tmp_counter >= (1-tail_f)*i:
                use = j + 1
                break

        use = sorted_gcds[:use]
        fig3 = tpl.figure()
        fig3.barh([gcds[x] for x in use], use)
        
        
        print(f'{i})throw . . .  {a} . . . {b}' + ('\tCOPRIME!'if cd==1 else ''))
        print(f'GCD = {cd} = {a}÷{int(a/cd)} = {b}÷{int(b/cd)}')
        print(f'({coprimes}/{i} coprimes/throws)')
        print('\tπ guess: π ≈{1:10f} \t ({0:5s}% error)\t (π ={2:10f})'.format(err_s, our_pi, pi))
        print('\t' + fmt_time(time()-start) + ' seconds elapsed\n')

        print(f'Figure 1.{i}: Guess of π of over time')
        fig1.show()

        print(f'\nFigure 2.{i}: % Error in guess of π of over time')
        fig2.show()

        print(f'\nFigure 3.{i}: GCD frequencies since start ({tail_f} of tail cut off)')
        fig3.show()

        print('\n-----zoom-out---------\n')
                
