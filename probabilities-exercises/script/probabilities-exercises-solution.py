#!/usr/bin/env python
# coding: utf-8

# <table><tr><td><a href="https://mybinder.org/v2/gh/markcrowe-com/statistics/master?filepath=probabilities-exercises/probabilities-exercises-solution.ipynb" target="_parent"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder"/></a></td><td>online editors</td><td><a href="https://colab.research.google.com/github/markcrowe-com/statistics/blob/master/probabilities-exercises/probabilities-exercises-solution.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td></tr></table>

# # Probabilities Exercises

filename = 'probabilities-exercises-solution.xlsx'


# local
filepath = filename


# remote
filepath = 'https://github.com/markcrowe-com/statistics/blob/master/probabilities-exercises/'+ filename + '?raw=true'


import pandas
excelWorkbook = pandas.ExcelFile(filepath)


# ## Exercise 1
# A purchasing department finds that 75% of its special orders are received on time. Of those received on time, 80% fully meet the specifications. Of those who arrive late, 60% comply. A random package is chosen:  
# 
# a) What is the probability that it meets the specifications?  
# b) If an order was chosen that does not meet specifications, what is the probability that it was received on time?

# ### Answer: Decision Tree and Algebra
# 
# [![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIjAuNzVcInwgVCgoXCJQKFQpXCIpKVxuXHRzdGFydC0tPiB8XCIwLjI1XCJ8IHQoKFwiUChUzIUpXCIpKVxuXHRULS0-IHxcIlAoU3xUKT0wLjhcInwgU1QoKFwiUChTJmNhcDtUKVwiKSlcblx0VC0tPiB8XCJQKFPMhXxUKT0wLjJcInwgc1QoKFwiUChTzIUmY2FwO1QpXCIpKVxuXHR0LS0-IHxcIlAoU3xUzIUpPTAuNlwifCBTdCgoXCJQKFMmY2FwO1TMhSlcIikpXG5cdHQtLT4gfFwiUChTzIV8VMyFKT0wLjRcInwgc3QoKFwiUChTzIUmY2FwO1TMhSlcIikpXG5cdFNULS0-U1RBbnN3ZXIoMC43NSAqIDAuOCA9IDAuNilcblx0U3QtLT5TdEFuc3dlcigwLjc1ICogMC4yID0gMC4xNSlcblx0c1QtLT5zVEFuc3dlcigwLjI1ICogMC42ID0gMC4xNSlcblx0c3QtLT5zdEFuc3dlcigwLjI1ICogMC40ID0gMC4xKVxuXHRTVEFuc3dlci0tPlMoKFwiUChTKVwiKSlcblx0U3RBbnN3ZXItLT5TXG5cdFMtLT5TQW5zd2VyKFwiMC42ICsgMC4xNSA9IDAuNzVcIikiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/#eyJjb2RlIjoiZ3JhcGggVEI7XG5cdHN0YXJ0KCApXG5cdHN0YXJ0LS0-IHxcIjAuNzVcInwgVCgoXCJQKFQpXCIpKVxuXHRzdGFydC0tPiB8XCIwLjI1XCJ8IHQoKFwiUChUzIUpXCIpKVxuXHRULS0-IHxcIlAoU3xUKT0wLjhcInwgU1QoKFwiUChTJmNhcDtUKVwiKSlcblx0VC0tPiB8XCJQKFPMhXxUKT0wLjJcInwgc1QoKFwiUChTzIUmY2FwO1QpXCIpKVxuXHR0LS0-IHxcIlAoU3xUzIUpPTAuNlwifCBTdCgoXCJQKFMmY2FwO1TMhSlcIikpXG5cdHQtLT4gfFwiUChTzIV8VMyFKT0wLjRcInwgc3QoKFwiUChTzIUmY2FwO1TMhSlcIikpXG5cdFNULS0-U1RBbnN3ZXIoMC43NSAqIDAuOCA9IDAuNilcblx0U3QtLT5TdEFuc3dlcigwLjc1ICogMC4yID0gMC4xNSlcblx0c1QtLT5zVEFuc3dlcigwLjI1ICogMC42ID0gMC4xNSlcblx0c3QtLT5zdEFuc3dlcigwLjI1ICogMC40ID0gMC4xKVxuXHRTVEFuc3dlci0tPlMoKFwiUChTKVwiKSlcblx0U3RBbnN3ZXItLT5TXG5cdFMtLT5TQW5zd2VyKFwiMC42ICsgMC4xNSA9IDAuNzVcIikiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)
# 
# $ P(T|\overline{S}) = \frac{P(\overline{S} \cap T)}{P(\overline{S})} $  
# $ P(\overline{S}) = 1 - P(S) $  
# 
# $ P(S) = 0.75 \therefore P(\overline{S}) = 0.25 $  
# $ P(T|\overline{S}) = \frac{0.15}{0.25} $  
# $ P(T|\overline{S}) = 0.6 $
# 
# Answer:  
# a) $ P(S) = 0.75 $  
# b) $ P(T|\overline{S}) = 0.6 $

