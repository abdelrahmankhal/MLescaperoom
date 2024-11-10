data = [2.3, 3.1, 4.5, 5.6, 7.2]
size_60 = int(len(data) * 0.6)
data_60 = data[:size_60]  
data_40 = data[size_60:]
print(f"Data_60: {data_60}")
print(f"Data_40: {data_40}")