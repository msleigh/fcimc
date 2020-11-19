import pickle
import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname1 = open("calc6_output.dat", "rb")

time11_str = fname1.readline()
xdata11 = pickle.load(fname1)
ydata11 = pickle.load(fname1)

time12_str = fname1.readline()
xdata12 = pickle.load(fname1)
ydata12 = pickle.load(fname1)

time13_str = fname1.readline()
xdata13 = pickle.load(fname1)
ydata13 = pickle.load(fname1)


fname2 = open("calc7_output.dat", "rb")

time21_str = fname2.readline()
xdata21 = pickle.load(fname2)
ydata21 = pickle.load(fname2)

time22_str = fname2.readline()
xdata22 = pickle.load(fname2)
ydata22 = pickle.load(fname2)

time23_str = fname2.readline()
xdata23 = pickle.load(fname2)
ydata23 = pickle.load(fname2)


plt.plot(xdata21, ydata21, "k-o")
plt.plot(xdata11, ydata11, "k+", linestyle="dotted")

plt.plot(xdata22, ydata22, "k-o")
plt.plot(xdata12, ydata12, "k+", linestyle="dotted")

plt.plot(xdata23, ydata23, "k-o")
plt.plot(xdata13, ydata13, "k+", linestyle="dotted")


ax.xaxis.set_ticks([0.1, 0.5, 1.0, 2.0, 3.0, 4.0])
ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

plt.xlim(0, 4.5)
plt.ylim(0, 1.2)

ax.xaxis.set_label_text("x - cm")
ax.yaxis.set_label_text("T - keV")

plt.legend(["dt = 2e-4 shakes", "dt = 2e-3 shakes"], loc=9, numpoints=1, frameon=False)

plt.savefig("fig6.png", bbox_inches="tight")

# plt.show()
