import numpy as np

price = np.array([29,99,24,91,19,32,54,67,89])
print("max price: ",np.max(price))
print("min price: ",np.min(price))
print("average price: ",np.mean(price))
print("price>30 ",price[price>30])
