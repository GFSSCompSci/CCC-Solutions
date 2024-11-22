# CCC Solutions 

## All CCC questions were accessed through [DMOJ](https://dmoj.ca/)

### [Computer Science Club](https://dmoj.ca/organization/20-glenforest-ss) at Glenforest Secondary School.

Club resources can be found [here](https://drive.google.com/drive/folders0B58mJPYXfz39fjBwd1hJaTZodzJNWkM4VV9HNVVxaDhKYTJadUx4MDE5SmEzclZzXzQ5aHc).

### Competitive Programming Resources
****
1. [USACO GUIDE](https://usaco.guide/general/intro-cp)
2. [Competitive programming Handbook](https://cses.fi/book/book.pdf) All Credits goes to the original author of the book `Antti Laaksonen`.
3. [Algorithms](https://github.com/TheAlgorithms) Every Algorithm you'll ever need
****

## Contributing

We welcome contributions to this repository! To ensure a smooth process, please follow these guidelines (ensure you have [git](https://www.youtube.com/watch?v=hwP7WQkmECE&ab_channel=Fireship) installed)

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page to create a copy of the repository on your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/GFSSCompSci/CCC-Solutions.git
    ```

3. **Create a New Branch**: Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-branch-name
    ```

4. **Make Changes**: Make your changes to the codebase. Ensure your code follows the project's coding standards and includes appropriate comments and documentation.

5. **Commit Changes**: Commit your changes with a descriptive commit message:
    ```bash
    git add .
    git commit -m "Description of the changes made"
    ```

6. **Push Changes**: Push your changes to your forked repository:
    ```bash
    git push origin feature-branch-name
    ```

7. **Create a Pull Request**: Go to the original repository and create a [pull request](https://www.youtube.com/watch?v=8lGpZkjnkt4&ab_channel=Fireship) from your forked repository. Provide a clear and detailed description of your changes.

## Important Info

When solving competitive programming problems, it's often necessary to handle large inputs efficiently. In python the built-in `input()` function can be slow for large inputs, so it's recommended to use `sys.stdin.readline` for faster input.

Here's how you can use it

1. **Import the `sys` module**:
    ```python
    import sys
    ```

2. **Read a single line of input**:
    ```python
    line = sys.stdin.readline().strip()
    ```

    - `sys.stdin.readline()` reads a line from standard input.
    - `.strip()` removes any trailing newline characters.

3. **Read multiple lines of input**:
    ```python
    import sys

    input = sys.stdin.read
    data = input().split()
    ```

    - `sys.stdin.read()` reads all input at once.
    - `.split()` splits the input into a list of strings based on whitespace.

4. **Example**:
    ```python
    import sys

    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    print(n)
    print(arr)
    ```


