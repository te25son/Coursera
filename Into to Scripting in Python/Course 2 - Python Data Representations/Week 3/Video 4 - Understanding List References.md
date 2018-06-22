## UNDERSTANDING LIST REFERENCES

To understand references and objects and how they work, let's look at a few different situations...

![capture1](https://user-images.githubusercontent.com/39095798/41774068-7cef2252-761e-11e8-969f-30691f0c255b.PNG)

![capture2](https://user-images.githubusercontent.com/39095798/41774076-880297f0-761e-11e8-98c1-8bf6db6ec151.PNG)
    
In our first example, we see two lists that appear to be the same. However, we can also see that while they look to be the same, my_list1 and my_list2 both refer to their own unique object. By calling the append method on my_list1 this becomes even more clear as we can see that only the list object for my_list1 was actually appeneded. Nothing has changed for my_list2. My_list1 and my_list2 are not copies or references to the same object, they are <b> lookalikes </b>.

In our next example, we'll look at aliases again.

![capture1](https://user-images.githubusercontent.com/39095798/41774251-255daa80-761f-11e8-8d6a-ad607d934d0d.PNG)
![capture2](https://user-images.githubusercontent.com/39095798/41774259-2ec7006c-761f-11e8-931c-86a065ac2125.PNG)

Here we can see that by stating mylist1 = mylist2, we are telling Python to make my_list2 refer to the same object that my_list1 refers to. Because both objects refer to the same object, whatever happens to one reference will also affect the other. This is clearly marked when we use the insert method to insert the number 5 into index 1 of my_list2. 

Remember, aliases are just different names for the same object like Batman and Bruce Wayne are aliases for the same person. If Batman breaks his back, Bruce Wayne will also have a broken back. 

Now what about making a copy of a list?

There are multiple ways to copy a list, but for this example we'll use the list function. 

![capture1](https://user-images.githubusercontent.com/39095798/41774627-e11266fc-7620-11e8-85d7-b6dd12792554.PNG)

![capture2](https://user-images.githubusercontent.com/39095798/41774638-ec1ca120-7620-11e8-8d54-640cf031602b.PNG)

Here we can see, like our first example, we've created an exact replica of our list. We also see that both my_list1 and my_list2 refer to unique lists, so we can assume that changes made to one list will not affect the other. Let's double-check this...

![capture3](https://user-images.githubusercontent.com/39095798/41774860-bdee7ce6-7621-11e8-9519-41a23acb719a.PNG)

![capture4](https://user-images.githubusercontent.com/39095798/41774873-c54bbcba-7621-11e8-9a10-765a208f2109.PNG)

And we're right! By calling the pop method on my_list2, my_list1 was left unaffected. The reason for this is that the object list does not contain objects themselves, rather it contains further references to those objects. So a list is an object that contains reference indexes to other objects. This is the reason, when we want to change an object in a list, we call its index number.

