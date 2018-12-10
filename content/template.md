---
background: "img/bg11.jpg"

title: "Here Here Write the best title for your page."
description: "Your page can also have a small description after the big bold title, that's why we added this text here. Add here all the information that can make you or your product create the first impression."

---


Here comes the body of the page...

```python
def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

numbers = (1,6,3,32,85,23,9,123,23,336)

print qsort1(numbers)
```
