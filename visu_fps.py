import matplotlib.pyplot as plt

f = open("data_fps_vide", "r")
data1 = f.read().split("\n")
f.close()

f = open("data_fps_backtracking", "r")
data2 = f.read().split("\n")
f.close()

# change theme
plt.style.use('Solarize_Light2')
temps1 = [float(k) for k in data1 if k!='']
temps2 = [float(k) for k in data2 if k!='']
weight1 = [2.0 for k in range(len(temps1))]
weight2 = [2.0 for k in range(len(temps2))]
nb_barres = 120
# En vert quand c'est vide
# plt.hist(temps1, bins = nb_barres, weights = weight1)
plt.hist(temps2, bins = nb_barres, weights = weight2)
tmax = max(temps1)
#plt.axis([0,30,0,50])
plt.xlabel("Temps (en secondes) ")
plt.ylabel("FPS")
plt.legend()
# save figure in 1090x720
plt.savefig("FPStvide.png")
#plt.show()
