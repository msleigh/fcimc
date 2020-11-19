import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname1 = open("calc1_output.dat", "r")

time11_str = fname1.readline()
xdata11 = [float(i) for i in fname1.readline().split()]
ydata11 = [float(i) for i in fname1.readline().split()]

time12_str = fname1.readline()
xdata12 = [float(i) for i in fname1.readline().split()]
ydata12 = [float(i) for i in fname1.readline().split()]

time13_str = fname1.readline()
xdata13 = [float(i) for i in fname1.readline().split()]
ydata13 = [float(i) for i in fname1.readline().split()]


fname2 = open("calc2_output.dat", "r")

time21_str = fname2.readline()
xdata21 = [float(i) for i in fname2.readline().split()]
ydata21 = [float(i) for i in fname2.readline().split()]

time22_str = fname2.readline()
xdata22 = [float(i) for i in fname2.readline().split()]
ydata22 = [float(i) for i in fname2.readline().split()]

time23_str = fname2.readline()
xdata23 = [float(i) for i in fname2.readline().split()]
ydata23 = [float(i) for i in fname2.readline().split()]


plt.plot(xdata11, ydata11, "k-o")
plt.plot(xdata21, ydata21, "k--x")
plt.plot(xdata12, ydata12, "k-o")
plt.plot(xdata22, ydata22, "k--x")
plt.plot(xdata13, ydata13, "k-o")
plt.plot(xdata23, ydata23, "k--x")


ax.xaxis.set_ticks([0.1, 0.5, 1.0, 2.0, 3.0, 4.0])
ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

plt.xlim(0, 4.5)
plt.ylim(0, 1.2)

ax.xaxis.set_label_text("x - cm")
ax.yaxis.set_label_text("T - keV")

plt.legend(["dt = 2e-3 shakes", "dt = 1e-2 shakes"], loc=9, numpoints=1, frameon=False)

plt.savefig("fig3.png", bbox_inches="tight")

# plt.show()
