import yaml
import json
from pprint import pprint as pp

with open("JSON_test.json") as j:
   jsonlist = json.load(j)


print "Here is the pretty print from JSON: "
pp(jsonlist)
