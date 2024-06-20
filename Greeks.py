import numpy as np
import pandas as pd
import math
from math import sqrt
from scipy.stats import norm

'''there are 5 factors affecting options theoretical price: underlying asset price, strike price, time to maturity(T-t), return volatility and risk-free rate. Apart from strike price, other four factors are time-varying. In order to study the relationships between these four factors and options price, Greeks are invented to quantify the relationships. They are delta, gamma, vega, theta and rho.'''
class BS_greeks:
    def __init__(self, S, K, r, sigma, T):     
        self.S= S # initial price of underlying asset
        self.K = K # strike price at day t 
        self.r = r # risk-free rate
        self.sigma = sigma # volatility
        self.T = T # Maturity date
        self.d1= 1/sigma*(np.sqrt(T))*(np.log(S/K) + (r+ (sigma**2/2)*T)/(sigma*np.sqrt(T)))
        self.d2= self.d1- sigma*np.sqrt(T)  
    def price(self):
        c= self.S*norm.cdf(self.d1)- self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        p = self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2) - self.S*norm.cdf(-self.d1)
        return c,p
    def delta(self):
        c_delta= norm.cdf(self.d1)
        p_delta=c_delta-1
        return c_delta,p_delta
    def gamma(self):
        c_gamma= norm.cdf(self.d1)/(self.S*self.sigma*np.sqrt(self.T))
        p_gamma=p = norm.pdf(self.d1)/(self.S*self.sigma*np.sqrt(self.T))
        return c_gamma, p_gamma
    def theta(self):
        c_theta= -self.S*norm.pdf(self.d1)*self.sigma / (2*np.sqrt(self.T)) - self.r*self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        p_theta=-self.S*norm.pdf(self.d1)*self.sigma / (2*np.sqrt(self.T)) + self.r*self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        return c_theta,p_theta
    def vega(self):
        c_vega= self.S*np.sqrt(self.T)*norm.cdf(self.d1)
        p_vega=c_vega
        return c_vega, p_vega
    def rho(self):
        c_rho=self.K*self.T*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        p_rho=-self.K*self.T*np.exp(-self.r*self.T)*norm.cdf(-self.d2)
        return c_rho,p_rho

    