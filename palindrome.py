# Check if a givens string is a palindrome
def palidrome(a):
  if a == a[::-1]:
    print("True!")
  else:
    print("False")


a = "madam" # "radar" # "mom" # "aspirin"
palidrome(a)
