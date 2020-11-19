import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname1 = open("calc6_output.dat", "r")

time11_str = fname1.readline()
print(time11_str)
xdata11 = [float(i) for i in fname1.readline().split()]
ydata11 = [float(i) for i in fname1.readline().split()]

time12_str = fname1.readline()
print(time12_str)
xdata12 = [float(i) for i in fname1.readline().split()]
ydata12 = [float(i) for i in fname1.readline().split()]

time13_str = fname1.readline()
print(time13_str)
xdata13 = [float(i) for i in fname1.readline().split()]
ydata13 = [float(i) for i in fname1.readline().split()]


fname2 = open("calc7_output.dat", "r")

time21_str = fname2.readline()
print(time21_str)
xdata21 = [float(i) for i in fname2.readline().split()]
ydata21 = [float(i) for i in fname2.readline().split()]

time22_str = fname2.readline()
print(time22_str)
xdata22 = [float(i) for i in fname2.readline().split()]
ydata22 = [float(i) for i in fname2.readline().split()]

time23_str = fname2.readline()
print(time23_str)
xdata23 = [float(i) for i in fname2.readline().split()]
ydata23 = [float(i) for i in fname2.readline().split()]


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
