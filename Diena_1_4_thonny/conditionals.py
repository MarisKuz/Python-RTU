# # # # # # # a = 215
# # # # # # a = int(input("Input a"))
# # # # # a = 9000
# # # # # a = 3
# # # # #
# if True:
# if False:
#     print("This always runs because if statement is True")
#     print("Still working in if block")
# # # # #
# # # # # # # after we go back to our normal indentation the if block is ended
# # # # # #
a = 15
# if a > 10: # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Do this when a is larger than 10")
#     print("Still only runs when a > 10", a)
# #     # we can keep doing things when a > 10 here
# # # # # #
# # # # # # # # here we have exited if
# print("This will always print no matter what")
# # # # # # # # # #
# # # # # # # # #
# # # # # # # # a = -333
# # # # # # # # a = 200
# # # a = 44
# # a = 10
print("Before if else")
# # a = -55
a = 100
# if a > 10:  # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Again Do this when a is larger than 10")
#     print("Indeed a is", a)
# else:  # when a is <= 10
#     print("Only when a is less or equal to 10")
#     print("Indeed a is only", a)
#     # we could do more stuff here when a is not larger than 10
# print("Back to normal flow")
# # # # # #
# # # # # # # # a = 10
# # # # a = 200
# # # # # # a = -95
# # # a = 10
# # a = -355
# # a = 10 
# # # # # if we need more than 2 distinct paths
# a = 10
# if a > 10:  # in Python when you see : next line will be indented
# # #     # runs only when statement after if is True
#     print("Again Do this when a is larger than 10", a)
# elif a < 10:
#     print("ahh a is less than 10", a)
# else:  # so a must be 10 no other choices you do not need to check, after all other choices are exhaustedprint("Only when a is equal to 10 since we checked other cases", a)
    # we could do more stuff here when a is not larger than 10
# # # # # # # # #
# # # print("Back to normal program flow which always runs no matter what a is")
# # # # # # # #
# # # # # # # #
# # # # # # # # #
# # # # # # without else both of these could run
3
# a = 7
# if a > 5:

#     print("a is larger than 5")
# if a > 10:
#     print("a is larger than 10")
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # # if else elif
# a = 200
# a = int(input("give me an a! "))
# if a > 10:
#     print("a is larger than 10")
#     print("This will only happen when a > 10")
#     if a >= 200: # so we can nest ifs inside another if
#         print("a is truly big over  or equal 200")
#         print("inded it is over 200", a)
#     else:
#         print("a is more than 10 but no more than 199",a)
# elif a < 10:
#     print("a is less than 10", a)
# else: # if a == 10
#     print("a is equal to 10", a)
# # # # # #
# print("This will always happen no matter the a value")
# # # # # #
# # # # # # b = -8500
# # # # # # b = 6
# # # # # # b = 555
# # # # # # b = 9000
# # # # # # if b < 0:
# # # # # #     print("Less than 0", b)
# # # # # # elif b < 10:
# # # # # #     print("Less than 10 but more or equal to 0", b)
# # # # # # elif b < 9000:
# # # # # #     pass # empty operation
# # # # # # #     print("At least 10 but less than 9000", b)
# # # # # # else:
# # # # # #     print("9000 or more!", b)
# # # # # # #
# # # # # # if b < 0:
# # # # # #     print("Less than 0", b)
# # # # # #
# # # # # # if b < 10:
# # # # # #     print("Less than 10", b)
# # # # # #
# # # # # # if b < 9000:
# # # # # #     print("less than 9000", b)
# # # # # # else:
# # # # # #     print("9000 or more!", b)
# # # # # # # #
# # # # # # c = None
# # # # # # c = 5
# # # # # # if c == None:
# # # # # #     print("There is Nothing")
# # # # # # else:
# # # # # #     print("There is something")
# # # # # # # #
# # # # # #
a = 4
if 2 < 3 < 8 < a:
    print(f"2 < 3 < 8 < {a} is it a True statement? ", 2 < 3 < 8 < a)
else:
    print(f"2 < 3 < 8 < {a} is it a True statement?", 2 < 3 < 8 < a)
# 
# # a = "Valdis"
# a = 20
# # if 2 < a and a < 150:
# if 2 < a < 150: #same as above
#     print("a is larger than 2 and less than 150", a)
# else:  # a <= 2 OR a >= 150
#     print("a is equal or less than 2 OR larger or equal to 150", a)
# 
# # or we would use to see outside
# if a < 2 or a > 150:
#     print("hmm  a less than 2 or a is more than 150")
# else: # 2 <= a <= 150
#     print("Inside 2 to 150", a)