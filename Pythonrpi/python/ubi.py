from ubidots import ApiClient
import random


api = ApiClient("BBFF-Trvre2iLUMHGOWpICXoip4NzOO1Yd5")
test_variable = api.get_variable("BBFF-ee87b3ea74bc757782cf96571d518cb6d44")
test_value = random.randint(1,100)
test_variable.save_value({'value':test_value})
