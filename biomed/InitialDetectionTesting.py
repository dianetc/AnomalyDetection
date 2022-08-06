#This is where initial anomaly detection testing will take place

from IngestData import *
import matplotlib.pyplot as plt

#Note that there are several samples per patient for some patients.
# => no 1-to-1 between patient and samples
samples = get_sample_data()

 
#first pass: PLOTTING each variable
plt.figure(1)

plt.subplot(411)
data_m1 = get_m1s()
data_m1_carrier = get_m1s('class_type','carrier')
data_m1_normal = get_m1s('class_type','normal')
sc1 = plt.scatter(data_m1_carrier,[0]*len(data_m1_carrier), color="red")
sc2 = plt.scatter(data_m1_normal,[0]*len(data_m1_normal))
average_total_m1 = sum(data_m1)/len(data_m1)
average_carrier_m1 = sum(data_m1_carrier)/len(data_m1_carrier)
average_normal_m1 = sum(data_m1_normal)/len(data_m1_normal)
std_m1 = (sum([((x - average_total_m1)** 2) for x in data_m1]) / len(data_m1))**0.5
low_m1 = average_total_m1 - 3*std_m1
high_m1  = average_total_m1 + 3*std_m1
print("\n")
print("M1 Statistics")
print(f"standard deviation m1: {std_m1}")
print(f"low: {low_m1}")
print(f"high: {high_m1}")
print("\n")
sc3 = plt.scatter(average_total_m1,0, color="green")
sc4 = plt.scatter(average_carrier_m1,0, color="black")
sc5 = plt.scatter(average_normal_m1,0, color="purple")
plt.xlabel("m1")

plt.subplot(412)
data_m2_none = get_m2s()
data_m2 = [d for d in data_m2_none if d is not None] # do not want to keep calling get_m2s()
data_m2_carrier = get_m2s('class_type','carrier')
data_m2_carrier = [d for d in data_m2_carrier if d is not None]
data_m2_normal = get_m2s('class_type','normal')
data_m2_normal = [d for d in data_m2_normal if d is not None]
plt.scatter(data_m2_carrier,[0]*len(data_m2_carrier), color="red")
plt.scatter(data_m2_normal,[0]*len(data_m2_normal))
average_total_m2 = sum(data_m2)/len(data_m2)
average_carrier_m2 = sum(data_m2_carrier)/len(data_m2_carrier)
average_normal_m2 = sum(data_m2_normal)/len(data_m2_normal)
std_m2 = (sum([((x - average_total_m2)** 2) for x in data_m2]) / len(data_m2))**0.5
low_m2 = average_total_m2 - 3*std_m2
high_m2  = average_total_m2 + 3*std_m2
print("M2 Statistics")
print(f"standard deviation m1: {std_m2}")
print(f"low: {low_m2}")
print(f"high: {high_m2}")
print("\n")
plt.scatter(average_total_m2,0, color="green")
plt.scatter(average_carrier_m2,0, color="black")
plt.scatter(average_normal_m2,0, color="purple")
plt.xlabel("m2")

plt.subplot(413)
data_m3 = get_m3s()
data_m3_carrier = get_m3s('class_type','carrier')
data_m3_normal = get_m3s('class_type','normal')
plt.scatter(data_m3_carrier,[0]*len(data_m3_carrier), color="red")
plt.scatter(data_m3_normal,[0]*len(data_m3_normal))
average_total_m3 = sum(data_m3)/len(data_m3)
average_carrier_m3 = sum(data_m3_carrier)/len(data_m3_carrier)
average_normal_m3 = sum(data_m3_normal)/len(data_m3_normal)
std_m3 = (sum([((x - average_total_m3)** 2) for x in data_m3]) / len(data_m3))**0.5
low_m3 = average_total_m3 - 3*std_m3
high_m3  = average_total_m3 + 3*std_m3
print("M3 Statistics")
print(f"standard deviation m1: {std_m3}")
print(f"low: {low_m3}")
print(f"high: {high_m3}")
print("\n")
plt.scatter(average_total_m3,0, color="green")
plt.scatter(average_carrier_m3,0, color="black")
plt.scatter(average_normal_m3,0, color="purple")
plt.xlabel("m3")

plt.subplot(414)
data_m4_none = get_m4s()
data_m4 = [d for d in data_m4_none if d is not None]
data_m4_carrier = get_m4s('class_type','carrier')
data_m4_carrier = [d for d in data_m4_carrier if d is not None]
data_m4_normal = get_m4s('class_type','normal')
data_m4_normal = [d for d in data_m4_normal if d is not None]
plt.scatter(data_m4_carrier,[0]*len(data_m4_carrier), color="red")
plt.scatter(data_m4_normal,[0]*len(data_m4_normal))
average_total_m4 = sum(data_m4)/len(data_m4)
average_carrier_m4 = sum(data_m4_carrier)/len(data_m4_carrier)
average_normal_m4 = sum(data_m4_normal)/len(data_m4_normal)
std_m4 = (sum([((x - average_total_m4)** 2) for x in data_m4]) / len(data_m4))**0.5
low_m4 = average_total_m4 - 3*std_m4
high_m4  = average_total_m4 + 3*std_m4
print("M4 Statistics")
print(f"standard deviation m1: {std_m4}")
print(f"low: {low_m4}")
print(f"high: {high_m4}")
plt.scatter(average_total_m4,0, color="green")
plt.scatter(average_carrier_m4,0, color="black")
plt.scatter(average_normal_m4,0, color="purple")
plt.xlabel("m4")

plt.tight_layout()
plt.figlegend((sc1,sc2,sc3,sc4,sc5), ('carriers', 'normal','average_total','average_carriers','average_normal'), "lower left")

##################################
# CONCLUSION : ANOMALY PRESENT VIA M1,M3,M4
# Issues: 1) negative low doesn't make sense -> need better nethodology that doesn't force normality. 2) are anomalies from same sample ? -> Nope, multiple samples with weirdness on at least one measurement 

idx = []
for i in range(len(data_m1)):
	if data_m1[i] > high_m1:
		idx.append(i)
print("\n")
print("MULTIPLE ANOMALY TEST")
for j in idx:
	print(samples[j].m1)
	print(samples[j].m2)
	print(samples[j].m3)
	print(samples[j].m4)
	print("\n")


##################################

#second pass: PLOTTING each relation between measurements
plt.figure(2)

plt.subplot(311)
sc1 = plt.scatter(data_m1,data_m2_none, color="red")
sc2 = plt.scatter(average_total_m1,average_total_m2,color="green")
plt.xlabel("m1")
plt.ylabel("m2")

plt.subplot(312)
plt.scatter(data_m1,data_m3, color="red")
plt.scatter(average_total_m1,average_total_m3,color="green")
plt.xlabel("m1")
plt.ylabel("m3")

plt.subplot(313)
plt.scatter(data_m1,data_m4_none, color="red")
plt.scatter(average_total_m1,average_total_m4,color="green")
plt.xlabel("m1")
plt.ylabel("m4")

plt.tight_layout()
plt.figlegend((sc1,sc2), ('(m1,m_n)','average'), "lower left")
plt.show()	

