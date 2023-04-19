import flywithwings
import nowings
import quack
import noquack
import squeak

obj1 = flywithwings.flywithwings
obj2 = nowings.nowings
obj3 = quack.quack
obj4 = noquack.noquack
obj5 = squeak.squeak

val = " "
print("select a duck")
print("for Mallard Duck  write 1")
print("for Rubber Duck write 2")
print("for Redhead Duck write 3")   
print("for Decoy Duck write 4")
val = input("number -")
if val == "1":
    print("This is a Mallard Duck.")
    obj1.flywithwings()
    obj3.quack()
elif val == "2":
    print("This is a Rubber Duck.")
    obj2.nowings()
    obj5.squeak()
elif val == "3":
    print("This is a Readhead Duck.")
    obj1.flywithwings()
    obj4.noquack()
elif val == "4":
    print("This is a Decoy Duck.")
    obj1.flywithwings()
    obj3.quack()