import yaml
import json
from pprint import pprint as pp

with open("JSON_test.json") as j:
   jsonlist = json.load(j)


print "Here is the pretty print from JSON: "
pp(jsonlist)


with open("yaml_test.yml") as y:
   yamllist = yaml.load(y)


print "Here is the pretty print from yaml: "
pp(yamllist)

