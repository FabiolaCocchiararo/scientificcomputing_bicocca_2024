import numpy as np

def roche_lobe_primary(a,e,q):
    num = 0.49*q**(-2./3.)*a*(1.-e)
    den = 0.6*q**(-2./3.)+np.log(1.+q**(-1./3.))
    
    return num/den

def roche_lobe_secondary(roche_lobe1, q):
    return roche_lobe1*q**(0.46)
