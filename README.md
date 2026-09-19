# hello-world

Simple Hello World examples with **intentional** vulnerabilities for code-scanner testing.

## Python (CWE-79 XSS)

```bash
python hello.py
```

`hello.py` reflects the `name` query parameter into HTML with no escaping.

## C (CWE-120 / CWE-121 buffer overflow)

```bash
gcc -o hello hello.c
./hello
```

`hello.c` copies attacker-controlled input into a 16-byte stack buffer with `strcpy`.

## Java (CWE-78 command injection, CWE-89 SQL injection)

```bash
javac Hello.java
java Hello World
```

`Hello.java` passes unsanitized arguments to `Runtime.exec()` and concatenates them into a SQL string.

These vulnerabilities are present on purpose so you can verify that a scanner detects them. Do not reuse these patterns!
