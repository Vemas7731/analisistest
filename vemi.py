nama = "Vemi"
nama[1:3]

print("abd" in "abcde")

test = "How much wood would a woodchuck chuck"
print(test.count("wood"))


def is_palindrome(input_string):
    # Inisialisasi dua variabel untuk menyimpan string baru tanpa spasi
    # dan string dalam urutan terbalik
    new_string = ""
    reverse_string = ""

    # Iterasi melalui setiap huruf dalam input_string
    for letter in input_string:

        # Jika karakter bukan spasi
        if letter != " ":

            # Tambahkan huruf ke new_string dan tambahkan ke depan di reverse_string
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string

    # Bandingkan apakah new_string dan reverse_string sama
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

# Select Run to compare the two results.