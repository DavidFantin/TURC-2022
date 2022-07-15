################################
# Contributors: David Fantin, Cameron Walker
# Purpose: testing the kappa_velocity_3D() function from PlasmaPy
# TURC Summer 2022
################################

from operator import length_hint
from cdasws import CdasWs
import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
from plasmapy.particles import *
from plasmapy.formulary import *

# Without this the code wont run, it suppresses various warnings
import warnings
warnings.simplefilter(action='ignore')

# Enable plotting support for astropy.units
from astropy.visualization import quantity_support
quantity_support()

## Getting data from WI_K0_3DP
params = ['sc_position','sc_velocity','elect_flux','elect_density','elect_vel','elect_temp','elect_qdotb','ion_flux','ion_density','ion_vel','ion_temp']


# get_data([__], [__], [_start-time_], [_end-time_])
# start/end-time format: [_Year_]-[_month_]-[_day_]T[_hour_]:[_minute_]:[_second_].[_millisecond_]Z
stat, data = CdasWs().get_data('WI_K0_3DP', params, '2020-07-11T00:00:00.000Z', '2020-07-12T00:00:00.000Z')

## Get number of datapoints available 
datalength = len(data['elect_vel'])

# electron_Vel contains all the electron velocity data at each timestamp
electron_Vel = data['elect_vel']

# electron_Temp contains the temperatures recorded for the electrons at each timestamp
# Note: the initial data from NASA are in eV units
electron_Temp = list(data['elect_temp'] * u.eV)

# Converting eV to Kelvin (I used list comprehention to keep it simple, but it is just converting each element using the plasmapy.units package)
electron_Temp = [x.to("K", equivalencies=u.temperature_energy()) for x in electron_Temp]

## X coordinate for electron velocity list initialization
electron_X = []

## Y coordinate for electron velocity list initialization 
electron_Y = []

## Z coordinate for electron velocity list initialization
electron_Z = []

# Note: the kappa_velocity_3D() function takes in cartesian coordinates, so this may affect our output, since NASA's data is in GSE

# parsing all of the X-component velocity data for electrons (GSE coordinates) into the list: electron_X
for i in range(0,datalength):
    electron_X.append(electron_Vel[i][0]*(u.m / u.s))

# parsing all of the Y-component velocity data for electrons (GSE coordinates) into the list: electron_Y
for i in range(0,datalength):
    electron_Y.append(electron_Vel[i][0]*(u.m / u.s))

# parsing all of the Z-component velocity data for electrons (GSE coordinates) into the list: electron_Z
for i in range(0,datalength):
    electron_Z.append(electron_Vel[i][0]*(u.m / u.s))

# Kappa parameter
kappa = 3.1/2

# The 3D kappa distribution function. Outputs a scalar with units: s^3 / m^3
## Note: I am not yet sure how this actually helps us, because we can't plot this, I believe there should a distribution curve for each timestamp
for i in range(0,datalength): # to iterate through all timestamps
    kappa_VDF = kappa_velocity_3D(vx=electron_X[i], vy=electron_Y[i], vz=electron_Z[i], T=electron_Temp[i], kappa=kappa, particle='e')
    print(kappa_VDF)

#######################################
# I would love to somehow plot the distribution, but I dont think we will be able to do that with this function
# Somehow we will need to get number density from this