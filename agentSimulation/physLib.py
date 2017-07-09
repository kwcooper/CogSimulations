location = [x,y]
velocity = [x,y]

def addV(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])
    
# Subtract one vector from another:
def subV(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])
    
# Multiply a vector's components by a scalar (a number):
def multV(v, s):
    return (v[0] * s, v[1] * s)
    
# Divide a vector's components by a scalar (a number):
def divV(v, s):
    return (v[0] / s, v[1] / s)
    
# Calculate the magnitude of the vector: 
def magV(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)
    
# Converts a vector to a unit vector (maximum length of 1):
def normV(v):
    return divide(v, magnitude(v))

#converts two vectors into a scaler
def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

#FInds the angle between two vectors
def theta(v1, v2):
    return cos(dot(v1, v2) / (magV(v1) * magV(v2)))
    

# Scales a vector so its magnitude is equivalent to a scalar (a number):
def clamp(v, s):
    m = magV(v)
    if m > 0:
        return multV(v, s / m)
    else:
        return v

