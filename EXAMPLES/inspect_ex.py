import inspect
import typing as T

class Spam:  # <1>
    pass

# s = Spam()

def ham(p0: int, /, p1: float, p2: str='a', *p3, p4:int, p5: str='b', **p6) -> str:  # <2>
    print(p0, p1, p2, p3, p4, p5, p6)


for thing in (inspect, Spam, ham):
    print("{}: Module? {}. Function? {}. Class? {} Callable? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
        callable(thing),
    ))
#  callable(thing)
print()

print("Function spec for Ham:", inspect.getfullargspec(ham))  # <6>
print()

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>


def spam(a: int, b: float, c: str):
    print(a, b, c)

spam(1, 2, 3)

spam("a", "b", 52.9)

