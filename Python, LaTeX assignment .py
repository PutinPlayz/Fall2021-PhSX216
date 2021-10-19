#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

def fred(a,b):
    c = (a+b)*12
    return c

a = 13.2
b = 3.9

c = fred(a,b)

# the print command completes this code

print("c = ", c)




#---------------------------------------

x = np.array([ 1.1, 1.3, 1.4, 0.9, 0.95, 1.05])
xmean = np.average(x)
xstdev = np.std(x)
n = x.size
errxmean = xstdev/np.sqrt(n)

print ("The mean of the data set is: ", xmean)
print ("The error in the mean is: ", errxmean)




# $\delta x = \Delta \sigma $
# 
# $\frac{m}{\delta m_1} $
# 
# $\sqrt{y+x^2}$

# In[12]:


#Rule 1
import numpy as np

def rule1(c, da):
    dQ = c*da
    return dQ
d1 = 0.005
c = 9.8
errd1 = 0.0005
df = c*d1
errdf = rule1(c,errd1)

print("df =", df)
print("errdf =", errdf)


# In[13]:


#Rule 2
import numpy as np

def rule2(dA, A, Q, m):
    dQ = Q*(m*(dA/A))
    return dQ
a = 0.06
da = 0.0005
M = 2
q = 5
errq = rule2(da, a, M, q)

print("q = ", q)
print("errq =", errq)


# In[9]:


#Rule 3
import numpy as np

def rule3(da, db):
    dQ = np.sqrt(da**2+db**2)
    return dQ

d1 = 1.0
d2 = 0.3
errd1 = 0.0005
errd2 = 0.0005
dtotal = d1 + d2
errdtotal = rule3(errd1, errd2)
print("dtotal =", dtotal)
print("errdtotal =", errdtotal)


# In[26]:


#Rule 4
import numpy as np

def rule4(A, dA, m, B, dB, n, Q):
    
    dQ = Q*np.sqrt((m*(dA/A))**2+((n*(dB/B))**2))
    
    return dQ

y = .99
xavg = 1.57
erry = 0.0005
errx = .0055
g = 9.81
m = 1
n = 1

vi = xavg*np.sqrt(g/(2*y))
errvi = rule4(y, erry, m, xavg, errx, n, vi)

print("vi = ", vi)
print("errvi = ", errvi)
print("There was a slight error in our human calculations of vi, the number we calculated was 3.509 ")


# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$
# 
# 
# $\delta v_i = v_i\sqrt{(\frac{\delta x}{x})^2 + (\frac{\delta y}{y})^2}$

# In[ ]:





# In[ ]:




