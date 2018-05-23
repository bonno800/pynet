import yaml
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

with open("yaml_test.yml", "w") as t:
   t.write(yaml.dump(my_list, default_flow_style=False))



