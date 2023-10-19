import matplotlib.pyplot as plt
import random


def pie_chart(n):
    labels = [i for i in range(n)]
    values = [random.randint(0, 25) for i in range(n)]
    plt.pie(values, labels=labels)
    plt.show()
pie_chart(int(input()))