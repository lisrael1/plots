import plotly as py
import numpy as np
import cufflinks

x = np.linspace(0, 1, 10000)

sines=30
amp=np.random.normal(0.2,0.01,sines)
offset=np.random.normal(0,0.05,sines)
phase=np.random.normal(0,3,sines)
freq=np.random.normal(200,100,sines)
y=[amp[i]*np.sin(2*np.pi*x*freq[i]+phase[i])+offset[i] for i in range(sines)]

data = [dict(x=x, y=y[i], name='sine %d'%i, type='scatter',mode='lines') for i in range(sines)]
layout=cufflinks.getLayout(title='hello world',xTitle="my x",yTitle='my y')
py.offline.plot(dict(data=data,layout=layout))

