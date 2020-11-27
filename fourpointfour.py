from main import solutions_43,aFty
import numpy as np

def HolePattern(solutions,yieldvalues):
    v = 3120.43
    holelst = []
    boltconfig = []
    for i in solutions:  
        h = 0.0131
        t1 = i[2] 
        tau_max = yieldvalues[i[3]]

        for n in range(2, 20, 2):
            tau_avg = 0
            d2 = 0.5
            while tau_avg < tau_max:
                d2 -=0.001
                fs = v / n
                tau_avg = fs / (np.pi * (d2/2)**2)
            boltconfig.append([n, d2])
                

        n = n + 1
        if n % 2 != 0:
            n = n + 1

        x = []
        f_top = 0
        f_bottom = 0

        for i in range(int(n/2)):
            for a in range(2):
                if i % 2 ==0:
                    x.append(d2 + (f_top * 2 * d2))
                    f_top += 1
                else:
                    x.append(-d2 - (f_bottom * 2 * d2))
                    f_bottom +=1

        length = h + (2*t1) + (4 * d2)
        z = []
        for i in range(n):
            if i % 2 ==0:
                z.append((length/2) - 1.5*d2)
            else:
                z.append(-(length/2) + 1.5*d2)
        r = n * [(d2/2)]

        holespre = []
        for i in range(n):
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes
        r = n * [(d2/2)]

        holespre = []
        for i in range(n):
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes
            holespre.append([r[i], x[i], z[i]])
        holelst.append(holespre)

    return holes

