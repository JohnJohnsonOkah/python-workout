"""
Create an HTML page containing number series 1 - 1000
where - 10th numbers are in bold
      - 3rd numbers are in italics &
      - prime numbers are underlined
"""


def is_prime(number):
    """ check if number is prime"""
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
    return False


mylist = [*range(1, 1001)]  # list of numbers, 1 - 1000

for index, value in enumerate(mylist):
    if value % 10 == 0:  # make multiplies of 10 bold
        mylist[index] = f"<b>{value}</b>"
    if value % 3 == 0:  # make multiples of 3 italics
        mylist[index] = f"<i>{value}</i>"
    if is_prime(value):  # underline prime numbers
        mylist[index] = f"<u>{value}</u>"

# convert list to string
text = " ".join(str(e) for e in mylist)

# create html file of the generated solution
file = open("sample.html", "w")
file.write(text)
file.close()
