from ubidots import ApiClient
api=ApiClient("BBFF-ee87b3ea74bc757782cf96571d518cb6d44")
myvariable=api.get_variable("5ff960291d84722e5f8f02f2")
new_value=myvariable.save_value({'value':100})
