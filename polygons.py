import math

class Polygon:
    """
    A class to represent a regular polygon.

    Attributes
    ----------
    n : int
        Number of vertices (or sides) of the polygon. Must be >= 3.
    R : float
        Circumradius of the polygon (the radius of the circle in which the polygon is inscribed).

    Methods
    -------
    count_vertices:
        Returns the number of vertices (or sides) of the polygon.
    count_edges:
        Returns the number of edges of the polygon (same as the number of vertices).
    circumradius:
        Returns the circumradius of the polygon.
    interior_angle:
        Returns the interior angle of the polygon.
    side_length:
        Returns the length of each side of the polygon.
    apothem:
        Returns the apothem (distance from the center to the midpoint of a side).
    area:
        Returns the area of the polygon.
    perimeter:
        Returns the perimeter of the polygon.
    """
    def __init__(self, n, R):
        """
        Constructs all the necessary attributes for the polygon object.

        Parameters
        ----------
        n : int
            Number of vertices (or sides) of the polygon. Must be >= 3.
        R : float
            Circumradius of the polygon.
        """
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R

    def __repr__(self):
        """Returns a string representation of the Polygon object."""
        return f'Polygon(n={self._n}, R={self._R})'

    @property
    def count_vertices(self):
        """Returns the number of vertices (or sides) of the polygon."""
        return self._n

    @property
    def count_edges(self):
        """Returns the number of edges of the polygon (same as the number of vertices)."""
        return self._n

    @property
    def circumradius(self):
        """Returns the circumradius of the polygon."""
        return self._R

    @property
    def interior_angle(self):
        """Returns the interior angle of the polygon."""
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        """Returns the length of each side of the polygon."""
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        """Returns the apothem (distance from the center to the midpoint of a side)."""
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        """Returns the area of the polygon."""
        return self._n / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        """Returns the perimeter of the polygon."""
        return self._n * self.side_length

    def __eq__(self, other):
        """
        Checks if two polygons are equal based on the number of edges and circumradius.

        Parameters
        ----------
        other : Polygon
            The other polygon to compare with.

        Returns
        -------
        bool
            True if the two polygons have the same number of edges and circumradius, False otherwise.
        """
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        """
        Compares two polygons to determine if one has more vertices than the other.

        Parameters
        ----------
        other : Polygon
            The other polygon to compare with.

        Returns
        -------
        bool
            True if the current polygon has more vertices than the other, False otherwise.
        """
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class PolygonsIterator:
    """
    An iterator class for iterating over a sequence of Polygon objects.
    """
    def __init__(self, polygons):
        """
        Constructs all the necessary attributes for the iterator object.

        Parameters
        ----------
        polygons : list
            A list of Polygon objects to iterate over.
        """
        self._polygons = polygons
        self._index = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """
        Returns the next Polygon object in the sequence.

        Returns
        -------
        Polygon
            The next Polygon object in the sequence.

        Raises
        ------
        StopIteration
            If there are no more polygons to return.
        """
        if self._index < len(self._polygons):
            polygon = self._polygons[self._index]
            self._index += 1
            return polygon
        else:
            raise StopIteration


class Polygons:
    """
    A class to represent a sequence of regular polygons.

    Attributes
    ----------
    m : int
        The maximum number of edges for polygons in the sequence.
    R : float
        The circumradius shared by all polygons in the sequence.

    Methods
    -------
    max_efficiency_polygon:
        Returns the polygon with the highest area-to-perimeter ratio.
    """
    def __init__(self, m, R):
        """
        Constructs all the necessary attributes for the polygons sequence.

        Parameters
        ----------
        m : int
            The maximum number of edges for polygons in the sequence. Must be >= 3.
        R : float
            The circumradius shared by all polygons in the sequence.
        """
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

    def __len__(self):
        """
        Returns the number of polygons in the sequence.
        """
        return self._m - 2

    def __repr__(self):
        """
        Returns a string representation of the Polygons object.
        """
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        """
        Returns an iterator object for the sequence of polygons.
        """
        return PolygonsIterator(self._polygons)

    def __getitem__(self, index):
        """
        Returns the polygon at the specified index in the sequence.

        Parameters
        ----------
        index : int
            The index of the polygon to retrieve.

        Returns
        -------
        Polygon
            The polygon at the specified index.
        """
        return self._polygons[index]

    @property
    def max_efficiency_polygon(self):
        """
        Returns the polygon with the highest area-to-perimeter ratio (efficiency).

        Returns
        -------
        Polygon
            The polygon with the maximum efficiency.
        """
        sorted_polygons = sorted(self._polygons, 
                                key=lambda p: p.area / p.perimeter,
                                reverse=True)
        return sorted_polygons[0]