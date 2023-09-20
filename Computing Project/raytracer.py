"""
raytracer.py
Emily Chini, 28/10/22
Module to describe optical rays and bundles
"""

import numpy as np


class Ray:
    """
    Class for an optical ray to be created
    """

    def __init__(self, start_point=[0, 0, 0], start_direction=[0, 0, 0]):
        """
        Parameters
        ----------
        start_point: takes a defined 3D starting point from the user

        start_direction: takes a defined starting direction from the user
        """

        self._start_point = np.array(start_point)
        self._start_direction = np.array(start_direction)
        self._points = []  # running list of the points the ray hits
        self._directions = []  # running list of the ray's direction vectors
        self._points.append(start_point)
        self._directions.append(start_direction)

    def p(self):
        """
        Method returns the current point of the ray

        Returns
        -------
        current point as last element from points list
        """

        self._current_point = self._points[-1]

        return self._current_point

    def k(self):
        """
        Method returns the current ray direction

        Returns
        -------
        current direction as last element from directions list
        """

        self._current_direction = self._directions[-1]

        return self._current_direction

    def append(self, p, k):
        """
        Method appends a new point and direction to the ray

        Parameters
        ----------
        p: 1D numpy array for new point the ray passes through

        k: 1D numpy array for new direction vector of the ray
        """

        self._points.append(p)
        self._directions.append(k)

        return self

    def vertices(self):
        """
        Method to return all the points the ray has crossed

        Returns
        -------
        all the points along the ray
        """

        return self._points


class Bundle:
    """
    A class for a bundle of rays for a uniform collimated beam,
    where each ray has a starting position and direction vector
    """

    def __init__(self, r, n, z_value, initial_dir):
        """
        Parameters
        ----------
        r : list of radi for each circle in the beam

        n : list of numbers of evenly spaced rays
            in each concentric circle of the beam

        z_value: initial z-coordinate position of the beam of rays

        initial_dir: initial direction vector for the beam of rays
        """

        self._r = r
        self._n = n
        self._z_value = z_value
        self._initial_dir = np.array(initial_dir)
        self._x = []
        self._y = []

    def positions(self):
        """
        Method to return the initial x and y positions
        for each ray in the collimated beam using polar coordinates

        Parameters
        ----------
        n : list of numbers of evenly spaced rays
            in each concentric circle of the beam

        r : list of radi for each circle in the beam

        z_value: initial z-coordinate of the beam of rays

        initial_dir: initial direction vector for the beam of rays

        Returns
        -------
        self._x: list of the x-coordinates for the starting point of the rays

        self._y: list of the y-coordinates of the starting point of the rays
        """

        for i in range(len(self._r)):
            for j in range(self._n[i]):

                theta = (2 * np.pi) / self._n[i]

                self._x.append(self._r[i] * np.cos(j * theta))
                self._y.append(self._r[i] * np.sin(j * theta))

        return self._x, self._y

    def create_rays(self):
        """
        Method to create lots of ray objects and adds them to a list

        Returns
        -------
        rays : list of ray objects in the collimated beam,
               each with a starting point and starting direction
        """

        rays = []

        for i in range(len(self._x)):

            ray_i = Ray([self._x[i], self._y[i], self._z_value],
                        self._initial_dir)  # creating a bunch of ray objects
            rays.append(ray_i)

        return rays
