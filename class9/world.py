
def main():
   print "hello world!"

class MyClass(object):
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def hello(self):
      print "my name is " + self.a + " and I live in " + self.b


class MyChildClass(MyClass):
    def hello(self):
      print "my name is " + self.a + " and I live in " + self.b + "in a town called Child Class"

if __name__ == "__main__":
    main()

