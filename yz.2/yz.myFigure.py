import matplotlib.pyplot as plt
import datetime

y=[120,122,124,126]
X=[datetime.datetime.now()+datetime.timedelta(minutes=i) for i in range(len(y))]

myFigure = plt.figure()

figureAxes = myFigure.add_axes([0.8,0.8,0.9,0.9])
figureAxes.plot(X, y, "m*")
figureAxes.set_xlabel("X ekseni")
figureAxes.set_ylabel("Y ekseni")
figureAxes.set_title("GRAFİK BAŞLIĞI")