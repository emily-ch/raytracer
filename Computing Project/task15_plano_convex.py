# -*- coding: utf-8 -*-
"""
plano_convex.py
Emily Chini, 02/12/22
Task 15: Modelling a plano-convex singlet lens
"""

import matplotlib.pyplot as plt
import numpy as np
import raytracer as rt
import optical_elements as oe
import plot as pt
# %%
# for the case where the plane surface faces the input

zero_curv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0, n1=1, n2=1.5168, ap_rad=100)

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 105], curv=-0.02, n1=1.5168, n2=1, ap_rad=100)

output_plane = oe.OutputPlane(z=250)

elems = [zero_curv_surf, conv_surf, output_plane]


testray = rt.Ray([0.1, 0, 0], [0, 0, 1])
op_axis_ray = rt.Ray([0, 0, 0], [0, 0, 1])
rays = [testray, op_axis_ray]


for ray in rays:
    for elem in elems:
        elem.propagate_ray(ray)
    pt.plot_ray(ray)
pf = conv_surf.paraxial_focus(testray)
print('Plane surface faces the input')
print('Paraxial focus at z =', pf)
plt.show()

# moving output plane to paraxial focus
output_plane.redefine_z(pf)

# for a range of beam diameters up to 10 mm
radius = [1, 2.5, 5]

for i in range(len(radius)):
    bundle = rt.Bundle((np.linspace(0, radius[i], 5)), [
                       1, 10, 25, 50, 100], 0, [0, 0, 1])

    x, y = bundle.positions()
    pt.plot_positions(x, y)
    rays = bundle.create_rays()

    for elem in elems:
        elem.propagate_rays(rays)

    for ray in rays:
        pt.plot_ray(ray)

    d = radius[i]*2

    plt.title('Task 15: Beam diameter of %.1f mm through a plano convex'
              ' singlet lens \nfor the case where the plane surface'
              ' faces the input' % d)
    plt.show()

    pt.spot_pf(rays)
    print('RMS for beam diameter', d, 'mm:', pt.rms(rays))
# %%
# for the case where the convex surface faces the input

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.02, n1=1, n2=1.5168, ap_rad=100)

zero_curv_surf = oe.SphericalRefraction(
    z0=[0, 0, 105], curv=0, n1=1.5168, n2=1, ap_rad=100)


output_plane = oe.OutputPlane(z=250)

elems = [conv_surf, zero_curv_surf, output_plane]

# finding paraxial focus
testray = rt.Ray([0.1, 0, 0], [0, 0, 1])
op_axis_ray = rt.Ray([0, 0, 0], [0, 0, 1])
rays = [testray, op_axis_ray]


for ray in rays:
    for elem in elems:
        elem.propagate_ray(ray)
    pt.plot_ray(ray)
pf = conv_surf.paraxial_focus(testray)
print('\nConvex surface faces the input')
print('Paraxial focus at z =', pf)
plt.show()

# moving output plane to paraxial focus
output_plane.redefine_z(pf)

# for a range of beam diameters up to 10 mm
radius = [1, 2.5, 5]

for i in range(len(radius)):
    bundle = rt.Bundle((np.linspace(0, radius[i], 5)), [
                       1, 10, 25, 50, 100], 0, [0, 0, 1])

    x, y = bundle.positions()
    pt.plot_positions(x, y)
    rays = bundle.create_rays()

    for elem in elems:
        elem.propagate_rays(rays)

    for ray in rays:
        pt.plot_ray(ray)

    d = radius[i]*2

    plt.title('Task 15: Beam diameter of %.1f mm through a plano convex'
              ' singlet lens \nfor the case where the convex surface'
              ' faces the input' % d)
    plt.show()

    pt.spot_pf(rays)
    print('RMS for beam diameter', d, 'mm:', pt.rms(rays))
