def my_decorator(func):
    def wrapper():
        print("Checking Raw ingredients…")
        func()
        print("Verify Final Product…")
    return wrapper

def bake_cake():
    print("Baking Cake")


def bake_bread():
    print("Baking Bread")

bake_item1 = my_decorator(bake_cake)
bake_item2 = my_decorator(bake_bread)

bake_item1()
bake_item2()
