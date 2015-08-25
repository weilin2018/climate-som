import numpy as np
import sompy as SOM
from matplotlib import pyplot as plt
import sys
msz0 = 50
msz1 = 50
cd = msz0*msz1*1*1
dlen = 100*1000*1*1*1#+224
dim = 3
Data = np.random.randint(0,2,size = (dlen,dim))

sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm.train(n_job = 2, shared_memory = 'no')

tmp = np.zeros((msz0,msz1,dim))
codebook = getattr(sm,'codebook')
codebook = SOM.denormalize_by(Data,codebook)
# codebook = SOM.denormalize(Data, codebook)
for i in range (codebook.shape[1]):
    tmp[:,:,i] = codebook[:, i].reshape(msz0,msz1)
from matplotlib import pyplot as plt
tmp.shape
fig = plt.imshow(tmp[:,:,0:3])
