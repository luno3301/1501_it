import matplotlib.pyplot as plt
import numpy as np

tanks = ["Sheridan", "M48 Patton", "ИС-4", "STB-1", "60TP Lewandowskiego", "AMX M4 mle. 54", "Jg.Pz. E 100"]
damage = [560, 340, 420, 330, 630, 450, 800]
plt.bar(tanks, damage)
plt.title("Танки")
plt.xlabel("Танки")
plt.ylabel("Разовый урон")
plt.show()