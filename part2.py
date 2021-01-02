'''The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
 Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, 
 return True if the squirrels play and False otherwise.'''


def squirrel_play(temp, is_summer):
  if is_summer and 60 <= temp <= 100:
    return True
  if 60 <= temp <= 90:
    return True
  else:
    return False


'''You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.'''


def caught_speeding(speed, is_birthday):
    d = {0: lambda x: x <= 60, 1: lambda x: 60 < x < 81, 2: lambda x: x > 80}
    for ticket, condition in d.items():
        if condition(speed - 5*is_birthday): return ticket


'''Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.'''


def sorta_sum(a, b):
    result = a + b
    if  10 <= result <= 19:
        return 20
    return result


'''Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, 
the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".'''

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day ==6:
            return "10:00"
        else:
            return "7:00"


'''The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.'''


def love6(a, b):
    if a == 6 or b == 6 or abs(a - b) == 6 or abs(b - a) == 6 or a + b == 6:
        return True
    else :
        return False


'''Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, 
in which case return True if the number is less or equal to 1, or greater or equal to 10'''


def in1to10(n, outside_mode):
    if outside_mode:
        return (n <= 1) or (n>=10)
    elif not outside_mode:
        return (n in range(1,11))


'''Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
 Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod'''


def near_ten(num):
    a = num % 10      
    return 2 >= a or 8 <= a 


'''We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.'''


def make_bricks(small, big, goal):
    return (goal%5)<=small and (goal-(big*5))<=small



'''Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, 
it does not count towards the sum.'''


def lone_sum(a, b, c):
    sum = a+b+c
    if a == b and a == c and b ==c :
        return 0
    if a == b:
        sum = c
        return sum
    if a == c:
        sum = b
        return sum
    if b ==c:
        sum = a
        return sum
    else:
        return sum


'''Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count 
towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.'''


def lucky_sum(a, b, c):
    sum = a+b+c
    if a == 13:
        sum = 0
    elif b == 13:
        sum = a
    elif c == 13:
        sum = a+b
    return sum


'''Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- 
then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
 Define the helper below and at the same indent level as the main no_teen_sum().'''


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n!= 16:
        return 0
    return n


'''For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
 Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
 Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition,
  write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().'''


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
  
def round10(num):
    if num % 10 < 5:
            return num - (num % 10)
            
    return num + (10 - num % 10)


'''We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.'''


def make_chocolate(small, big, goal):
    if(small+big*5<goal):

        return -1

    elif small<goal%5:

        return -1

    else:

        if(goal<10):
            return goal%5
        return goal-(big*5)


'''Given a string, return a string where for every char in the original, there are two chars.'''

def double_char(str):
    new_str = ""
    for char in str:
        new_str += char*2
    return new_str

'''Return the number of times that the string "hi" appears anywhere in the given string.'''


def count_hi(str):
    return str.count('hi') #Would be much better if you  tried to use another method


'''Return True if the string "cat" and "dog" appear the same number of times in the given string.'''


def cat_dog(str):
    return str.count('cat') == str.count('dog')


'''Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.'''


def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0 :
            count += 1
    return count
    




















  






