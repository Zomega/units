"""Math functions for qunatities with units."""
""" Designed as a drop in replacement for the default python math library."""

import math
import collections

from composed_unit import ComposedUnit

pi = math.pi

def sqrt( x ):
    if not hasattr(x, 'num'):
        return math.sqrt( x )
        
    x_unit = x.get_unit()
    x_num = x.get_num()
    
    numer, denom, multiplier = x_unit.numer, x_unit.denom, x_unit.multiplier
    
    new_numer = []
    numer_counter = collections.Counter(numer)
    for element in numer_counter:
        assert numer_counter[element] % 2 == 0 # If not, raise UnitMathException...
        new_numer.extend( [element] * ( numer_counter[element] / 2 ) )
        
    new_denom = []
    denom_counter = collections.Counter(denom)
    for element in denom_counter:
        assert denom_counter[element] % 2 == 0 # If not, raise UnitMathException...
        new_denom.extend( [element] * ( denom_counter[element] / 2 ) )
        
    new_multiplier = math.sqrt( multiplier )
    
    new_unit = ComposedUnit( new_numer, new_denom, new_multiplier )
    return new_unit( math.sqrt( x_num ) )
