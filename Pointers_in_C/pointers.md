# Pointers in C

Pointers are a pain in the ass to work with. Trust me, I learned about them 2 days ago.

It has almost everything to do with memory allocation and referencing and dereferencing variables. Pointers are glorious tools to use if you want to save some memory, aka make your program run faster, by dynamically allocating the memory your program uses. 

To understand how dynamic memory works, we need to understand heaps and stacks. 

In a nutshell, the stack is where all your declared variables go. So, when you declare something like `int a;`, because m is a declared variable with a name, it spends its life on the stack. The same way a pointer like `int* ptr1;` also is born, lives, and dies on the stack. 

Here's what our memory looks like after we pointer our pointer ;) at a with this snippit of code `int* ptr1 = &a`:

![Image of the memory so far](https://github.com/te25son/Learning-Tools/blob/master/Pointers_in_C/images/stack0.PNG)
