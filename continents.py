import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

while True:
    num_points = int(input("How many points do you want?\n"))

    # Take the point generation formula from part a), and then sum up points that 
    # fall within regions we mark as Africa and Antarctica

    # Generates random spherical coordinates
    phi = np.arccos(1-2*np.random.rand(num_points))
    theta = np.random.uniform(0, 2*np.pi, num_points)

    # Converts spherical coordinates to Cartesian coordinates
    x_sphere = np.sin(phi) * np.cos(theta)
    y_sphere = np.sin(phi) * np.sin(theta)
    z_sphere = np.cos(phi)

    """
    Africa:
    - Minimum Longitude: 17 degrees West (-17)
    - Maximum Longitude: 51 degrees East 
    - Minimum Latitude: 35 degrees South (-35) 
    - Maximum Latitude: 37 degrees North

    """

    # Divide latitudes by 180 and longitudes by 90 so that they fit within the unit sphere
    # Calculating points inside Africa
    africa_count = 0
    for x,y in zip(x_sphere, y_sphere):
        # -20/180 < x < 50/180  and -40/90 < y < 40/90) <- using these bounds is a better approximation than using the actual extremes
        if(-17/180 < x < 51/180  and -35/90 < y < 37/90):
            africa_count += 1

    # Other estimate that did not work as well
    # africa_count2 = 0 
    # for x,z,y in zip(x_sphere, z_sphere, y_sphere):
    #     if(-17/180 < x < 51/180  and -35/90 < z < 37/90 and y < 0):
    #         africa_count2 += 1

    """
    Antarctica:    
    - Minimum Longitude: 180 degrees West (-180)
    - Maximum Longitude: 180 degrees East
    - Minimum Latitude: 90 degrees South (-90)
    - Maximum Latitude: 63 degrees South (-63) 

    Since Antartica spans the entire button of the globe both east and west. This means we only have to check the latitudes

    IMPORTANT UPDATE: Using this approach seemed to create results that were extremely off. (Resulting size was almost twice
    as large as the actual area of Antarctica.) What I did instead to fix this was to observe the original spherical graph
    I produced in sphere.py, and then eyeball the measurements for the x, y, and z values. This gave me results that were much,
    much closer.

    """

    # Calculating points inside Antarctica
    antarctica_count = 0
    for x,y,z, in zip(x_sphere, y_sphere, z_sphere):
        #print(x,y,z)
        if( (-.3 < x < .3) and (-.3 < y < .3) and (z <= -.85)):
            antarctica_count += 1

    # Using radius of earth in kilometers
    radius = 6371

    # we can estimate the area by making it a fraction of the earth's surface area
    antarctica_area_estimate = (antarctica_count / num_points) * (4 * np.pi * radius**2)
    africa_area_estimate = (africa_count / num_points) * (4 * np.pi * radius**2)

    print("\nActual Area of Antarctica: 15 million squared km")
    print("Estimated Area of Antarctica: {:.2f}".format(antarctica_area_estimate))
    print("\nActual Area of Africa: 30 million squared km" )
    print("Estimated Area of Africa: {:.2f}".format(africa_area_estimate))

    
    # different test
    # africa_area_estimate2 = (africa_count2 / num_points) * (4 * np.pi * radius**2)
    # print("Estimated Area of Africa 2: {:.2f}".format(africa_area_estimate2), "\n")
