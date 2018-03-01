The [ripgrep](https://github.com/BurntSushi/ripgrep), implmented in Rust is
meant to be used exactly like you'd use `grep` in a terminal&mdash;but is [much
faster](https://github.com/BurntSushi/ripgrep#quick-examples-comparing-tools)
and an
[improvement](https://github.com/BurntSushi/ripgrep#why-should-i-use-ripgrep)
over grep in many ways.

### But what *is* grep?

Grep is a small Unix program for finding matching patterns! You can give it
anything as input: files, text from standard input (your keyboard), and a
pattern to match against!

Here is a quick example of how you'd use `grep` (you can use `ripgrep` in a
similar way)

```bash
# print all lines in my_file.txt containing the word 'flags' (case sensitive)
cat my_file.txt | grep 'flags'
```

