#comments
# str
# int
# float
# bool
# bytes
name: str = "John Doe"
age = 20
aggregate: float = 77.9
is_raining: bool = False

x: tuple = [1, 2, 3, 3]
list_names = ["John", "Mary"]

print(x)
print(list_names)

nums: list = [2, 3, 4, 1, 34, 123, 321, 50]

data: dict = {'name': 'Tom', 'age': 20}
print(data)
print(nums)

def get_largest(numbers, n):
    
    numbers.sort(reverse=True)
    return numbers[:n]
sorted_list = get_largest(nums, 8)

print(sorted_list)

for x in range(1, 11):
    print(x)
    

fruits = ["Apple", "Banana", "Kiwi", "Tomato"]

for i in fruits:
    print(i)
    
    if i == "Banana":
        break
    

for j in range(4, 40, 3):
    print(j)
    
    
m = 1

while m < 7:
    print(m)
    m = m + 1
    
else:
    print("i is not less that 7")