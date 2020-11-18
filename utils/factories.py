def restricted_integer_factory(lower=None, upper=None):
    """A class factory that creates a RestrictedInteger class. The class
    is a subclass of integers which places a lower- and/or upper-bound
    on the value an integer can take.

    Parameters:
        lower   The lower-bound of a valid RestrictedInteger integer
        upper   The upper-bound of a valid RestrictedInteger integer

    Return:
        Returns a RestrictedInteger class that restricts an integer to
        the given lower and/or upper bounds.
    """
    # Prepare an informative error string in case the input value to the
    # RestrictedInteger class is invalid.
    errstr = "Invalid RestrictedInteger value {}."
    if upper is not None and lower is not None:
        errstr += f" Value must be between {lower} and {upper}."
    elif lower is not None:
        errstr += f" Value must be greater than or equal to {lower}"
    elif upper is not None:
        errstr += f" Value must be less than or equal to {upper}."

    # Prepare a function that validates that the input value meets the
    # RestrictedInteger class' restrictions.
    def valid_value(value):
        if upper is not None and value > upper:
            return False
        if lower is not None and value < lower:
            return False
        return True

    # Now create the class that will restrict the possible integer value.
    class RestrictedInteger(int):
        def __new__(cls, value):
            integer = int.__new__(cls, value)

            if not valid_value(integer):
                raise ValueError(errstr.format(integer))

            return integer

    return RestrictedInteger
