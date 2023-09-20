"""
optical_elements.py
Emily Chini, 28/10/22
Module to describe optical elements, such as refracting surfaces and lenses
"""
import numpy as np

# %%
# functions to be used in the class methods


def normalise(v):
    """
    A function that normalises any 3D vector

    Parameters
    ----------
    v : 1D numpy array that represents a 3D vector

    Returns
    -------
    the corresponding normalised vector
    """

    if len(v) != 3:
        print('Incorrect dimension')
        return None
    else:
        return v/np.sqrt(np.dot(v, v))


def snell(k1, n, n1, n2):
    """
    A function that uses Snell's law of refraction
    to determine the direction vector of the refracted ray

    Parameters
    ----------
    k1: direction vector of the incident ray

    n: direction vector of surface normal

    n1: the refractive index one side of the surface

    n2: the refractive index for the other side of the surface

    Returns
    -------
    k2_hat: the refracted ray direction as a unit vector
    """

    k1_hat = normalise(k1)  # unit vector for incident direction
    n_hat = normalise(n)  # unit vector for surface normal

    theta_1 = np.arccos(np.fabs(np.dot(n_hat, k1_hat)))

    if np.sin(theta_1) > n2/n1:
        print('\nTotal Internal Reflection occurs')
        return None

    else:
        mu = n1/n2

        # using equation for Snell's law in 3D

        a = (np.sqrt(1-((mu**2)*(1 - (np.dot(k1_hat, n_hat)**2))))) * n_hat
        b = mu * (k1_hat - ((np.dot(k1_hat, n_hat))*n_hat))

        k2_hat = a + b

        return k2_hat

# %%


class OpticalElement:

    """
    Class for optical elements to be created
    """

    def propagate_ray(self, ray):
        """
        propagates a ray through the optical element

        Parameters
        ----------
        ray: object of the ray class
        """

        raise NotImplementedError()

        return self

    def propagate_rays(self, rays):
        """
        Method to propagate a beam of rays through an optical element

        Parameters
        ----------
        rays : list of ray objects in the collimated beam,
               each with a starting point and starting direction
        """

        for ray in rays:
            self.propagate_ray(ray)

        return self


