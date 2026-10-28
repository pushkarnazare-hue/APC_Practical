day1_visitors = {101, 102, 103, 104}
day2_visitors = {103, 104, 105, 106}
print("Unique visitors across both days:", day1_visitors | day2_visitors)
print("Returning visitors:", day1_visitors & day2_visitors)
print("Visitors only on day 1:", day1_visitors - day2_visitors)
print("Visitors only on day 2:", day2_visitors - day1_visitors)