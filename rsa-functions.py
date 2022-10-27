import random

def prob_prime_test(p): #implements Fermat's Little Theorem probabilistic primality test.
    if pow(2, p - 1, p) == 1:
        return True
    return False

def rand_prime(): #generates a random 50-digit prime number. Uses probabilistic primality test.
    lower_bound = 10**49 + 1
    upper_bound = 10**50
    prime = random.randrange(lower_bound, upper_bound, 2) #generate random 50-digit odd number
    while not prob_prime_test(prime):
        prime = random.randrange(lower_bound, upper_bound, 2)
    return prime

#implementation of Euclidean Algorithm. finds the gcd of two integers.
def gcd(a:int, b:int):
    if a == 0 or b == 0:
        return "Error: division by 0 in gcd"
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

#implementation of Extended Euclidean Algorithm.
#given two positive integers a and b, finds integers x and y such that ax + by = gcd(a, b).
#returns a list containing x, y, and the gcd.
#A proper implementation of this would be able to handle zeroes and negative integers but it'll probably
#only get passed positive ints in this program, so it isn't built for those special cases.
def extended_euclid(r0, r1):
    if r1 == 0 or r0 == 0:
        return [1, 0, r0]
    #initial values for "2 steps previously" x and y, "1 step previously" x and y.
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    #compute first remainder and quotient.
    r2 = r0 % r1
    quotient = r0 // r1
    while r2 != 0:
        #update the xs and ys so that, whatever the current r2 is, it can be written as a linear combination of a and b.
        x0, x1 = x1, x0 - (quotient * x1)
        y0, y1 = y1, y0 - (quotient * y1)
        
        r0 = r1
        r1 = r2
        r2 = r0 % r1
        quotient = r0 // r1
    return [x1, y1, r1]

def find_public_exponent(p:int, q:int):
    #find public exponent, a number relatively prime to (p-1)(q-1)
    phi_p_q = (p-1) * (q-1)
    public = 3
    while gcd(public, phi_p_q) != 1:
        public += 2
    return public

def find_private_exponent(public:int, p:int, q:int):
    #find private exponent, a number D providing a solution to the linear Diophantine equation:
    #          ED = 1 + k(p-1)(q-1)
    #where E is the public exponent and k is a natural number uses the Extended Euclidean Algorithm.
    phi_p_q = (p-1) * (q-1)
    euclid_output = extended_euclid(public, phi_p_q)
    private = euclid_output[0]
    #a negative private key won't work. Thankfully, for linear Diophantine equations, given some number x0 such that
    #ax0 + by0 = c
    #we can always find other solutions by adding (b / gcd(a, b)) to x0.
    while (private < 0):
        private += phi_p_q
    return private

def generate_keys(p:int, q:int):
    #find public exponent, a number relatively prime to (p-1)(q-1)
    public = find_public_exponent(p, q)
    #find private exponent, a number D providing a solution to the linear Diophantine equation:
    #          ED = 1 + k(p-1)(q-1)
    #where E is the public exponent and k is a natural number uses the Extended Euclidean Algorithm.
    private = find_private_exponent(public, p, q)
    modulus = p * q
    return "Your public key is {}. Your public modulus is {}. Your private key is {}.".format(public, modulus, private)
def encrypt_decrypt (key:int, modulus:int, message:int):
    #takes in a key, the public modulus (pq), and a message (a natural number less than the modulus).
    #can be used for encryption or decryption--operations are the same either way.
    
    #checks that the parameters fit the conditions above.
    if (message < 0):
        return "Message is a negative number. Please try again with a positive number."
    if (message >= modulus):
        return "Message too large. Please try again with a message smaller than the modulus."
    if (key < 0):
        return "Key is negative. Try again with a positive key."
    if (modulus < 0):
        return "Modulus is negative. Try again with a positive modulus."
    #raises the message to power given by the key, then reduces with the modulus.
    #returns the resulting value.
    return pow(message, key, modulus)