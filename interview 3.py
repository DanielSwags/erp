def palindrome_chain_length(n):
    num = str(n)
    rev_num = ""
    x = len(num) - 1
    for i in range(x, -1, -1):
        digit = num[i]
        rev_num = rev_num + digit
    return rev_num


def is_palindrome(n):
    num = str(n)
    rev_num = palindrome_chain_length(n)
    return num == rev_num


numb = input("Please enter a number")
number = int(numb)
step = 0
limit = 5000

while (not is_palindrome(number) and step < limit):
    step = step +1
    rev_num = palindrome_chain_length(number)
    print('step', step, ':',number, '+', rev_num, '=')
    number = number + int(rev_num)
    print(number)
