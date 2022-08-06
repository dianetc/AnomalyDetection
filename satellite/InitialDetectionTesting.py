#This is where initial anomaly detection testing will take place

from IngestData import *
import matplotlib.pyplot as plt

#Note that there are several samples per patient for some patients.
# => no 1-to-1 between patient and samples
samples = get_sample_data()

 
#first pass: PLOTTING each variable
plt.figure(1)

plt.subplot(211)
data_periods = get_periods()
data_periods_USA = get_periods('operator_country', 'USA')
plt.scatter(data_periods,[0]*len(data_periods))
plt.scatter(data_periods_USA,[0]*len(data_periods_USA),color="red")
plt.xlabel("period")

plt.subplot(212)
data_powers = get_powers()
plt.scatter(data_powers,[0]*len(data_powers))
plt.xlabel("power")


plt.tight_layout()
plt.show()

