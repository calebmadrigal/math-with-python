import random, math

NUM_POINTS = 10000

# Function for which we want to find area from (x=0 to 10).
f = lambda x: 5 * math.sin(6 * x) + 3 * math.sin(2 * x) + 7

# Sample rectangle will be (x,y) such that 0 <= x <= 10 and 0 <= y <= 14.
rect_width = 10
rect_height = 14

# Funcitions to generate samples for x and y respectively.
rand_x = lambda: random.uniform(0, rect_width)
rand_y = lambda: random.uniform(0, rect_height)

# Generate random sample points.
points = [(rand_x(), rand_y()) for i in xrange(NUM_POINTS)]

# Find points under our function
points_under = filter(lambda point: point[1] <= f(point[0]), points)

# Area = area of domain rectangle * num_points_under/num_points_total
area = rect_width * rect_height * len(points_under)*1.0/len(points)
print "Estimate of area under the curve:", area

