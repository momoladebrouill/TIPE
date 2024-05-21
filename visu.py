import matplotlib.pyplot as plt

f = open("data", "r")
data = f.read().split("\n")
f.close()
# change theme
plt.style.use('Solarize_Light2')
data = [float(i) for i in data if i != ""][:10000]
plt.plot(data)
plt.xlabel("Frame")
plt.ylabel("Moyenne des normes de vitesse")
plt.legend()
# save figure in 1090x720
plt.savefig("euler.png")
