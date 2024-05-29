import numpy as np
import scipy.stats as ss
from scipy.stats import norm

class Parity :
    def __init__(self) -> None : 
        pass
    def ver (put,call,S,K,r,T):
        for i in range (0,len(put)):
            if (call[i]-put[i]==S[i]-K*np.exp(-r*T)):
                print("Results verified")    
            else : 
                print('Results unverified ')
            return 
        

class MC_Error:
    def __init__(self) -> None : 
        pass
    def error(call,put):
        call_err = np.std(call)
        print("Call error:",call_err) # standard error
        put_err = np.std(put)
        print("Put error: ", put_err)  # standard error
            
