import matplotlib.pyplot as plt
import datetime

plt.axis('auto')

y1=[120,122,124,126]
y2=[100,102,103,104]
X=[datetime.datetime.now()+datetime.timedelta(minutes=i) for i in range(len(y1))]

plt.subplot(1,2,1)
plt.plot(X,y1,'sr')
plt.legend(['Makina1'])


plt.subplot(1,2,2)
plt.plot(X,y2,'m*')

plt.legend(['Makina2'])
plt.gcf().autofmt_xdate()
plt.show()