# ### Answer: Excel Contingency Table

excelWorkbook.parse('Question1')


# Answer:  
# a) $ P(B) = 0.75 $  
# b) $ P(A|\overline{B}) = 0.6 $

# ### Answer: Contingency Table and Algebra
# 
# | | $$ B \text{ (specification)} $$ | $$ \overline{B} \text{ (failed specification)} $$  | |
# |-|-|-|-|
# | $$ A \text{ (on time)} $$ | $$ A \cap B $$  $$ 0.75 * 0.8 = 0.60 $$ | $$ A \cap \overline{B} $$ $$ 0.75 * 0.2 = 0.15 $$ | $$ 0.75 $$ |
# | $$ \overline{A} \text{ (late)} $$ | $$ \overline{A} \cap B $$ $$ 0.25 * 0.6 = 0.15 $$ | $$ \overline{A} \cap \overline{B} $$  $$ 0.25 * 0.4 = 0.10 $$ | $$ 0.25 $$ |
# | | $$ 0.75 $$ | $$ 0.25 $$ | $$ 1.00 $$|
# 
# Answer a):  
# $ P(B) = P(A \cap B) + P(\overline{A} \cap B)$  
# $ P(B) = 0.6 + 0.15 $  
# $ P(B) = 0.75  $  
# 
# Answer b):  
# $ P(A \cap \overline{B}) = 0.15 $  
# $ P(B) = 0.75$  
# $ \therefore P(\overline{B}) = 1 - P(B) = 1 - 0.75 = 0.25 $
# 
# $ P(A|\overline{B}) = \frac{P(A \cap \overline{B})}{P(\overline{B})} $  
# $ P(A|\overline{B}) = \frac{0.15}{0.25} $  
# $ P(A|\overline{B}) = 0.6 $

# ### Answer: Programming

orderOnTime = .75 # 75% of its special orders are received on time
orderLate = 1 - orderOnTime # ie 25%
orderOnTimeSpecificationMet = .8 # those received on time, 80% fully meet the specifications.
orderLateSpecificationMet = .6 # those who arrive late, 60% comply.

# Solve with variables
specificationsMet = orderOnTime * orderOnTimeSpecificationMet + orderLate * orderLateSpecificationMet

# Solve with float numbers
# specificationsMet = .75 * .8 + .25 * .6

# Solve with fractions
# specificationsMet = 3/4 * 8/10 + 1/4 * 6/10

print("a) Answer: {}".format(round(specificationsMet, 2)))


# Solved with variables
specificationfailed = 1 - specificationsMet
onTimeSpecificationFail = orderOnTime * (1 - orderOnTimeSpecificationMet)
print("Unit spec-fail rate: {}".format(round(specificationfailed, 2)))
print("Unit spec-fail & on-time rate: {}".format(round(onTimeSpecificationFail, 2)))
print("P(on-time|Unit spec-fail): {}".format(round(onTimeSpecificationFail/specificationfailed, 2)))


