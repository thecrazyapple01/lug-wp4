import numpy as np

def masscalculator(solutions,rhofastener,rhobackplate,holes,d2):
# backplate
    h = 0.0131 # calculated in 3.1
    t1 = solutions[2]
    t2 = solutions[6]
    w = solutions[0]
    D1 = solutions[1]
    t4 = (w - D)/2
    y = solutions[5]
    rho_fast = 
    rho_backplate = 

    vol_fast = 0.25 * np.pi * d2**2 * t2 * n

    l = (4 * d2) + (2 * t1) + h
    vol_backplate = l * w * t2 - vol_fast

    # lugs
    vol_sqpart = (y - (0.5* w)) * w * t1
    vol_circpart = (0.5 * np.pi * (0.5 * w)**2) * t1
    vol_lugtotal = 2 * (vol_sqpart + vol_circpart - (np.pi * (0.5 * D1)**2 * t1))

    vol_tot = vol_lugtotal + vol_backplate

    m_tot = (vol_fast * rho_fast) + (vol_tot * rho_backplate)

    return m_tot