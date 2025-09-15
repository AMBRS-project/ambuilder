# This driver script is adapted from runMe_standalone.py, and is covered by the
# same LGPL license as mphys-1-moment-sectional. It differs from
# runMy_standalone.py in the following ways:
# 1. It accepts input from an `input` module instead of specifying it inline
# 2. It writes size distribution information to 'dNdlogDp.dat' instead of
#    generating plots
# 3. In its final form, it has the contents of get_coag_kernel.py and
#    dNdt_all.py appended to it so the script is self-contained.

# make sure we can find the input module in our current directory
import sys
sys.path.append('.')

from pylab import *
from scipy.integrate import odeint

################
# Input
################

# fetch input variables from our input module
from input import *

################
# Code
################

# initialize bin sizes
dia=logspace(log10(lower_limit),log10(upper_limit),nbins+1)
diam=sqrt(dia[:-1]*dia[1:])
dDp=dia[1:]-dia[:-1]
dlogDp=log10(dia[1:]/dia[:-1])
xk=density*pi/6.*dia**3
xkm=density*pi/6.*diam**3

kna = 2*mfp/diam # knudson #
beta = (1.+kna)/(1.+2.*kna*(1.+kna)) # noncontinuum correction

ftimes=linspace(0.,tfinal,num_times)
btimes=-ftimes

# initialize size distribution
Nk=zeros((nbins))
dNdDp = zeros((nbins)) # number per bin per box
for m in range(0,len(No)):
    dNdDp = dNdDp+No[m]/(sqrt(2.*pi)*(diam)*log(sigma[m])) \
       *exp(-((log(Dpm[m]/diam))**2./ \
       (2.*(log(sigma[m]))**2.)))
Nk=dNdDp*dDp
Nki=Nk
#Mk=Nk*xkm
#Mki=Mk

coag_kernel = get_coag_kernel(temp,pres,density,nbins,\
                              diam,xkm)

inputs=Nk

soln = odeint(dNdt_all,inputs,ftimes,\
         args=(nbins,coag_kernel,coag_eff,xkm,diam,beta,H2SO4,NucScale,doNucCondCoag))


print('Initial total number =', soln[0,:30].sum())
print('Final total number =', soln[-1,:30].sum())
print('Ratio =', soln[-1,:30].sum()/soln[0,:30].sum())

dNdlogDp=soln[:,:]/dlogDp

if dNdlogDp.min() < -1E-6: 
   print('ERROR! non-trival negative values after odeint!')

dNdlogDp[where(dNdlogDp<0.)]=0. # some values were just < 0.

################
# Output
################

from numpy import savetxt
numpy.savetxt('dNdlogDp.dat', dNdlogdp)

################
# Dependencies
################
