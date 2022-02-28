import math

number_remaining = 3e6 # this is number of atoms remaining
number_starting = 7e2 # this is the number of atoms that start in the decay
time = 4236 # the time of decay (in seconds)

def calculate_lambda(N, N_o, t):
    """
    This function will return a tuple with the value of lambda and the value
    of t_0.5.
    """

    decay_constant = math.log(N/N_o)/t
    half_life = math.log(2)/decay_constant

    return (decay_constant, half_life)

values_nuc_x = calculate_lambda(number_remaining, number_starting, time)

print('The value of lambda is:', values_nuc_x[0], '1/s',
        '\nThe value of the half life is:', values_nuc_x[1], 's')
