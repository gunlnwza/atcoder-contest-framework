# atcoder-contest-framework
Fast local testing framework for AtCoder using `pytest` and docstring-based test cases.

### Structure
```
practice/
    submission.py

contest/
    A.py
    B.py
    C.py
    ...
```

Both `practice/` and `contest/` behave identically.
The only difference is file organization.

## How It Works
- Copy and paste sample test cases from the problem statement.
    - Separate input and output using `===`.
    - Separate each test case with a blank line.
- The local tester feeds input to `stdin` and captures `stdout` automatically.

## How to Use
1. Copy + paste the problem’s sample inputs and outputs.
2. Add additional custom test cases if needed.
3. Run:
    - `make test` (for `practice/`)
    - `make A`, `make B`, ... (for `contest/`)

### Example
A solution that adds two numbers:

```python
"""
1
1
===
2

2
2
===
4

40
2
===
42
"""

def main():
    a = int(input())
    b = int(input())
    print(a + b)
```

## Why
- No manual copy-paste testing
- Fast feedback loop
- Consistent contest workflow
