def express_as_float( x, unit ): # Is this useful?
    print x, unit
    print x / unit( 1.0 )
    
# TODO: Decorators for converting old functions to use units / return units
#
#
# i.e. 
# 
# @parameter_units( 'a', km )
# @parameter_units( 'b', km )
# @parameter_units( 'c', s )
# @function_units_wrapper( 'f', ... )
# @return_units( km )
# def f( a, b, c, function )


# TODO: Out of box way to work with numpy?
