# -*- coding: utf-8 -*-
"""
tests_tasks_12-14.py
Emily Chini, 02/12/22
Tasks 12-14: Testing a single spherical surface, beyond the paraxial limit,
using a beam of rays
"""

import matplotlib.pyplot as plt
import raytracer as rt
import optical_elements as oe
import plot as pt

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.03, n1=1, n2=1.5, ap_rad=100)
output_plane = oe.OutputPlane(z=250)

elems = [conv_surf, output_plane]


# finding paraxial focus
testray = rt.Ray([0.1, 0, 0], [0, 0, 1])
op_axis_ray = rt.Ray([0, 0, 0], [0, 0, 1])
rays = [testray, op_axis_ray]

for ray in rays:
    for elem in elems:
        elem.propagate_ray(ray)
    pt.plot_ray(ray)
pf = conv_surf.paraxial_focus(testray)
print('Paraxial focus at z =', pf)
plt.show()

# redefining output plane position to paraxial focus
output_plane.redefine_z(pf)

# plotting positions of beam before propagation
bundle = rt.Bundle([0, 1, 2.5, 5], [1, 10, 25, 50], 0, [0, 0, 1])
x, y = bundle.positions()
pt.plot_positions(x, y)

rays = bundle.create_rays()

# propagating rays
for elem in elems:
    elem.propagate_rays(rays)

# plotting rays
for ray in rays:
    pt.plot_ray(ray)
plt.title('Task 12: Tracing a large diameter uniform bundle \nof collimated'
          ' rays through a convex lens')
plt.show()

# Task 13- plots spot diagram for bundle of rays at paraxial focal plane
pt.spot_pf(rays)
print('RMS spot radius:', pt.rms(rays))  # outputs RMS spot radius value
