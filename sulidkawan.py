greeting = "Hello"
for c in greeting :
    print(c)


for i in range(len(greeting)):
	print(i)
      
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
	
for n in range(12,36,6):
  print(n*2)



input = "Four score and seven years ago"
for c in input:
  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(c)


num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

for x in range(1, 10, 3):
    print(x)