# ## Exercise 2.
# Every night James rolls a dice to decide how he is going to wake up the next day to go to college. If the number turns out to be even, he will use the alarm of his cell phone and, if not, he will use the alarm clock. 5% of the times that his cell phone alarm sounds, he falls asleep, while only 1% of the times that he uses the alarm clock, he falls asleep and then fails to get to school on time.
# 
# a) What is the probability that, on any given day, James falls asleep?
# 

numberOfDiceSides = 6
numberOfEvenSides = 3 # 3 sides are even number (2, 4, 6)
numberOfOddSides = numberOfDiceSides - numberOfEvenSides

cellPhoneAlarmFailureRate = 0.05 #5% of the times that his cell phone alarm sounds, he falls asleep
alarmClockFailureRate = 0.01 # 1% of the times that he uses the alarm clock, he falls asleep

failureRate = ((numberOfEvenSides / numberOfDiceSides) * cellPhoneAlarmFailureRate) + ((numberOfOddSides / numberOfDiceSides) * alarmClockFailureRate)

print("Answer: {}".format(round(failureRate, 2)))


# 
# b) If it is known that on a certain day James attended college on time, what is the probability that he chose to wake up with the alarm on his cell phone? Answer: 0.83  

# ## Exercise 3.
# If we throw 3 coins, find the probability of getting:
# 
# a) Two heads.  
# b) Two tails.

# $ P(H) = 1 / 2 $  
# $ P(T) = 1 / 2 $    
# 
# $ P(2 Heads) = P(T \cap H \cap H)+ P(H \cap T \cap H)+ P(H \cap H \cap T) $  
# $ P(T \cap H \cap H) = P(H \cap T \cap H) = P(H \cap H \cap T) $  
# $ P(H \cap H \cap T) = (1/2) * (1/2) * (1/2) $  
# 
# $ P(2 Heads) = 3 * P(THH) $  
# $ P(2 Heads) = 3 * (1 / 2 * 1 / 2 * 1 / 2) $  

3 * (1 / 2 * 1 / 2 * 1 / 2) 


numberOfCoinSides = 2
numberOfCoins = 3
head = 1
tail = 1

answer = numberOfCoins * head / numberOfCoinSides * head / numberOfCoinSides * tail / numberOfCoinSides

print("Answer: {}".format(answer))


# ## Exercise 4.
# We roll a dice, and we want to know the probability of:  
# 
# a) Getting an even number?  

# A dice has 6 sides.  3 sides are even number (2, 4, 6), 3 sides are odd number (1, 3, 5)
numberOfDiceSides = 6
numberOfEvenSides = 3

answer = round(numberOfEvenSides / numberOfDiceSides, 2)
print("Answer: {}".format(answer))


# b) Getting a multiple of 6?

# Only one side of the dice is a multiple of 6. i.e. 6

answer = round(1 / 6, 2)
print("Answer: {}".format(answer))


# c) A number greater than 4?

# Only two sides of the dice is greater than 4. i.e. 5 and 6

answer = round(2 / 6, 2)
print("Answer: {}".format(answer))


# ## Exercise 5.
# An urn contains 8 red balls, 5 yellow balls and 7 green balls. If we randomly picked one, what is the probability of:

# Variables
redBalls = 8;
yellowBalls = 5;
greenBalls = 7;
ballCount = redBalls + yellowBalls + greenBalls;


# a) Getting a red ball?  

answer = round(redBalls / ballCount, 2)
print("Answer: {}".format(answer))


# b) Getting a green ball?

answer = round(greenBalls / ballCount, 2)
print("Answer: {}".format(answer))


# c) Getting a yellow ball?

answer = round(yellowBalls / ballCount, 2)
print("Answer: {}".format(answer))


# d) Not getting a red ball?

answer = round((ballCount - redBalls) / ballCount, 2)
print("Answer: {}".format(answer))


# e) Not getting a yellow ball?

answer = round((ballCount - yellowBalls) / ballCount, 100)
print("Answer: {}".format(answer))


# f) If we know that the ball is not red, what is the probability of getting a green one?

answer = round(greenBalls / (ballCount - redBalls), 2)
print("Answer: {}".format(answer))


