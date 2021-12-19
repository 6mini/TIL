import pandas as pd
import matplotlib.pyplot as plt

trips = pd.read_csv("trips-date.csv")
trips.plot()
plt.show()