class SphericalRefraction(OpticalElement):

    """
    Derived class of OpticalElement for spherical lenses to be created
    """

    def __init__(self, z0=[0, 0, 0], curv=0, n1=0, n2=0, ap_rad=0):
        """
        Parameters
        ----------
        z0: 3D vector for the intercept of the surface with the z-axis

        curv: the curvature of the surface defined by 1/radius of curvature

        n1: the refractive index one side of the surface

        n2: the refractive index for the other side of the surface

        ap_rad: the maximum extent of the surface from the optical axis
        """

        self._z0 = np.array(z0)
        self._curv = curv
        self._n1 = n1
        self._n2 = n2
        self._ap_rad = ap_rad

    def intercept(self, ray):
        """
        Method to return the first valid intercept
        of a ray with the spherical surface

        Parameters
        ----------
        ray: object of the ray class

        Returns
        -------
        intercept: the intercept for the appropriate
                   convex/concave/zero curvature case
        """

        p = ray._points[-1]  # using the last point of the ray as start point

        # unit vector in the direction of the incident ray
        k_hat = normalise(ray._directions[-1])

        if self._curv == 0:  # zero curvature case
            intercept = p + ((self._z0[2] - p[2])/k_hat[2]*k_hat)

            if intercept[0] > self._ap_rad:  # ray misses the lens in this case
                raise Exception('There is no intercept')

            return intercept

        else:
            R = 1/self._curv  # radius of spherical surface

            # vector from the sphere’s centre O to the ray’s starting point
            r = p - (self._z0 + np.array([0, 0, R]))

            disc = np.sqrt((np.dot(r, k_hat))**2 - (np.dot(r, r) - R**2))

            if disc < 0:
                raise Exception("No real solutions so no intercept")

            else:

                if self._curv > 0:  # convex case

                    l_1 = -np.dot(r, k_hat) - disc
                    intercept = p + (l_1*k_hat)

                    if abs(intercept[0]) > self._ap_rad:  # ray misses the lens
                        raise Exception('There is no intercept')

                    return intercept

                elif self._curv < 0:  # concave case

                    l_2 = -np.dot(r, k_hat) + disc
                    intercept = p + (l_2*k_hat)

                    if abs(intercept[0]) > self._ap_rad:  # ray misses the lens
                        raise Exception('There is no intercept')

                    return intercept

    def get_normal(self, ray):
        """
        Method to return the normal for refraction at a spherical surface

        Parameters
        ----------
        ray: object of the ray class

        Returns
        -------
        normal: the normalised direction vector
                for the normal from the refraction at the spherical surface
        """

        if self._curv != 0:  # no R value for zero curvature lens
            R = 1/self._curv

        if self._curv == 0:  # zero curvature case
            normal = normalise([0, 0, 1])

            return normal

        elif self._curv > 0:  # convex case

            normal = normalise((-1*self.intercept(ray)) +
                               self._z0 + np.array([0, 0, R]))
            return normal

        elif self._curv < 0:  # concave case

            normal = -1*normalise((-1*self.intercept(ray)) +
                                  self._z0 + np.array([0, 0, R]))
            return normal

    def snells(self, ray):
        """
        Method to return the refracted ray's new direction vector
        using Snell's law function

        Parameters
        ----------
        ray: object of the ray class

        Returns
        -------
        new_dir: the refracted ray direction vector
        """

        new_dir = snell(ray._directions[-1],
                        self.get_normal(ray), self._n1, self._n2)

        return new_dir

    def propagate_ray(self, ray):
        """
        Method propagates a ray through the spherical optical element

        Parameters
        ----------
        ray: object of the ray class
        """

        ray.append(self.intercept(ray), self.snells(ray))

        return self

    def paraxial_focus(self, ray):
        """
        Method finds the paraxial focus position for the lens

        Parameters
        ----------
        ray: object of the ray class, should be a paraxial ray

        Returns
        -------
        z: the z-coordinate at which the paraxial focus is positioned
        """

        i = len(ray.vertices())

        m = (ray.vertices()[i-1][0] - ray.vertices()[i-2][0]) / \
            (ray.vertices()[i-1][2] - ray.vertices()
             [i-2][2])                                  # gradient of ray
        c = ray.vertices()[i-1][0] - (m*ray.vertices()
                                      [i-1][2])         # y-intercept of ray
        z = -c/m  # finding z-intercept

        return z


class OutputPlane(OpticalElement):

    """
    Derived class of OpticalElement to create an output plane for the rays to
    finish propagation, where they are not refracted
    """

    def __init__(self, z=0):
        """
        Parameters
        ----------
        z : z-coordinate at which the output plane is positioned
        """

        self._z = z
        OpticalElement.__init__(self)

    def intercept(self, ray):
        """
        Method finds the intercept of the ray at the output plane

        Parameters
        ----------
        ray : object of the ray class

        Returns
        -------
        intercept : the point where the ray meets the output plane
        """

        dist = (self._z - ray._points[-1][-1]) / ray._directions[-1][-1]
        intercept = ray._points[-1] + (dist * ray._directions[-1])

        return intercept

    def get_normal(self, ray):
        """
        Method gives the normal of the output plane to be used in Snells

        Parameters
        ----------
        ray : object of the ray class

        Returns
        -------
        normal : defined normal vector to the vertical output plane
        """

        normal = np.array([0, 0, 1])

        return normal

    def snells(self, ray):
        """
        Method for getting ray's new direction vector after passing
        through output plane

        Parameters
        ----------
        ray : object of the ray class

        Returns
        -------
        new_dir : direction vector of ray after it passes through
                  the output plane
                 (same as before it enters the output plane since
                  no refraction occurs)
        """

        new_dir = snell(ray._directions[-1],
                        self.get_normal(ray), 1, 1)

        return new_dir

    def propagate_ray(self, ray):
        """
        Method propagates a ray through the output plane

        Parameters
        ----------
        ray : object of the ray class
        """

        ray.append(self.intercept(ray), self.snells(ray))

        return self

    def redefine_z(self, new_z):
        """
        Method to change the position of the output plane

        Parameters
        ----------
        new_z: new z-axis position of the output plane

        Returns
        -------
        self._z: z-coordinate at which the output plane is positioned
        """

        self._z = new_z

        return self._z
