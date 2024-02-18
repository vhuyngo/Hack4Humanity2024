import sys
# global_timer = 0

start_time_display = 1.2
end_time_display = 1.3
# call outside of loop
global_range = .2
global_start = start_time_display
global_end = end_time_display
# loop

list_times = []
print(f"Initial list Times: {list_times}")
#first iteration 
start_time_display = 1.2
end_time_display = 1.3
global_end = end_time_display
if abs(start_time_display - global_end) < global_range: 
    list_times.append(f"{global_start} - {global_end}")
    print(start_time_display) # print the starting time
else:
    global_start = start_time_display
    if not list_times: # not empty
        list_times.pop()
    list_times.append(f"{global_end}")
print(f"After First Iteration list Times: {list_times}")


# 2nd iteration
start_end_display = 1.3
end_time_display = 1.5
global_end = end_time_display
if abs(start_time_display - global_end) < global_range: 
    list_times.append(f"{global_start} - {global_end}")

    print(start_time_display) # print the starting time
else:
    global_start = start_time_display
    if not list_times: # not empty
        list_times.pop()
    list_times.append(f"{global_end}")
print(f"After Second Iteration list Times: {list_times}")


# 3rd iteration
start_end_display = 1.5
end_time_display = 4.3
global_end = end_time_display
if abs(start_time_display - global_end) < global_range: 
    list_times.append(f"{global_start} - {global_end}")
    print(start_time_display) # print the starting time
else:
    global_start = start_time_display
    if not list_times: # not empty
        list_times.pop()
    list_times.append(f"{end_time_display}")
print(f"After Third Iteration list Times: {list_times}")


# [1.2 - 1.3, 4.3] 
# [1.2, 1.3, 1.4, 1.5, 4.3] => [1.2 - 1.5, 4.3]
# [1.2, 1.3, 1.4, 1.5, 4.3] => [1.2 - 1.5, 4.3]
# s = 1.2
# e = 1.3

# s = 1.3
# e = 1.4

# s = 1.4
# e = 1.5

# s = 1.5
# e = 4.3