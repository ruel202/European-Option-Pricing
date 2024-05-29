import numpy as np
import scipy.stats as ss
from scipy.stats import norm


class BlackScholes:
    def __init__(self) -> None :
        pass
    def blackscholes (t,r,S,K,T):
        mu=1
        sigma= np.std(S)
        call= []
        put=[]
        for i in range(0,len(S)):
            mu= mu*(S[i]-S[i-1])/2
            d1= 1/sigma*(np.sqrt(T-t))*(np.log(S[i]/K) + (r+ (sigma**2/2)*T)/(sigma*np.sqrt(T-t)))
            d2= d1- sigma*np.sqrt(T-t)
            call_i = S[i]*norm.cdf(d1,mu,sigma)-K*np.exp(-r*(T-t))*norm.cdf(d2,mu,sigma)
            call.append(call_i)
            put_i= K*np.exp(-r*(T-t))*norm.cdf(d2,0,1)-S[i]*norm.cdf(d1,mu,sigma)
            put.append(put_i)
        return call,put

   
class Binomial:
    def __init__(self) -> None :
        pass
    
        """
    N = number of binomial iterations
    S0 = initial stock price
    u = factor change of upstate
    r = risk free interest rate per annum
    K = strike price constant
    """
    def binomial(T,S,K,r,n) :
        delta= float(T)/n
        sigma= np.std(S)
        u = np.exp(sigma*np.sqrt(delta))#up factor
        d=1.0/u#down factor
        a=np.exp(r*delta)
        p = (a - d) / (u - d)  # risk neutral up probability
        q = 1.0 - p  # risk neutral down probability
        S_fin=([(S[i]* u**j * d ** (n- j)) for i in range (0,len(S)) for j in range (n+1)])
        call= ([np.maximum(S_fin[i]-K,0.0) for i in range (len(S))])
        put= ([np.maximum(K-S_fin[i],0.0) for i in range (len(S))])
        for i in range(n- 1, -1, -1):
            call_i= np.exp(-r * delta) * (p * call[i] + q * put[i])
            put_i= np.exp(r * delta) * (p * call[i] + q * put[i])
        return call_i,put_i

  
class MonteCarlo:
    def __init__(self) -> None :
        pass
    def monte_carlo(T,S,K,r,n):
        delta = T/365
        sigma= np.std(S)
        mu=np.mean(S)
        W= np.random.normal(mu, sigma**2,n)
        drift= r-0.5*sigma**2
        call=[]
        put=[]
        final_price= ([S[i]*np.exp(drift*delta-sigma*W) for i in range (0,len(S))])
        for i in range (0,len(final_price)):
            call.append(np.maximum(final_price[i]-K,0 ))
            put.append(np.maximum(K-final_price[i],0))
        call_t=np.mean(call)
        print("Call option:",call_t)
        put_t=np.mean(put)
        print("Put option", put_t)
        return call_t, put_t


                







        
        
