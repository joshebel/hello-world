# hello-world

Simple Hello World examples, plus an **intentional** C buffer overflow for code-scanner testing.

## Python

```bash
python hello.py
```

## C (intentionally vulnerable)

`hello.c` copies attacker-controlled input into a 16-byte stack buffer with `strcpy` (CWE-120 / CWE-121).

```bash
gcc -o hello hello.c
./hello
./hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

This vulnerability is present on purpose so you can verify that a scanner detects it. Do not reuse this pattern.
