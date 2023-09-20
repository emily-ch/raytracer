# -*- coding: utf-8 -*-
"""
tests_tasks_1-8.py
Emily Chini, 25/11/22
Code to test single spherical refracting surfaces- Tasks 9, 10, 11
"""

import matplotlib.pyplot as plt
import raytracer as rt
import optical_elements as oe
import plot as pt

# %%
# Task 9
# Tracing trajectory of a few rays through a specified spherical surface
# rays start in the input plane z = 0 mm

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.03, n1=1, n2=1.5, ap_rad=100)
conc_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=-0.03, n1=1, n2=1.5, ap_rad=100)
zero_curv_surf = oe.SphericalRefraction(
    z0=[0, 0, 3], curv=0, n1=1, n2=1.5, ap_rad=10)

output_plane = oe.OutputPlane(z=500)
output_plane2 = oe.OutputPlane(z=40)

# optical elements to propagate the ray through
conv_elems = [conv_surf, output_plane]
conc_elems = [conc_surf, output_plane]
zero_curv_elems = [zero_curv_surf, output_plane2]

# convex case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([0, 0, 0], [0.01, 0, 1])
ray3 = rt.Ray([0, 0, 0], [0.02, 0, 1])
ray4 = rt.Ray([0, 0, 0], [0.05, 0, 1])
rays = [ray1, ray2, ray3, ray4]

plt.title('Task 9: Tracing rays for a convex refracting surface')
plt.grid()
for i in rays:
    for j in conv_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()

# concave case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([0, 0, 0], [0.01, 0, 1])
ray3 = rt.Ray([0, 0, 0], [0.02, 0, 1])
ray4 = rt.Ray([0, 0, 0], [0.05, 0, 1])
rays = [ray1, ray2, ray3, ray4]

plt.title('Task 9: Tracing rays for a concave refracting surface')
plt.grid()
for i in rays:
    for j in conc_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()

# zero curvature case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([0, 0, 0], [0.01, 0, 1])
ray3 = rt.Ray([0, 0, 0], [0.02, 0, 1])
ray4 = rt.Ray([0, 0, 0], [0.05, 0, 1])
rays = [ray1, ray2, ray3, ray4]

plt.title('Task 9: Tracing rays for a zero curvature refracting surface')
plt.grid()
for i in rays:
    for j in zero_curv_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()


# %%
# Task 10
# Tracing a ray parallel to the optical axis through system
# to estimate the position of the paraxial focus for a convex lens


conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.03, n1=1, n2=1.5, ap_rad=100)

output_plane = oe.OutputPlane(z=250)

elems = [conv_surf, output_plane]

# using a paraxial ray 0.1mm to optical axis
testray = rt.Ray([0.1, 0, 0], [0, 0, 1])
op_axis_ray = rt.Ray([0, 0, 0], [0, 0, 1])
rays = [testray, op_axis_ray]

for ray in rays:
    for elem in elems:
        elem.propagate_ray(ray)
    pt.plot_ray(ray)
pf = conv_surf.paraxial_focus(testray)
print('Estimation of the position of the paraxial focus:', pf)
plt.show()

# changes the position of the output plane to the paraxial focus
output_plane.redefine_z(pf)

# %%
# Task 11
# Tracing parallel rays for a spherical refracting surface

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.03, n1=1, n2=1.5, ap_rad=100)
conc_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=-0.03, n1=1, n2=1.5, ap_rad=100)
zero_curv_surf = oe.SphericalRefraction(
    z0=[0, 0, 3], curv=0, n1=1, n2=1.5, ap_rad=10)

output_plane = oe.OutputPlane(z=250)
output_plane2 = oe.OutputPlane(z=-10)
output_plane3 = oe.OutputPlane(z=40)

# optical elements to propagate the ray through
conv_elems = [conv_surf, output_plane]
conc_elems = [conc_surf, output_plane2]
zero_curv_elems = [zero_curv_surf, output_plane3]

# convex case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([1, 0, 0], [0, 0, 1])
ray3 = rt.Ray([2, 0, 0], [0, 0, 1])
ray4 = rt.Ray([3, 0, 0], [0, 0, 1])
ray5 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray6 = rt.Ray([-2, 0, 0], [0, 0, 1])
ray7 = rt.Ray([-3, 0, 0], [0, 0, 1])
rays = [ray1, ray2, ray3, ray4, ray5, ray6, ray7]

plt.title('Task 11: Tracing parallel rays for a convex refracting surface')
plt.grid()
for i in rays:
    for j in conv_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()

# concave case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([1, 0, 0], [0, 0, 1])
ray3 = rt.Ray([2, 0, 0], [0, 0, 1])
ray4 = rt.Ray([3, 0, 0], [0, 0, 1])
ray5 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray6 = rt.Ray([-2, 0, 0], [0, 0, 1])
ray7 = rt.Ray([-3, 0, 0], [0, 0, 1])
rays = [ray1, ray2, ray3, ray4, ray5, ray6, ray7]

plt.title('Task 11: Tracing parallel rays for a concave refracting surface')
plt.grid()
for i in rays:
    for j in conc_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()

# zero curvature case

ray1 = rt.Ray([0, 0, 0], [0, 0, 1])
ray2 = rt.Ray([1, 0, 0], [0, 0, 1])
ray3 = rt.Ray([2, 0, 0], [0, 0, 1])
ray4 = rt.Ray([3, 0, 0], [0, 0, 1])
ray5 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray6 = rt.Ray([-2, 0, 0], [0, 0, 1])
ray7 = rt.Ray([-3, 0, 0], [0, 0, 1])
rays = [ray1, ray2, ray3, ray4, ray5, ray6, ray7]

plt.title('Task 11: Tracing parallel rays for a zero curvature'
          ' refracting surface')
plt.grid()

for i in rays:
    for j in zero_curv_elems:
        j.propagate_ray(i)
    pt.plot_ray(i)
plt.show()
