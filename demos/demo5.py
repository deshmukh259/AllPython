# Function definition is here
def changeme( mylist , f):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   f =56
   print ("Values inside the function: ", mylist)
   return

if __name__ == "__main__":
# Now you can call changeme function
    mylist = [10,20,30];
    f = 45
    changeme( mylist, f );
    print ("Values outside the function: ", mylist, f)
