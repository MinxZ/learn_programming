# Decorator example
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Annotation example
def greet(name: str) -> str:
    return f"Hello, {name}"

# A wrapper is the inner function defined within a decorator that actually performs the added functionality.
# A decorator is the outer function that takes a function as an argument, defines a wrapper function to modify it, and returns the wrapper.
