import MyPackages
from MyPackages import fullname


#camry = Car.Car("camry", "silver", "toyota", 120) 
#camry.start()


#fullname.fullname()
myname = fullname.fullname("mahadeva,Mahesh")

print ("First Name : " + myname.getFirstName()) 
print ("First Name : " + myname.firstName) 

print (myname.counter)
myname.increment()
print (myname.counter)
myname.increment()
print (myname.counter)


baagu = fullname.fullname("Mahesh, Bhagya")
print(baagu.counter)
baagu.increment()
print(baagu.counter)
baagu.increment()
