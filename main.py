"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bitshift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    xvec,yvec = pad(x.binary_vec,y.binary_vec)
    if binary2int(xvec).decimal_val <=1 and binary2int(yvec).decimal_val <= 1:
        res=BinaryNumber(binary2int(xvec).decimal_val * binary2int(yvec).decimal_val)
        return res.binary_vec
    else:
        left_x,left_y = split_number(xvec)
        right_x,right_y = split_number(yvec)
        n=0
        for i in x.binary_vec:
            n+=1
        left = BinaryNumber(binary2int(left_x.binary_vec).decimal_val * binary2int(left_y.binary_vec).decimal_val)
        left = bitshift(left,n)
        mid1 = binary2int(left_x.binary_vec).decimal_val + binary2int(right_y.binary_vec).decimal_val
        mid2 = binary2int(right_x.binary_vec).decimal_val + binary2int(left_y.binary_vec).decimal_val
        mid = bitshift(BinaryNumber(mid1 + mid2),n//2)
        right = BinaryNumber(binary2int(right_x.binary_vec).decimal_val * binary2int(right_y.binary_vec).decimal_val)
        res = left.decimal_val + mid.decimal_val + right.decimal_val
        return BinaryNumber(res)
    



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

print(quadratic_multiply(BinaryNumber(2),BinaryNumber(2)))
