This is how a variable is declared and initialized in Rust.

```rust
let x = 5;
```
In Rust, variables are immutable by default. This allows programmers to have the
confidence that once a variable is initialized, it will never change its value.
If we try to change it, our code won't compile! This turns out to be very useful
in preventing logical bugs. If some code that is called very rarely was able to
change the value of a variable whose value should *not* be changed, debugging
would be very hard, because the bug would occur only **some** of the times.

By making variables immutable, Rust makes it easier to reason about and debug
code. It gurantees that when a variable is given a certain value, it will
**always** have that value.

However, you can probably imagine situations in which we **do** want the ability
to change (or mutate) variable. Rust provides us with this option too&mdash;just
not by default. To make a variable, we use the `mut` keyword, as follows.

```rust
let mut x = 5;
```
You can read more about variables in Rust
[here](https://doc.rust-lang.org/book/second-edition/ch03-01-variables-and-mutability.html#differences-between-variables-and-constants)
