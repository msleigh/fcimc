import pickle
import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.add_subplot(111, aspect=6.9 / 1.4)


fname1 = open("calc1_output.dat", "rb")

fname1.readline()
xdata11 = pickle.load(fname1)
ydata11 = pickle.load(fname1)

fname1.readline()
xdata12 = pickle.load(fname1)
ydata12 = pickle.load(fname1)

fname1.readline()
xdata13 = pickle.load(fname1)
ydata13 = pickle.load(fname1)


fname2 = open("calc3_output.dat", "rb")

fname2.readline()
xdata21 = pickle.load(fname2)
ydata21 = pickle.load(fname2)

fname2.readline()
xdata22 = pickle.load(fname2)
ydata22 = pickle.load(fname2)

fname2.readline()
xdata23 = pickle.load(fname2)
ydata23 = pickle.load(fname2)


fname3 = open("calc4_output.dat", "rb")

fname3.readline()
xdata31 = pickle.load(fname3)
ydata31 = pickle.load(fname3)

fname3.readline()
xdata32 = pickle.load(fname3)
ydata32 = pickle.load(fname3)

fname3.readline()
xdata33 = pickle.load(fname3)
ydata33 = pickle.load(fname3)


plt.plot(xdata11, ydata11, "k-o")
plt.plot(xdata21, ydata21, "k--x")
plt.plot(xdata33, ydata33, "ko", linestyle="dotted", markerfacecolor="white")

# plt.plot(xdata31,ydata31,'ko',linestyle='dotted',markerfacecolor='white')

plt.plot(xdata12, ydata12, "k-o")
# plt.plot(xdata22,ydata22,'k--x')
# plt.plot(xdata32,ydata32,'ko',linestyle='dotted',markerfacecolor='white')

plt.plot(xdata13, ydata13, "k-o")
plt.plot(xdata23, ydata23, "k--x")

ax.xaxis.set_ticks([0.1, 0.5, 1.0, 2.0, 3.0, 4.0])
ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

plt.xlim(0, 4.5)
plt.ylim(0, 1.2)

ax.xaxis.set_label_text("x - cm")
ax.yaxis.set_label_text("T - keV")

plt.legend(
    ["dt = 2e-3 shakes", "dt = 2e-2 shakes", "dt = 5e-2 shakes"],
    loc=9,
    numpoints=1,
    frameon=False,
)

plt.savefig("fig4.png", bbox_inches="tight")

# plt.show()