# ## Exercise 6.
# Given $P(A) = 0.50$, $P(\overline{B}) = 0.30$ and $P(A \cup \overline{B}) = 0.70$, Calculate $P(A \cap B)$  
# 
# ### Contingency Table Answer
# 
# | | $$ B $$ | $$ \overline{B} $$ ||
# |-|-|-|-|
# | $$ A $$ | $$ A \cap B $$ | $$ A \cap \overline{B} $$ | $$ 0.5 $$ |
# | $$ \overline{A}$$ | $$ \overline{A} \cap B $$ | $$ \overline{A} \cap \overline{B} $$ | $$ ? $$ |
# | | $$ ? $$ | $$ 0.3 $$ | $$ 1.0 $$ |
# 
# $ P(A \cap B) + P(\overline{B}) = P(A \cup \overline{B})$  
# $ P(A \cap B) = P(A \cup \overline{B}) - P(\overline{B}) $  
# $ P(A \cap B) = 0.7 - 0.3 $  
# $ P(A \cap B) = 0.4 $  

round(0.7 - 0.3, 2)


excelWorkbook.parse('Question6')


# ### Formula Algebra Answer
# 
# $ P(A \cup \overline{B}) = P(A) + P(\overline{B})-P(A \cap \overline{B}) $  
# $ P(A) = P(A \cap B) + P(A \cap \overline{B}) $  
# $ P(A \cup \overline{B}) = P(A \cap B) + P(A \cap \overline{B}) + P(\overline{B})-P(A \cap \overline{B}) $  
# $ P(A \cup \overline{B}) = P(A \cap B) + P(\overline{B}) $  
# $ P(A \cup \overline{B})-P(\overline{B}) = P(A \cap B) $  
# $ .7 - .3 = P(A \cap B) $  
# $ P(A \cap B) = 0.4 $  

notB = .3
AuNotB = .7

AnB = AuNotB - notB
answer = round(AnB, 2)
print("Answer: {}".format(answer))


# ## Exercise 7.
# In a classroom of 40 students, 10 of them are boys. Between the boys, 3 can speak another language while 50% of the girls can speak a foreign language. If we randomly pick a student:  

excelWorkbook.parse('Question7')


# let probability of a girl be $ P(\overline{A}) $  
# let probability of a foreign language be $ P(B) $  
# $ P(\overline{A}) = 0.75 $  
# $ P(B) = 0.45 $  
# $ P(A|\overline{B}) = 0.318182 $  

# ### Contingency Table
# | | $$ B \text{ (boy)} $$ | $$ \overline{B} \text{ (girl)} $$ | |
# |-|-|-|-|
# | $$ M $$ (multilingual) | $$ 3 $$ | $$ 0.5 * 30 = (15) $$ | $$ 3 + 15 = (18) $$ |
# | $$ \overline{M} $$ (not multilingual) | $$ 10 - 3 = (7) $$ | $$ 0.5 * 30 = (15) $$ | $$ 7 + 15 = (22) $$ |
# | | $$ 10 $$| $$ 40 - 10 = (30) $$ | $$ 40 $$ |

# a) What is the probability of this to be a girl?

studentCount = 40
boyCount = 10
boyMultilingualCount = 3
girlMultilingualRate = .5

girlCount = studentCount - boyCount
answer = round(girlCount / studentCount, 2)
print("Answer: {}".format(answer))


# b) What is the probability this student speaks a foreign language?

girlMultilingualCount = girlCount * girlMultilingualRate
studentMultilingualCount = boyMultilingualCount + girlMultilingualCount
answer = round((studentMultilingualCount) / studentCount, 2)
print("Answer: {}".format(answer))


# c) If the student does not speak a foreign language, what is the probability of this person to be a boy?

answer = round((boyCount - boyMultilingualCount)/(studentCount - studentMultilingualCount), 4)
print("Answer: {}".format(answer))


# Close Connection to the open excelWorkbook
excelWorkbook.close()


# Copyright (c) 2021 Mark Crowe (<https://github.com/markcrowe-com>). All rights reserved.  
