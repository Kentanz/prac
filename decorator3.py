def my_decorator(func):
    def wrapper(*args,**kwargs):
        num=args[0]
        print("Checking Raw ingredients for "+str(num)+" cake")

        func(*args,**kwargs)
        print("Verify Final Product…")
    return wrapper

@my_decorator
def bake_cake(num):
    print("Baking "+str(num)+" Cake")

@my_decorator
def bake_bread():
    print("Baking Bread")

#bake_item1 = my_decorator(bake_cake)
#bake_item2 = my_decorator(bake_bread)

bake_cake(1)
