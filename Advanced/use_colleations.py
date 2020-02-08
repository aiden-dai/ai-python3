from collections import namedtuple

# Named tuples assign meaning to each position in a tuple and allow for more readable
Emp = namedtuple('Emp', ['name', 'age'])
e1 = Emp('Tom', 12)
print('Employee is {} and age is {}'.format(e1.name, e1.age))
name, age = e1  # use as a regular tuple
print('Employee2 is {} and age is {}'.format(name, age))


# deque: Returns a new deque object initialized left-to-right
# Deques support thread-safe, memory efficient appends 
# and pops from either side of the deque with approximately the same O(1) performance in either direction.

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')  # Add to the right side of the deque.
q.appendleft('y')  # Add to the left side of the deque.
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])

q.pop()  # Remove and return an element from the right side of the deque.
q.popleft()  # Remove and return an element from the left side of the deque.
print(q)  # deque(['a', 'b', 'c'])

q.rotate(1)  # Rotate the deque n steps to the right
print(q)  # deque(['c', 'a', 'b'])

# To be added.
from collections import OrderedDict



# To be added.
from collections import defaultdict


# To be added.
from collections import Counter
