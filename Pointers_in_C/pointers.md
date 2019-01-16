# Pointers in C

Pointers are a pain in the ass to work with. Trust me, I learned about them 2 days ago.

It has almost everything to do with memory allocation and referencing and dereferencing variables. Pointers are glorious tools to use if you want to save some memory, aka make your program run faster, by dynamically allocating the memory your program uses. 

To understand how dynamic memory works, we need to understand heaps and stacks. 

In a nutshell, the stack is where all your declared variables go. So, when you declare something like `int a;`, because a is a declared variable with a name, it spends its life on the stack. The same way a pointer like `int* ptr1;` also is born, lives, and dies on the stack. 

Here's what our memory looks like after we pointer our pointer ;) at a with this snippit of code `int* ptr1 = &a`:

![Image of the memory so far](https://github.com/te25son/Learning-Tools/blob/master/Pointers_in_C/images/stack0.PNG)

So now our code looks a little something like this:

```c
int a;
int* ptr1 = &a;
```

As you know, or will soon know, **POINTERS ARE JUST AN ADDRESS**. I say again, **POINTERS ARE JUST AN ADDRESS**. Sing it with me. 1, 2, 3 **POINTERS ARE JUST AND ADDRESS**.

Since we've established that pointers are just an address, let's look at the heap. 

You may be asking well, wait if declared variables always live on the stack, then how can there be an undeclared variable? What would that even look like? Well, the heap is a magic place where memory can be allocated and freed at the programmers discrition. In this way, the programmer is a little like God. And if we remember that pointers are just an address, we can start to imagine how an address can direct us to something that's not quite in view yet.

But before I go further, know that declared, non-pointer variables spend their short little lives on a single plane of existence, the stack. Pointers, on the other hand, are magical creatures that can move (or point) between the stack world and the heap world.

For example, the following two lines of code are NOT equal:

```c
int b = malloc(sizeof(int));
int* ptr2 = malloc(sizeof(int));
```


