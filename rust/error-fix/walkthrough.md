# Solution

When we run the code in the Rust Playground, we get the following error.

```
error[E0384]: cannot assign twice to immutable variable `flags_captured`
 --> src/main.rs:4:5
  |
2 |     let flags_captured = 7;
  |         -------------- first assignment to `flags_captured`
3 |     println!("We captured {} flags!", flags_captured);
4 |     flags_captured = 6;
  |     ^^^^^^^^^^^^^^^^^^ cannot assign twice to immutable variable
```

This error is telling us that since we assigned the value 7 to `flags_captured`
previously, we cannot update (or **mutate**) the variable with a new value
later.

On line 2 of the code, replace

```rust
let flags_captured = 7;
```
with

```rust
let mut flags_captured = 7;
```

This tells the Rust compiler "allow me to update the variable `flags_captured`"!
When you run this changed code in the Rust playground, it should compile with no
errors.
