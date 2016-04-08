import json
my_list = ['corn', 
	   'potatoes',
	   'short ribs',
	  {'ingredients': [
			   'butter', 
			   'milk', 
			   'salt'], 
	  'dessert': [
			   'pie', 
	   	           'cake',
 			   'crumble']
          }
	  ]

with open("JSON_test.json", "w") as t:
   json.dump(my_list, t)



