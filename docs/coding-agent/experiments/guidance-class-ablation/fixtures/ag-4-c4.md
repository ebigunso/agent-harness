---
id: ag-4-c4
section: ag-4
type: clean
---
Task framing: Make character index units explicit.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,10 @@
+pub struct CharacterAt<'a> { pub text: &'a str, pub scalar_index: usize }
+pub struct CharacterResult { pub value: Option<char> }
+pub fn select(input: CharacterAt<'_>) -> CharacterResult {
+ CharacterResult { value: input.text.chars().nth(input.scalar_index) }
+}
+#[test]
+fn unicode() {
+ assert_eq!(select(CharacterAt { text:"éa", scalar_index:1 }).value,Some('a'));
+ assert_eq!(select(CharacterAt { text:"éa", scalar_index:2 }).value,None);
+}
```
Commit message: "make character index units explicit"

Reviewer notes: Input is Unicode scalar index, not byte offset. Missing position explicitly returns None. Structs carry only needed fields, borrow lifetime is limited to call, and output char is owned.
