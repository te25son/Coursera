OBJECTS & REFERENCES
--------------------

Think of a reference as a name tag. You put a name tag onto an object so you have something to reference that object as. You can also take the name tag off and put it back on again. Or, if you're feeling especially crazy, you can take your name tag off of one object and put it onto another object. Whoa!

Furthermore, you can put multiple name tags onto one object. For example:

![screenshot 1](https://user-images.githubusercontent.com/39095798/41703520-e0f8e594-7533-11e8-8280-b2be36d8c220.png)

In the above example my_list refers to the list object [1, 2, 3]. In other words, we've placed a name tag on our list to introduce it as "my_list". When we call my_list, we are really calling the list [1, 2, 3].

On the second line we declare my_other_list = my_list. By saying this we are telling Python we want my_other_list to refer to the object referred to by my_list. Here's another image to clear up any confusion:

![screenshot2](https://user-images.githubusercontent.com/39095798/41706284-b5893df2-753b-11e8-895e-3f227f80ec4c.PNG)

You can see here that both names refer to the same object. Therefore, we can logically conclude that whatever happens to one of the names will happen to the other. To check this, look at the next example:

![screen shot 2018-06-21 at 1 30 30 pm](https://user-images.githubusercontent.com/39095798/41718594-b03c6294-755d-11e8-97af-b3315555be09.png) 
![screen shot 2018-06-21 at 1 31 01 pm](https://user-images.githubusercontent.com/39095798/41718638-ccab6d44-755d-11e8-816f-f33a4ebe16ea.png)

Here we've used the append method to add a fourth item into our list. I called the method on my_list, but because my_list and my_other_list both refer to the same list, both lists now have four elements. 

Another way to look at this is to think of the object as a person with multiple names or aliases. For example, let's try to imaging a person who has two names, Bruce Wayne and Batman. Both of these names refer to the same person, and so whatever happens to Batman also happens to Bruce Wayne and vice versa. 

To really clarify this, let's try calling another method, but on my_other_list this time.

![screen shot 2018-06-21 at 2 21 53 pm](https://user-images.githubusercontent.com/39095798/41718853-86f828d6-755e-11e8-8cfb-418b65f94a01.png) 
![screen shot 2018-06-21 at 2 22 16 pm](https://user-images.githubusercontent.com/39095798/41718873-95e5643a-755e-11e8-943a-0bf2838289cd.png)

As we can see, calling a method on my_other_list also changes my_list. Surprise-surprise!

I mentioned earlier that name tags can also be taken off and put onto other objects. To continue the Batman / Bruce Wayne analogy, let's say Batman gets tired of beating up baddies, so decides to retire and pass the role of Batman on to a successor. The alias Batman is still there, but now it refers to a new person. What do you think will happen? Will Bruce Wayne also disappear because he is no longer Batman?

Let's experiment with this idea by assigning the name my_list to a new list.

![screenshot](https://user-images.githubusercontent.com/39095798/41725080-474a2002-756f-11e8-9aa6-98e0284d2d79.PNG) 

![screen shot](https://user-images.githubusercontent.com/39095798/41725104-53cbf7a6-756f-11e8-9aaa-2ba41528ca8a.PNG)

The answer is: no, Bruce Wayne does not disappear just because Batman now refers to another person. The person who was Bruce Wayne <i>and</i> Batman still exists, but now with just one alias instead of two. 


### TLDR:

An object can have as many names as you can give it. Whatever you do to one name will happen to every other name sharing the same object. 
