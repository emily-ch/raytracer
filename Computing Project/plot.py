# -*- coding: utf-8 -*-
"""
plot.py
Emily Chini, 04/12/22
Code for plotting spot diagrams and calculating rms spot radius
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_positions(x, y):
    """
    Function that plots x against y coordinates
    (to observe a spot diagram before refraction)

    Parameters
    ----------
    x: list of x-coordinates (for bundle of rays starting points)

    y: list of y-coordinates (for bundle of rays starting points)

    Returns
    -------
    Plot of x coordinates against y coordinates
    """

    plt.title('Spot diagram of uniform bundle of rays before refraction')
    plt.xlabel('x / mm')
    plt.ylabel('y / mm')
    plt.plot(x, y, 'o', color='blue')

    return plt.show()


def plot_ray(ray):
    """
    A function that plots the vertices of the ray

    Parameters
    ----------
    ray: object of the Ray class

    Returns
    -------
    a matplotlib plot that traces the ray's path using its vertices
    """
    z = []
    x = []

    plt.xlabel('z / mm')
    plt.ylabel('x / mm')

    for i in range(len(ray._points)):
        z.append(ray._points[i][2])
        x.append(ray._points[i][0])

    return plt.plot(z, x, marker='o', linestyle='dashed', linewidth=1,
                    markersize=7)
    plt.grid()
    plt.show()


def spot_pf(rays):
    """
    A function that plots the spot diagram for bundle of rays
    at the paraxial focal plane

    Parameters
    ----------
    rays: list of rays in the collimated beam

    Returns
    -------
    graph of the spot diagram for the bundle of rays after refraction
    """

    x_fp = []  # x values of ray at focal point
    y_fp = []  # y values of ray at focal point

    for ray in rays:

        x_fp.append(ray.p()[0])
        y_fp.append(ray.p()[1])

    plt.xlabel('x / mm')
    plt.ylabel('y / mm')
    plt.title(
        'Corresponding spot diagram for the bundle of rays'
        '\n at the paraxial focal plane')
    plt.plot(x_fp, y_fp, 'o', color='blue')

    return plt.show()


def rms(rays):
    """
    Function calculates the RMS spot radius of a refracted beam of rays
    at the paraxial focus

    Parameters
    ----------
    rays: list of rays in the collimated beam

    Returns
    -------
    RMS_spot_radius: RMS spot radius of the refracted beam of rays
    """

    x_fp = []  # x values of ray at focal point
    y_fp = []  # y values of ray at focal point

    for ray in rays:

        x_fp.append(ray.p()[0])
        y_fp.append(ray.p()[1])

    RMS_spot_radius = np.sqrt(
        (sum((((np.array(x_fp))**2) + ((np.array(y_fp))**2))))/len(x_fp))

    return RMS_spot_radius
