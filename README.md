# EPAiV5-Session10 - Iterability in Polygon Module

## Overview
The **Polygons Module** provides a Python implementation for representing regular polygons and a collection of polygons. This module offers an object-oriented approach to handling geometric properties of polygons, as well as an iterable and subscriptable sequence of polygons with a common circumradius.

The module consists of three primary classes:

1. '**Polygon**': Represents a single regular polygon.
2. '**Polygons**': Represents a sequence of polygons with varying numbers of edges but a common circumradius. This class is both iterable and subscriptable.
3. '**PolygonsIterator**': Provides iteration functionality for the Polygons class.
This README will walk you through the functionality provided by each class and how to use them effectively in your Python projects.

## Class Polygon
### Description
The '**Polygon**' class represents a single regular polygon, which is a geometric figure with equal-length sides and equal angles between them. The class allows you to create a polygon with a specified number of vertices ('**n**') and a circumradius ('**R**'), which is the radius of the circle that can be circumscribed around the polygon.

### Attributes

- '**count_vertices**': Returns the number of vertices (or edges) of the polygon.
- '**'circumradius**': Returns the circumradius of the polygon.
- '**interior_angle**': Returns the interior angle of the polygon.
- '**side_length**': Returns the length of each side of the polygon.
- '**apothem**': Returns the apothem (the distance from the center to the midpoint of a side).
- '**area**': Returns the area of the polygon.
- '**perimeter**': Returns the perimeter of the polygon.

### Methods

- **`__init__(self, m, R)`**: Constructor that initializes a polygon with n vertices and circumradius R.
- **`__repr__(self)`**: Provides a string representation of the polygon.
- **`__eq__(self, other)`**: Checks equality between two polygons based on the number of edges and circumradius.
- **`__gt__(self, other)`**: Compares two polygons to see if one has more vertices than the other.

### Example Usage

```
polygon = Polygon(5, 10)  # Creates a regular pentagon with circumradius 10
print(polygon.area)       # Outputs the area of the pentagon

```

## Class Polygons

### Description
The '**Polygons**' class represents a sequence of regular polygons with a shared circumradius. This class can generate all polygons with a number of edges ranging from 3 (triangle) to '**m**', where '**m**' is the maximum number of edges specified at the time of creation. The '**Polygons**' class is designed to be both iterable and subscriptable, providing flexibility in how you interact with the sequence.

### Attributes

- '**m**': The maximum number of edges for polygons in the sequence.
- '**R**': The circumradius shared by all polygons in the sequence.
- '**max_efficiency_polygon**': Returns the polygon with the highest area-to-perimeter ratio (efficiency).

### Methods

- **`__init__(self, m, R)`**: Constructor that initializes a sequence of polygons with maximum edges m and circumradius R.
- **`__len__(self)`**: Returns the number of polygons in the sequence.
- **`__repr__(self)`**: Provides a string representation of the sequence of polygons.
- **`__iter__(self)`**: Returns an iterator (PolygonsIterator) for the sequence.
- **`__getitem__(self, index)`**: Allows access to a specific polygon in the sequence using subscript notation.

### Subscriptability

The '**Polygons**' class is subscriptable, which means you can access individual polygons in the sequence using index notation. This is particularly useful when you want to retrieve a specific polygon without iterating through the entire sequence.


```
polygons = Polygons(5, 10)
first_polygon = polygons[0]  # Accesses the first polygon in the sequence
third_polygon = polygons[2]  # Accesses the third polygon in the sequence

```

### Example Usage

```
polygons = Polygons(5, 10)  # Creates a sequence of polygons with up to 5 edges

# Iteration
for polygon in polygons:
    print(polygon)

# Subscriptability
print(polygons[0])  # Outputs the first polygon in the sequence
print(polygons[2])  # Outputs the third polygon in the sequence

```

## Class PolygonsIterator

### Description

The PolygonsIterator class is responsible for providing the iteration functionality for the Polygons class. This class maintains the state of the current position in the sequence and defines the logic to move through the sequence of polygons.

### Methods

- **`__init__(self, polygons)`**: Constructor that initializes the iterator with a list of polygons.
- **`__iter__(self)`**: Returns the iterator object itself.
- **`__next__(self)`**: Returns the next polygon in the sequence. Raises a StopIteration exception when all polygons have been iterated over.

### Example Usage

The '**PolygonsIterator**' class is typically used internally by the '**Polygons**' class, so you generally won’t need to interact with it directly.


```
polygons = Polygons(5, 10)
iterator = iter(polygons)
print(next(iterator))  # Outputs the first polygon in the sequence

```

## Iterable and Iterator
In the provided Python code, the '**Polygons**' class is the iterable, and the '**PolygonsIterator**' class is the iterator. Here's an explanation of each:

#### Iterable: Polygons

'**Polygons**' is a class that can be iterated over. An object is considered iterable if it implements the **`__iter__()`** method, which returns an iterator. In the code, the '**Polygons**' class implements the **`__iter__()`** method, which returns an instance of the '**PolygonsIterator**' class. The '**Polygons**' class represents a collection of polygons, where each polygon has a different number of edges but shares the same circumradius. When you create an instance of '**Polygons**', you can iterate over it using a for loop or any other iteration context (e.g., list comprehension, next() function).

#### Iterator: PolygonsIterator

'**PolygonsIterator**' is the class that handles the actual iteration process. An iterator is an object that implements the **`__next__()`** method and the **`__iter__()`** method. The **`__next__()`** method is responsible for returning the next item in the sequence. It raises a StopIteration exception when there are no more items to return.
The PolygonsIterator class is initialized with a list of polygons, and it keeps track of the current position in this list with an internal index (self._index). Each time **`__next__()`** is called, it returns the next polygon in the sequence and increments the index. Once all polygons have been returned, it raises a StopIteration exception to signal that the iteration is complete.

'**Polygons (Iterable)**': The class that defines how to create an iterable sequence of polygons. It provides the **`__iter__()`** method, which returns an instance of '**PolygonsIterator**'.

'**PolygonsIterator (Iterator)**': The class that manages the iteration process over the sequence of polygons. It implements **`__next__()`** to return polygons one by one until the sequence is exhausted.


## Installation

Simply copy the code for the '**Polygon**', '**Polygons**', and '**PolygonsIterator**' classes into your Python project. There are no external dependencies for this module beyond Python's standard library.

## Use Cases

This module is useful in scenarios where you need to:

- Work with regular polygons and their geometric properties.
- Generate and analyze a sequence of polygons with varying numbers of sides but the same circumradius.
- Perform comparisons and optimizations on polygons based on their geometric attributes.
- Access specific polygons within a sequence using subscript notation.

## Conclusion
The Polygons Module provides a powerful and flexible way to work with regular polygons in Python. Whether you need to analyze individual polygons, iterate through a sequence of them, or access specific polygons by index, this module offers the tools you need. Its object-oriented design makes it easy to extend and integrate into larger projects.

---------------------------------------------------------------------------------------------------------------------------------------------------

**Submission by** - Hema Aparna M

**mail id** - mhema.aprai@gmail.com

---------------------------------------------------------------------------------------------------------------------------------------------------