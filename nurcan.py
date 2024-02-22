def colculate_series_sum(epshilon
s=0
z=1
n=1
while z>epsilon:
     s +=z
     n +=1
     z=1/n*n
return s 
epsilon=0.001
result = calculate_serious_sum(epsilon)
print("S=", result)