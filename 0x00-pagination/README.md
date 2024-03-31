## 00 - Pagination

### Resources

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination "REST API Design: Pagination")
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS "HATEOAS")

### Tasks

<details>
<summary>0. Simple helper function</summary>

Write a function named `index_range` that takes two integer parameters `page` and `page_size`.

This function should return a tuple of two elements. The first element is the start index and the second element is the end index. These indexes represent the range of indexes to be returned in a list for the given pagination parameters.

The page numbers start from 1, meaning the first page is referred to as page 1.

```sh
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```

**File:**

- File: `0-simple_helper_function.py`
</details>

<details>
<summary>1. Simple pagination</summary>

Copy `index_range` from the previous task and the following class into your code

```sh
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
```

Create a function called `get_page` that accepts two integer parameters: `page` and `page_size`, with default values of 1 to 10 respectively.

- You need to use this CSV file (The same one shown at the beginning of the project)
- Use `assert` to ensure that both arguments are positive integers.
- Use the `index_range` function to determine the correct indexes for proper pagination of the dataset and return the corresponding page of the dataset (i.e, the correct list of rows).
- If the input arguments are outside the range of the dataset, the function should return an empty list.

```sh
bob@dylan:~$  wc -l Popular_Baby_Names.csv
19419 Popular_Baby_Names.csv
bob@dylan:~$
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$
```

**File:**

- File: `1-simple_pagination.py`
</details>

<details>
<summary>2. Hypermedia pagination</summary>

Replicate code from the previous task.

Create a function called `get_hyper` that accepts the same parameters (and default values) as `get_page`. This function should return a dictionary with the following keys and their corresponding values:

- `page_size`: the size of the returned page from the dataset
- `page`: the number of the current page
- `data`: the page of the dataset (same as the return from the previous task)
- `next_page`: the number of the next page, or `None` if there is no next page
- `prev_page`: the number of the previous page, or `None` if there is no previous page
- `total_pages`: the total number of pages in the dataset, represented as an integer

Ensure that you reuse the `get_page` function in your implementation.

If necessary, you can use the `math` module.

```sh
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$
```

**File:**

- File: `2-hypermedia_pagination.py`
</details>

<details>
<summary>3. Deletion-resilient hypermedia pagination</summary>

Sure, here's the rephrased version:

The objective here is to ensure that if certain rows are deleted from the dataset between two queries, the user does not skip any items from the dataset when navigating to a different page.

Begin with this code in `3-hypermedia_del_pagination.py`:

```python
#!/usr/bin/env python3
"""
Hypermedia pagination resilient to deletions
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            truncated_data = data[:1000]
            self.__indexed_dataset = {
                i: data[i] for i in range(len(data))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            pass
```

In this code, the `Server` class is used to paginate a database of popular baby names. The `get_hyper_index` method is yet to be implemented. It will take an index and page size as arguments and return a dictionary.

Create a method named `get_hyper_index` that takes two integers parametes: `index`, which defaults to `None`, and `page_size`, which defaults to 10.

The method should return a dictionary that includes the following key-value pairs:

- `index`: the current starting index of the returned page. This is the index of the first item on the current page. For instance, if the user requests page 3 with a `page_size` of 20 and no data has been removed from the dataset, the current index should be 60.
- `next_index`: the index to query next. This should be the index of the first item following the last item on the current page.
- `page_size`: the size of the current page
- `data`: the actual page of the dataset

**_Requirments/Behaviour:_**

- Use `assert` to ensure that `index` is within a valid range.
- If the user queries index 0 with a `page_size` of 10, they should receive rows indexed from 0 to 9 inclusive.
- If they request the next index (10) with a `page_size` of 10, but rows 3, 6, and 7 have been deleted, the user should still receive rows indexed from 10 to 19 inclusive.

```sh
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

bob@dylan:~$
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
bob@dylan:~$
```

**File:**

- File: `3-hypermedia_del_pagination.py`
</details>
