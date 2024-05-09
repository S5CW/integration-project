import matplotlib.pyplot as plt
import math

"""
Variables & Function  to be integrated
"""

def f(x):
  # mean, sd = 0, 1
  # return (1/(sd*math.sqrt(2*math.pi)))*math.exp(-(((x-mean)/sd)**2)/2) # cartesian eq. of Normal Distribution 
  # # above is not algebraically integrable

  # return math.tan(x)/math.cos(x)
  # return math.sin(x)
  # return math.cos(2*x)/math.cos(x**2)/math.tan(x)
  return x**2



def gradient_method():

  '''
  variables
  '''

  dx = 0.1
  limits = 10
  c = 0

  '''
  definite variables
  '''

  definite = True
  uplim = 5
  lowlim = 0
  if definite: limits = 2*max(uplim, lowlim)



  def connect(p1, p2): # Function to connect two points w/ line
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    
    plt.plot(x_values, y_values, 'bo', linestyle="--")
  
  def estimate(p1, p2, x3):
    return (p2[1]-p1[1])*(x3-p1[0])/(p2[0]-p1[0])+p1[1]


  """
  +/- Integration Method
  """

  plt.rcParams["figure.autolayout"] = True
  p_points = []

  point1 = [0, c]
  point2 = [dx, f(0)*dx]
  p_points.append(point1)

  connect(point1, point2)

  for i in range(round(limits/dx)-1):
    point1 = point2
    point2 = [point1[0]+dx, point1[1]+f(point1[0])*dx]
    
    connect(point1, point2)
    p_points.append(point1)

  n_points = []

  point1 = [0, c]
  point2 = [-dx, -f(0)*dx]

  connect(point1, point2)

  for i in range(round(limits/dx)-1):
    point1 = point2
    point2 = [point1[0]-dx, point1[1]-f(point1[0])*dx]

    connect(point1, point2)
    n_points.append(point1)

  # print(point2)

  points = n_points[::-1] + p_points

  if definite:
    for index, i in enumerate(points):

      try:
        if(i[0]-uplim)/(points[index+1][0]-uplim) <= 0: top = estimate(i, points[index+1], uplim)
      except ZeroDivisionError: top = estimate(i, points[index+1], uplim)
      except: IndexError: i=0 # not sure why pass causes error
      
      try:
        if (i[0]-lowlim)/(points[index+1][0]-lowlim) <= 0: bottom = estimate(i, points[index+1], lowlim)
      except ZeroDivisionError: bottom = estimate(i, points[index+1], lowlim)
      except: IndexError: i=0 # not sure why pass causes error

    print(top-bottom)

      
  plt.grid()
  plt.axvline()
  plt.axhline()
  plt.show()

gradient_method()