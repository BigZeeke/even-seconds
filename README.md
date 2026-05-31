# Even Seconds

In Python, a **decorator** is syntactic sugar for a function that takes another function and returns a (usually modified) version of it.  Decorators let you write re-usable wrappers — logging, timing, caching, authentication checks — that you can attach to any function with a single line.

This challenge has you write a decorator that controls *when* the wrapped function actually runs.

## Requirements

1. Write a decorator called `only_even_seconds`.
2. Write some other function of your choice and decorate it with `@only_even_seconds`.
3. When the decorated function is called, it should only execute if the current time's **seconds** value is even.  If the seconds are odd, the call should do nothing (no error, no output — just silently skip).

So if your program is executed at `10:23:55`, the wrapped function would *not* run.  At `10:23:56` it would.

## Example

```python
from datetime import datetime

@only_even_seconds
def shout(message):
    print(message.upper())

# Call repeatedly in a loop and you'll see the message print
# only when the seconds-portion of the current time is even.
for _ in range(10):
    shout("hello!")
    time.sleep(1)
```

## Things to think about

- What does your decorator return when the seconds are odd?  `None`?  Something else?
- What happens if the wrapped function has a return value?  Does it still make sense to silently skip?
- Why does the decorator need to be a function that returns a function?  What's the inner function for?

## Challenge Yourself

- Add a parameter to the decorator: `@only_even_seconds(timezone="UTC")` or `@only_when(predicate=...)`.  How do parameterized decorators differ from plain ones?
- Write a `@only_odd_seconds` decorator without duplicating any of the logic — refactor toward a single shared implementation.

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
