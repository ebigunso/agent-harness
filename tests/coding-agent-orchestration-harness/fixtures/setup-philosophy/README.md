# Setup philosophy fixtures

`no-philosophy` exercises scenario 1: setup lists both philosophies as none yet.
`with-product-philosophy` exercises scenario 2: setup records the product philosophy pointer, then a later small run is graded against it.
Copy each fixture into a temporary git repository; in `with-product-philosophy`, append the line in `ratification-line.txt` to `docs/product/what-tally-is-for.md` (after a blank line) and delete `ratification-line.txt`; then commit and run setup. The ratification line is kept apart here so that the fixture's document is not itself a ratified philosophy inside the repository that holds the fixtures.
`with-foreign-philosophy` exercises a document that may belong to something else: its only ratified product philosophy sits inside the vendored project `vendor/wordlist/`, so setup records no pointer, writes the awaiting line and brings the file to the person for confirmation. Prepare it as the second fixture, appending its `ratification-line.txt` to `vendor/wordlist/docs/what-wordlist-is-for.md`.
The persons and words in the ratification records are fictional.
`RUN-2026-10-05.md` records one run of both scenarios on these fixtures.
