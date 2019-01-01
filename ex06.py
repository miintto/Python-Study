# -*- coding: utf-8 -*-
# 2018.12/28

### 문자열과 텍스트


x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'" % y)   ### 콤마 찍는거 주의!!
### ''와 ""를 구별하든지
### 또는 escaper \' 시용

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w+e)
