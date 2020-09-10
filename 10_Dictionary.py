#10- Dictionary

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"} #Key: Value
print(dict1["IOS"])
dict1["RAM"] = "128"
print(list(dict1))
del dict1["Ports"]
print(list(dict1))
print(len(dict1))
print("IOS" in dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())