# contest-framework
Fast local testing framework for competitive programming using `pytest` and docstring-based test cases.

### Structure
```
practice/
    submission.py
```

## How It Works
- Copy and paste sample test cases from the problem statement.
    - Separate input and output using `===`.
    - Separate each test case with a blank line.
- The local tester feeds input to `stdin` and captures `stdout` automatically.

## How to Use
1. Copy + paste the problem’s sample inputs and outputs.
2. Add additional custom test cases if needed.
3. Run:
    - `make` (for `practice/`)

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

if __name__ == "__main__":
    main()
```

## Why
- No manual copy-paste testing
- Fast feedback loop
- Consistent contest workflow
