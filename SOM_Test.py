# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:35:36 2015

@author: student
"""
from mvpa2.suite import *

colors = np.array(
         [[0., 0., 0.],
          [0., 0., 1.],
          [0., 0., 0.5],
          [0.125, 0.529, 1.0],
          [0.33, 0.4, 0.67],
          [0.6, 0.5, 1.0],
          [0., 1., 0.],
          [1., 0., 0.],
          [0., 1., 1.],
          [1., 0., 1.],
          [1., 1., 0.],
          [1., 1., 1.],
          [.33, .33, .33],
          [.5, .5, .5],
          [.66, .66, .66]])

# store the names of the colors for visualization later on
color_names = \
        ['black', 'blue', 'darkblue', 'skyblue',
         'greyblue', 'lilac', 'green', 'red',
         'cyan', 'violet', 'yellow', 'white',
         'darkgrey', 'mediumgrey', 'lightgrey']

"""
Now we can instantiate the mapper. It will internally use a so-called
Kohonen layer to map the data onto. We tell the mapper to use a
rectangular layer with 20 x 30 units. This will be the output space of
the mapper. Additionally, we tell it to train the network using 400
iterations and to use custom learning rate.
"""

som = SimpleSOMMapper((40, 60), 900, learning_rate=0.01)

"""
Finally, we train the mapper with the previously defined 'color' dataset.
"""

som.train(colors)

"""
Each unit in the Kohonen layer can be treated as a pointer into the
high-dimensional input space, that can be queried to inspect which
input subspaces the SOM maps onto certain sections of its 2D output
space.  The color-mapping generated by this example's SOM can be shown
with a single matplotlib call:
"""

pl.imshow(som.K, origin='lower')

"""
And now, let's take a look onto which coordinates the initial training
prototypes were mapped to. The get those coordinates we can simply feed
the training data to the mapper and plot the output.
"""

mapped = som(colors)

pl.title('Color SOM')
# SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
for i, m in enumerate(mapped):
    pl.text(m[1], m[0], color_names[i], ha='center', va='center',
           bbox=dict(facecolor='white', alpha=0.5, lw=0))

"""
The text labels of the original training colors will appear at the 'mapped'
locations in the SOM -- and should match with the underlying color.
"""

# show the figure
if cfg.getboolean('examples', 'interactive', True):
    pl.show()

"""
The following figure shows an exemplary solution of the SOM mapping of the
3D color-space onto the 2D SOM node layer:
.. image:: ../pics/ex_som.*
   :align: center
   :alt: Color-space mapping by a self-organizing map.
"""