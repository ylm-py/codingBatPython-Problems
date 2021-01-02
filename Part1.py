'''The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
 We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.'''
 
def sleep_in(weekday, vacation):
    return not weekday or vacation


'''We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.'''

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else :
        return False

'''Given two int values, return their sum. Unless the two values are the same, then return double their sum.'''

def sum_double(a, b):
    if a != b :
        return a + b
    else :
        return (a + b) * 2

'''Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.'''

def diff21(n):
    if n > 21:
        return abs((n - 21) * 2)
    else :
        return abs(n - 21)

'''We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.'''

def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20) :
        return True
    else :
        return False

'''Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.'''

def makes10(a, b):
    return (a == 10 or b == 10 or a+b == 10)

'''Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.'''

def near_hundred(n):
    if abs( 100 - n ) <= 10 or abs ( 200 - n ) <= 10 :
        return True
    else :
        return False

'''Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.'''

def pos_neg(a, b, negative):
    if negative:
        return(a < 0 and b < 0)
    else :
        return ((a > 0 and b < 0) or (a < 0 and b > 0))

'''Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.'''

def not_string(str):
    if len(str) >= 3 and str[:3] == "not" :
        return str
    return "not " + str

'''Given a non-empty string and an int n, return a new string where the char at index n has been removed.
 The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).'''

def missing_char(str, n):
    new_str = str.replace(str[n],'')
    return new_str


'''Given a string, return a new string where the first and last chars have been exchanged.'''


def front_back(str):
    if len(str) <= 1 :
        return str
    else:
        first_char = str[0]
        last_char = str[-1]
        new_str = last_char + str[1:-1] + first_char
        return new_str


'''Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.'''


def front3(str):
    if len(str) < 3:
        return str * 3
    else:
        return str[0:3] * 3


'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".'''


def string_bits(str):
    new_str = ''
    for char in range(len(str)):
        if char % 2 == 0:
        new_str += str[char]
    return new_str


'''Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".'''

def hello_name(name):
  return'Hello ' + name + '!'


'''Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".'''


def make_abba(a, b):
  return a + b + b + a


'''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
 Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".'''


 def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'


'''Given an "out" string length 4, such as "<<>>", 
and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".'''


def make_out_word(out, word):
  return  out[:2] + word + out[2:]


'''Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2.'''


def extra_end(str):
  return str[-2:] * 3


'''Given a string, return the string made of its first two chars, 
so the String "Hello" yields "He". If the string is shorter than length 2, 
return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".'''


def first_two(str):
  if len(str) > 2:
    return str[:2]
  else:
    return str


'''Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".'''


def first_half(str):
  return str[:len(str)/2]


'''Given a string, return a version without the first and last char, 
so "Hello" yields "ell". The string length will be at least 2.'''


def without_end(str):
  return  str[1:-1]


'''Given 2 strings, a and b, return a string of the form short+long+short,
 with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).'''


def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else :
    return a + b + a

'''Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.'''


def non_start(a, b):
  return a[1:] + b[1:]


'''Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.'''


def left2(str):
  return str[2:] +   str[:2]


'''When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60,
 inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars.
  Return True if the party with the given values is successful, or False otherwise.'''


def cigar_party(cigars, is_weekend):
  a = range(61)
  if is_weekend and cigars not in a:
    return True

  elif cigars in range(40,61):
    return True

  else:
    return False


'''You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, 
in the range 0..10, and "date" is the stylishness of your date's clothes. 
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, 
then the result is 0 (no). Otherwise the result is 1 (maybe).'''


def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  
  if you >= 8 or date >= 8 :
    return 2
  
  else :
    return 1