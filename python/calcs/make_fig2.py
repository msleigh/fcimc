import pickle
import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname = open("calc1_output.dat", "rb")

fname.readline()
xdata1 = pickle.load(fname)
ydata1 = pickle.load(fname)

fname.readline()
xdata2 = pickle.load(fname)
ydata2 = pickle.load(fname)

fname.readline()
xdata3 = pickle.load(fname)
ydata3 = pickle.load(fname)


plt.plot(xdata1, ydata1, "k-o")
plt.plot(xdata2, ydata2, "k-o")
plt.plot(xdata3, ydata3, "k-o")


ax.xaxis.set_ticks([0.1, 0.5, 1.0, 2.0, 3.0, 4.0])
ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

plt.xlim(0, 4.5)
plt.ylim(0, 1.2)

ax.xaxis.set_label_text("x - cm")
ax.yaxis.set_label_text("T - keV")

plt.legend(["IMC"], loc=9, numpoints=1, frameon=False)

plt.savefig("fig2.png", bbox_inches="tight")

# plt.show()
