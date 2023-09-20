# -*- coding: utf-8 -*-
"""
tests_tasks_1-8.py
Emily Chini, 04/11/22
Code to test Tasks 1-8
"""
import numpy as np
import raytracer as rt
import optical_elements as oe
import plot as pt

# %%
# Task 2- Testing optical ray methods
ray = rt.Ray([0, 0, 0], [0.5, 0, 1])

ray.append([5, 5, 5], [10, 10, 10])

print('current point of the ray:', ray.p())
print('current direction of the ray:', ray.k())

print(ray.vertices())


# %%
# Task 4- Testing for known intercept of ray

ray2 = rt.Ray([0, 0, 0], [0.5, 0, 1])

surface = oe.SphericalRefraction(
    z0=[0, 0, 5], curv=0.1, n1=1.5, n2=2.5, ap_rad=8)

intercept = surface.intercept(ray2)

print(intercept)
# %%
# Task 4- Testing for known intercept of ray
# testing for tangential intercept
# ray should intercept at z0

ray3 = rt.Ray([-2, 0, 2], [5, 0, 0])

lens = oe.SphericalRefraction(z0=[0, 0, 2], curv=0.01, n1=1, n2=2, ap_rad=1)

intercept = lens.intercept(ray3)

print(intercept)


# %%
# Task 5- Testing Snell's law function in 3D to see refraction
# Snell function takes k1, n, n1, n2 as parameters

# initial test values where initial direction vector normalises to itself

k2_hat = oe.snell([1/np.sqrt(2), 0, 1/np.sqrt(2)], [0, 0, -1], 1, 1.5)

print("\nnew direction vector from Snell's:", k2_hat)


# %%
# Task 5 cont. - critical angle case (theta_1 = critical angle)
# to ensure expected result, k1 and n normalise to themselves

k2_hat = oe.snell([np.sqrt(2)/3, np.sqrt(2)/3, (-1*np.cos(np.arcsin(2/3)))],
                  [0, 0, -1], 1.5, 1)

print("\nnew direction vector from Snell's:", k2_hat)

# %%
# Task 5 cont.- testing for TIR (theta_1 > critical angle)
# k1 doesn't normalise to itself here but this is not necessary

oe.snell([np.sqrt(2)/3, np.sqrt(2)/3, (-1*np.cos(np.arcsin(2/2.5)))],
         [0, 0, -1], 1.5, 1)

# %%
# Task 5 cont.- normal incidence case (theta_1 = 0)
# ray should travel parallel to the surface normal

k2_hat1 = oe.snell([0, 0, 1], [0, 0, 1], 1, 1.5)
k2_hat2 = oe.snell([0, 0, 3], [0, 0, 1], 1, 1.5)  # changing z position

print("\nnew direction vector from Snell's:", k2_hat1)
print("\nnew direction vector from Snell's:", k2_hat2)

# %%
# Task 7- Testing ray propagation for a few rays
# Convex lens test

ray4 = rt.Ray([0, 0, 0], [0.1, 0, 1])
ray5 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray6 = rt.Ray([2, 0, 0], [0.01, 0, 1])
rays = [ray4, ray5, ray6]

conv_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=0.03, n1=1, n2=1.5, ap_rad=100)

output_plane = oe.OutputPlane(z=250)

elems = [conv_surf, output_plane]

print('\nconvex lens')

for j in rays:
    for i in elems:
        i.propagate_ray(j)
    pt.plot_ray(j)

    print('\ncurrent point of ray:', j.p())
    print('\ncurrent direction of ray:', j.k())
    print('\nvertices of ray', j.vertices())
    print('\ndirections of ray', j._directions)
# %%
# Task 7- Testing ray propagation for a singular ray
# Concave lens test

ray7 = rt.Ray([0, 0, 0], [0.1, 0, 1])
ray8 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray9 = rt.Ray([2, 0, 0], [0.01, 0, 1])
rays = [ray7, ray8, ray9]


conc_surf = oe.SphericalRefraction(
    z0=[0, 0, 100], curv=-0.03, n1=1, n2=1.5, ap_rad=100)

output_plane = oe.OutputPlane(z=250)

elems = [conc_surf, output_plane]

print('\nconcave lens')

for j in rays:
    for i in elems:
        i.propagate_ray(j)
    pt.plot_ray(j)

    print('\ncurrent point of ray:', j.p())
    print('\ncurrent direction of ray:', j.k())
    print('\nvertices of ray', j.vertices())
    print('\ndirections of ray', j._directions)
# %%
# Task 7- Testing ray propagation for a singular ray
# Zero curvature lens test

ray10 = rt.Ray([0, 0, 0], [0.1, 0, 1])
ray11 = rt.Ray([-1, 0, 0], [0, 0, 1])
ray12 = rt.Ray([2, 0, 0], [0.01, 0, 1])
rays = [ray10, ray11, ray12]

zero_curv_surf = oe.SphericalRefraction(
    z0=[0, 0, 3], curv=0, n1=1, n2=1.5, ap_rad=10)
# to raise exception of no intercept, change ap_rad to 0.25

output_plane = oe.OutputPlane(z=40)

elems = [zero_curv_surf, output_plane]

print('\nzero curvature lens')


for j in rays:
    for i in elems:
        i.propagate_ray(j)
    pt.plot_ray(j)

    print('\ncurrent point of ray:', j.p())
    print('\ncurrent direction of ray:', j.k())
    print('\nvertices of ray', j.vertices())
    print('\ndirections of ray', j._directions)
