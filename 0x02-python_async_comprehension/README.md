#	Async Generators and Comprehensions
```py
#!/usr/bin/env python3
from typing import Generator


def generate_numbers(limit: int) -> Generator[int, None, None]:
    for num in range(limit):
        yield num

def main(limit: int) -> list:
    numbers = [num async for num in generate_numbers(limit)]
    return numbers
```
