# The change to `tally.py`

One line changed, line 11, between the fixture's commits 4f22ff7 and ba3675f. It is shown as the line before and after, not as a patch: a patch's blank context line ends in a space, which this repository's whitespace check rejects.

Before:

```python
    print("Cannot read the file.", file=sys.stderr)
```

After:

```python
    print(f"tally could not read {sys.argv[1]}.", file=sys.stderr)
```

Nothing else in the file changed.
