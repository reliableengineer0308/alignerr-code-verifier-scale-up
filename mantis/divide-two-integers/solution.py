def divide(dividend, divisor):
    if dividend == 0:
        return 0
    
    # Handle overflow case
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    
    # Determine sign of result
    negative = (dividend < 0) != (divisor < 0)
    
    # Work with absolute values
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)
    
    quotient = 0
    while dividend_abs >= divisor_abs:
        temp = divisor_abs
        multiple = 1
        
        # Double the divisor until it's larger than remaining dividend
        while dividend_abs >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        dividend_abs -= temp
        quotient += multiple
    
    # Apply sign
    if negative:
        quotient = -quotient
    
    return quotient