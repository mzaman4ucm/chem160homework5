import math
import time
import numpy as np
ntrials=100000
t=time.process_time()
x1=np.random.random(ntrials)
y1=np.random.random(ntrials)
x2=np.random.random(ntrials)
y2=np.random.random(ntrials)
dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2))
et=time.process_time()-t
ex_dist=1/15*(math.sqrt(2)+2+5*math.log(1+math.sqrt(2)))
print("Ntrials=%d  Ave dist=%9.7f  Exact dist=%9.7f"%(ntrials,dist,ex_dist))
print("Elapsed time=%6.2f"%(et))