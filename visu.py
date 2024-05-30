import matplotlib.pyplot as plt

f_euler = open("data_euler", "r")
data_euler = f_euler.read().split("\n")
f_euler.close()
f_rk = open("data_euler_droite", "r")
data_rk = f_rk.read().split("\n")
f_rk.close()
# change theme
plt.style.use('Solarize_Light2')
#11_500
#data = [float(i) for i in data_euler if i != ""][:12_000]
#plt.plot(data)
data = [float(i) for i in data_rk if i != ""]
plt.plot(data)
plt.xlabel("Frame")
plt.ylabel("Moyenne des normes de vitesse")
plt.legend()
# save figure in 1090x720
plt.savefig("euler_gd.png")
# plt.show()
