import matplotlib.pyplot as plt
import random
from collections import Counter
values = []
frequency = []
average_value_x = []
value_frequency_y = []
sample_size = 100
number_of_samples =100000

def sample_generator(average,sample_size):
    for x in range(0,sample_size):
       average += random.randint(1,6)
    values.append(average/sample_size)

def Central_Limit_theorem(sample_size,number_of_samples):
    for x in range(0,number_of_samples):
        sample_generator(0,sample_size)

Central_Limit_theorem(sample_size,number_of_samples)
frequency.append(Counter(values))

for index in range(len(frequency)):
    for key in frequency[index]:
        value_frequency_y.append(frequency[index][key])
        average_value_x.append(key)

plt.plot(average_value_x,value_frequency_y,'o')
plt.show()
