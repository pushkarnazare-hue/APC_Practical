from mathutils import basic, number, statistics

print("Addition:", basic.add(10, 5))
print("Is 7 prime:", number.is_prime(7))
print("Is 153 Armstrong:", number.is_armstrong(153))

nums = [10, 20, 30, 40]
print("Mean:", statistics.mean(nums))
print("Maximum:", statistics.maximum(nums))
print("Minimum:", statistics.minimum(nums))
