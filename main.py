n = int(input("Enter number of requests: "))
requests = [0] * n

for i in range(n):
    requests[i] = int(input(f"Enter request {i+1}: "))

if len(requests) != len(set(requests)):
    print("Duplicate values detected.")
else:
    print("No duplicate values detected.")

full_name = input("Enter your full name: ")
full_name_without_spaces = full_name.replace(" ", "")
L = len(full_name_without_spaces)
print("Length of Name:", L)

PLI = L % 3

no_demand = [0] * n
low_demand = [0] * n
moderate_demand = [0] * n
high_demand = [0] * n
invalid_requests = [0] * n

no_index = 0
low_index = 0
moderate_index = 0
high_index = 0
invalid_index = 0
t_valid = 0

for r in requests:

    if r < 0:
        invalid_requests[invalid_index] = r
        invalid_index += 1

    elif r == 0:
        no_demand[no_index] = r
        no_index += 1
        t_valid += 1

    elif 1 <= r and r <= 20:
        low_demand[low_index] = r
        low_index += 1
        t_valid += 1

    elif 21 <= r and r <= 50:
        moderate_demand[moderate_index] = r
        moderate_index += 1
        t_valid += 1

    elif r > 50:
        high_demand[high_index] = r
        high_index += 1
        t_valid += 1

no = no_demand[:no_index]
low = low_demand[:low_index]
moderate = moderate_demand[:moderate_index]
high = high_demand[:high_index]
invalid = invalid_requests[:invalid_index]

print("--- Before Filtering ---")
print("No Demand:", no)
print("Low Demand:", low)
print("Moderate Demand:", moderate)
print("High Demand:", high)
print("Invalid Requests:", invalid)
print("PLI Value:", PLI)

removed_count = 0

if PLI == 0:
    print ("Low demand requests are removed")
    removed_count = low_index
    low_index = 0

elif PLI == 1:
    print ("High demand requests are removed")
    removed_count = high_index
    high_index = 0

elif PLI == 2:
    print ("Only Moderate demand requests are displayed")
    removed_count = no_index + low_index + high_index
    no_index = 0
    low_index = 0
    high_index = 0

no_final = no_demand[:no_index]
low_final = low_demand[:low_index]
moderate_final = moderate_demand[:moderate_index]
high_final = high_demand[:high_index]
invalid_final = invalid_requests[:invalid_index]

all_valid_final = no_final + low_final + moderate_final + high_final

print("---- After Filtering -----")
print("No Demand:", no_final)
print("Low Demand:", low_final)
print("Moderate Demand:", moderate_final)
print("High Demand:", high_final)
print("Invalid Requests:", invalid_final)
print("Total Valid Requests:", len(all_valid_final))
print("Requests Removed due to PLI:", removed_count)

if all_valid_final:
    peak = max(all_valid_final)
    print("Peak Demand Value:", peak)
else:
    print("No valid requests to identify peak value.")
