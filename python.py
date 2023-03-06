

print("python code is running")

fruits = ["Mango","Banana","Orange"];

for x in fruits: 
  print(x);


def my_function(a,b) : 

  if b > a:
    print("b is greater than a")
  else:
    print("a is greater then b")

  
my_function(40,30)

print(type(True));

def find_largest_number(numbers):
  largest = numbers[0];
  for number in numbers : 
    if number>largest: 
        largest = number
  return largest;


print(find_largest_number([10,20,30,40,50]))
