1. There are several attacks possible. For example, memcmp only compares the number of bytes you tell it to. If you compare no bytes against either of "admin" or "password" it will return true.
