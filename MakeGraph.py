import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

count=1001
y1=[]

counter=0
for i in range (5000):
    if (counter % 100 == 0):
        y1.append(count)
    count+=1
    counter += 1


resavg=[]
randavg=[]
totalavg=[]

counter=0
with open("resavg.txt") as f:
    for line in f:
        if (counter%100==0):
            resavg.append(float(line.strip()))
        counter+=1

counter=0
with open("randavg.txt") as g:
    for line in g:
        if (counter % 100 == 0):
            randavg.append(float(line.strip()))
        counter += 1

counter=0
with open("totalavg.txt") as h:
    for line in h:
        if (counter % 100 == 0):
            totalavg.append(float(line.strip()))
        counter += 1


c0=0
sumerror=0
randerror=0
for k in range(len(totalavg)):
    sumerror=abs(totalavg[c0]-randavg[c0])
    c0+=1

print("Randerror avg:")
print(sumerror/len(totalavg))

c0 = 0
sumerror2 = 0
reserror = 0
for k in range(len(totalavg)):
    sumerror2=abs(totalavg[c0]-resavg[c0])
    c0+=1

print("Reserror avg:")
print(sumerror2/len(totalavg))



trace0 = go.Scatter(
    y = totalavg,
    x = y1,
    mode = 'lines',
    name = 'total'
)
trace1 = go.Scatter(
    y=randavg,
    x=y1,
    mode='lines',
    name='random'
)
trace2 = go.Scatter(
    y=resavg,
    x=y1,
    mode='lines',
    name='reservoir'
)
data = [trace0, trace1, trace2]

layout = dict(title = 'Comparison of Averages of Trump Support',
              xaxis = dict(title = 'Number of Tweets'),
              yaxis = dict(title = 'Average Support(0 to 1)'),
              )

# Plot and embed in ipython notebook!
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='line-mode')
