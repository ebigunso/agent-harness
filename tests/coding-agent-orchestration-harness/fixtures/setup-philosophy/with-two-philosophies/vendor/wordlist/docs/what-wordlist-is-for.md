# What wordlist is for

This document is this repository's product philosophy.

Wordlist is for someone building a glossary from a draft.
Each distinct word appears once in the list, in the order it first occurs.
Words that differ only in letter case are the same word.
The tool never changes the file it reads.
When it cannot read a file, it says so in one plain sentence and prints no list.
A successful run prints one word per line and nothing else, so it can be piped.
