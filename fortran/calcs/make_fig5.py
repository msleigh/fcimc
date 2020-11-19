import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname1 = open("calc1_output.dat", "r")

fname1.readline()
xdata11 = [float(i) for i in fname1.readline().split()]
ydata11 = [float(i) for i in fname1.readline().split()]

fname1.readline()
xdata12 = [float(i) for i in fname1.readline().split()]
ydata12 = [float(i) for i in fname1.readline().split()]

fname1.readline()
xdata13 = [float(i) for i in fname1.readline().split()]
ydata13 = [float(i) for i in fname1.readline().split()]


fname2 = open("calc5_output.dat", "r")

fname2.readline()
xdata21 = [float(i) for i in fname2.readline().split()]
ydata21 = [float(i) for i in fname2.readline().split()]

fname2.readline()
xdata22 = [float(i) for i in fname2.readline().split()]
ydata22 = [float(i) for i in fname2.readline().split()]

fname2.readline()
xdata23 = [float(i) for i in fname2.readline().split()]
ydata23 = [float(i) for i in fname2.readline().split()]


fname3 = open("calc6_output.dat", "r")

fname3.readline()
xdata31 = [float(i) for i in fname3.readline().split()]
ydata31 = [float(i) for i in fname3.readline().split()]

fname3.readline()
xdata32 = [float(i) for i in fname3.readline().split()]
ydata32 = [float(i) for i in fname3.readline().split()]

fname3.readline()
xdata33 = [float(i) for i in fname3.readline().split()]
ydata33 = [float(i) for i in fname3.readline().split()]

plt.plot(xdata31, ydata31, "k-o")
plt.plot(xdata11, ydata11, "kx", linestyle="dotted")
plt.plot(xdata21, ydata21, "ko", markerfacecolor="white")

plt.plot(xdata32, ydata32, "k-o")
plt.plot(xdata12, ydata12, "kx", linestyle="dotted")
plt.plot(xdata22, ydata22, "ko", markerfacecolor="white")

plt.plot(xdata33, ydata33, "k-o")
plt.plot(xdata13, ydata13, "kx", linestyle="dotted")
plt.plot(xdata23, ydata23, "ko", markerfacecolor="white")


ax.xaxis.set_ticks([0.1, 0.5, 1.0, 2.0, 3.0, 4.0])
ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

plt.xlim(0, 4.5)
plt.ylim(0, 1.2)

ax.xaxis.set_label_text("x - cm")
ax.yaxis.set_label_text("T - keV")

plt.legend(
    ["dx = 0.16 cm", "dx = 0.4 cm", "dx = 0.8 cm"], loc=9, numpoints=1, frameon=False
)

plt.savefig("fig5.png", bbox_inches="tight")

# plt.show()
