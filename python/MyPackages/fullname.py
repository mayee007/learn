class fullname: 

  def __init__(self , val): 
    print("inside init, val  " + val)
    if val.find(","):
    	self.lastName, self.firstName = val.split(',') 	

    self.counter = 1

  def getFirstName(self): 
    return self.firstName

  def increment(self):
    self.counter = self.counter + 1
    return self.counter
