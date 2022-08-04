import numpy as np

cities_temp = {"Amman" :np.array([20,30,50,30,25]) , "Irbid" : np.array([77,50,33,15,20]),"Karak" : np.array([100,80,30,60,55])}

print("Amman Avg Temp ",cities_temp["Amman"].sum() / 5)
print("Irbid Avg Temp ",cities_temp["Irbid"].sum() / 5)
print("Karak Avg Temp ",cities_temp["Karak"].sum() / 5)

print("Amman Min Temp ",cities_temp["Amman"].min())
print("Irbid Min Temp ",cities_temp["Irbid"].min())
print("Karak Min Temp ",cities_temp["Karak"].min())

print("Amman Max Temp ",cities_temp["Amman"].max())
print("Irbid Max Temp ",cities_temp["Irbid"].max())
print("Karak Max Temp ",cities_temp["Karak"].max())
