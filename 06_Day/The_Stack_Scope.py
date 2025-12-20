def calculate_area(radius : float ) -> float:
    '''Returns area of circle. Inputs float.'''
    if radius<0:
        return 0
    return 3.14*(radius**2)
# Main Execution
r=5
print(calculate_area(r))