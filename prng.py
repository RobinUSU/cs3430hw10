from PIL import Image
import numpy as np
import matplotlib.colors as col
import random
import scipy.stats




class prng(object):

    ### ================ Problem 1: Unit Tests =====================

    @staticmethod
    def lcg(a, b, m, n, x0=0):
        """
        returns an lcg generator that generates n random numbers with linear congruential generator
        given a, b, m, n, and x0 (i.e., seed). 
        """
        ### your code here

        def lcg2():
            # Initialize first two Fibonacci Numbers
            # limit = 5
            i = 1
            #a, b = 0, 1
            xn = x0

            # One by one yield next Fibonacci Number
            while i <= n:
                # a, b = b, a + b
                # xn = xn + n
                xn = (a * xn + b) % m
                yield xn
                #a = ()
                i = i+1

        return(lcg2)
        pass

    @staticmethod
    def xorshift(a, b, c, n, x0=1):
        """
        returns a xorshift generator that generates n random numbers with xorshift
        given a, b, c, n, and x0 (i.e., seed). 
        """
        ### your code here

        def xor2():
            i = 0
            xn = x0

            # One by one yield next Fibonacci Number
            while i <= n:
                yield xn
                xn = xn ^ ((xn << a) & 0xFFFFFFFF)
                xn = xn ^ ((xn >> b) & 0xFFFFFFFF)
                xn = xn ^ ((xn << c) & 0xFFFFFFFF)
                i = i+1

        return(xor2)

        pass

    @staticmethod    
    def mersenne_twister(n, x0=1, start=0, stop=1000):
        """
        returns a mersenne twister generator (the python generator) to generate n random numbers 
        given the seed x0 which defaults to 1.
        """
        ### your code here

        #random.randint(start, stop)

        ## A attempt at Mersenne Twister, using Python's Rand fuction
        def merTwist2():
            i = 0
            #xn = x0
            random.seed(x0)

            # One by one yield next Fibonacci Number
            while i <= n:
                xn = random.randint(start, stop)
                yield xn
                i = i+1

        return(merTwist2)

        pass

    @staticmethod
    def __get_byte(i, byte_index):
        i = int(i)
        return ((i >> (8 * byte_index)) % 256 + 256) % 256

    @staticmethod
    def __int_to_rgb(i):
        r = prng.__get_byte(i, 0) / 255
        g = prng.__get_byte(i, 1) / 255
        b = prng.__get_byte(i, 2) / 255
        return [r, g, b]

    @staticmethod
    def gen_lcg_data(a, b, m, n, seed=0, option=1):
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        
        ### option 1) generate n lcg numbers.
        if option == 1:
            return np.array([next(lcgg) for _ in range(n)])

        ### option 2) generate n lcg numbers by
        ### varying the seed from i upto n-1.
        elif option == 2:
            data = np.zeros(n)
            for i in range(n):
                data[i] = next(prng.lcg(a, b, m, 1, x0=i)())
            return data
        
        ### option 3) generate n numbers with numpy arange.
        elif option == 3:
            return np.arange(n)

        else:
            raise Exception('prng.get_lcg_data(): option must be 1,2,3')
      
    @staticmethod
    def gen_xorshift_data(a, b, c, n, seed=1, option=1):
        ### your code here
        pass

    @staticmethod
    def gen_mersenne_twister_data(n, seed=1, start=0, stop=1000, option=1):
        ### your code here
        pass

    @staticmethod
    def gen_pil_image(data, w, h, n, name='tmp', save_flag=True):
        """
        generate a PIL image from data and display/save it.
        """
        img_data = np.zeros((n, 3))
        
        for i, j in enumerate(data):
            img_data[i] = prng.__int_to_rgb(j)

        img_data = img_data.reshape(h, w, 3)
        
        pil_img = Image.fromarray(img_data, 'RGB')
        
        ### save PIL image in the current directory
        if save_flag:
            pil_img.save(name + '.png')
        else:
            pil_img.show()


    ### =============== Problem 3 ===============================
    
    @staticmethod
    def equidistrib_test(seq, n, lower_bound, upper_bound):
        ### your code here
        pass
