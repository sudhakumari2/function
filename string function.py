# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter]) 
#     counter+=1


# def convert(sentence): 
#     return ([i for item in sentence for i in item.split()]) 
# sentence=["NavGurukul is an alternative to higher education reducing the barriers of current formal education system"]
# print(convert(sentence))

# def string_test(s):
#     UPPER_CASE=0
#     lower_case=0
#     for c in s:
#         if c.isupper():
#            UPPER_CASE+=1
#         elif c.islower():
#            lower_case+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", UPPER_CASE)
#     print ("No. of Lower case Characters : ", lower_case)

# string_test('The quick Brown Fox')

def test():
   s='The quick Brown Fox'
   i=0
   UPPER_CASE=0
   lower_case=0
   while i<len(s):
      if s[i].isupper():
         UPPER_CASE+=1
      elif s[i].islower():
         lower_case+=1         
      else:
           pass
      i+=1
   print(UPPER_CASE)
   print(lower_case)
test()
      

