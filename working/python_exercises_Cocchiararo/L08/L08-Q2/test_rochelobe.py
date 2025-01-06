import numpy as np
import pytest
from rochelobe import roche_lobe_primary, roche_lobe_secondary

def test_roche_lobe_primary_circular_orbit():
    a = 1  
    e = 0  
    q = 1 
    roche_lobe = roche_lobe_primary(a, e, q)
    
    assert pytest.approx(roche_lobe, 0.01) == 0.3789

def test_roche_lobe_primary_eccentric_orbit():
    a = 1
    e = 0.2  
    q = 0.5 
    roche_lobe = roche_lobe_primary(a, e, q)
    
    assert pytest.approx(roche_lobe, 0.01) == 0.352

def test_roche_lobe_secondary():
    roche_lobe1 = 0.3789  
    q = 1  
    roche_lobe2 = roche_lobe_secondary(roche_lobe1, q)
    
    assert pytest.approx(roche_lobe2, 0.01) == 0.3789

