from ubidots import ApiClient

api = ApiClient(token='SwWv78hxFMR42afpUyIKGKtwnNBtEV')
new_datasource = api.create_datasource({"name": "third", "tags": ["a", "b"], "description": "trying"}) 	#create new datasource
print "datasource created\n"
new_variable = new_datasource.create_variable({"name": "variable0", "unit": "kg"})					#create a new variable in the datasource
print "variable0 created\n"
new_variable1 = new_datasource.create_variable({"name": "variable1", "unit": "kg"})
print "variable1 created"
new_variable.save_values([												#saving multiple values
    {'timestamp': 1380558972614, 'value': 2},
    {'timestamp': 1380558972915, 'value': 4},
    {'timestamp': 1380558973516, 'value': 5},
    {'timestamp': 1380558973617, 'value': 3}
])
print "value saved to the variable0"
new_variable1.save_values([												#saving multiple values
    {'timestamp': 1380558972614, 'value': 0},
    {'timestamp': 1380558972915, 'value': 0},
    {'timestamp': 1380558973516, 'value': 0},
    {'timestamp': 1380558973617, 'value': 0}
])
print "value saved to the variable1"
#api.save_collection([{'variable': '58e875047625420f6770b4e5', 'value': 10}, {'variable': '58e875027625420f66c286c6', 'value':20}]) #updating multiple values
all_values = new_variable.get_values()											#get all values
print all_values
last_value = new_variable.get_values(1)
print last_value[0]['value']



