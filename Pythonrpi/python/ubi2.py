from ubidots import ApiClient
#from random import randint
import random
api=ApiClient("BBFF-ee87b3ea74bc757782cf96571d518cb6d44")
test_variable=api.get_variable("5ff958a61d847219d88099fa")
#test_value=random.randint(1,50)
while True:
 test_value1=random.uniform(2.555)
#test_variable.save_value({'value':test_value})
 test_variable.save_value({'value':test_value1})
