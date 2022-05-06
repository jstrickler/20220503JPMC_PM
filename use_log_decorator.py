from simple_decorators import log_calls

@log_calls
def spam():
    print("hello from spam()")
# spam = honk(spam)

@log_calls
def ham():
    print("hello from ham()")

spam()
spam()
ham()
ham()
spam()
spam()
ham()

print(spam.__name__, ham.__name__)