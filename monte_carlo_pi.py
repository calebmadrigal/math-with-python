import random

NUM_POINTS = 10000

# Generates random numbers between -1 and 1
def rand(): return random.random() * 2 - 1

# Generate a bunch of random points in the square which inscribes the unit circle.
all_points = [(rand(), rand()) for i in xrange(NUM_POINTS)]

# Find all points which are inside the circle - i.e. points which match the formula for
# a circle: x**2 + y**2 <= 1
points_in_circle = filter(lambda point: point[0]**2 + point[1]**2 <= 1, all_points)

print "Estimate of pi:", 4.0 * len(points_in_circle) / len(all_points)

