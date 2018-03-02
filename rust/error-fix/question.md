In this question, you will learn a little bit about the Rust programming
language by understanding and fixing a compiler error in a code snippet.

Run the following code snippet in the [Rust
playground](https://play.rust-lang.org/).

```rust
fn main() {
    let flags_captured = 7;
    println!("We captured {} flags!", flags_captured);
    flags_captured = 6;
    println!("We captured {} flags!", flags_captured);
}
```

You should get an error. Your task is to fix this error&mdash;it should only be
a one line change. You might find it useful to look up the meaning of "immutable
variables" and the [variable
bindings](https://rustbyexample.com/variable_bindings.html) chapter in Rust By
Example helpful.

Enter the correct line of code that makes the code run without any errors.
