# -*- coding: utf-8 -*-
"""
lens_optimization.py
Emily Chini, 3/12/22
Using the ray-tracer to optimise the design of a biconvex lens
"""

import numpy as np
import scipy.optimize as sp
import raytracer as rt
import optical_elements as oe
import plot as pt


def optimize_rms(curvs):

    # lens config. where convex surface faces the input
    conv_surf1 = oe.SphericalRefraction(
        z0=[0, 0, 100], curv=curvs[0], n1=1, n2=1.5168, ap_rad=100)
    conv_surf2 = oe.SphericalRefraction(
        z0=[0, 0, 105], curv=curvs[1], n1=1.5168, n2=1, ap_rad=100)

    # at paraxial focus of plano convex lens, where convex surface faces input
    output_plane = oe.OutputPlane(z=198.45)

    elems = [conv_surf1, conv_surf2, output_plane]

    # for a beam with diameter 10mm
    radius = [5]

    for i in range(len(radius)):
        bundle = rt.Bundle((np.linspace(0, radius[i], 6)), [
            1, 10, 20, 30, 40, 50], 0, [0, 0, 1])

        bundle.positions()

        rays = bundle.create_rays()

        for elem in elems:
            elem.propagate_rays(rays)

        rms = pt.rms(rays)

        # plots spot diagram
        # for each implementation of the minimisation algorithm

        pt.spot_pf(rays)  # comment out to run code quickly

    return rms


# x0 array from plano convex lens curvatures, 0.02 and -0.02

x, nfeval, rc = sp.fmin_tnc(optimize_rms, np.array([0.02, -0.02]), bounds=[
    (-0.05, 0.05), (-0.05, 0.05)], approx_grad=True)

print('Curvature 1:', x[0], '\nCurvature 2:', x[1])

optim_rms = optimize_rms(x)
print('\nOptimised RMS:', optim_rms)
