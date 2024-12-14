import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create random data
data = pd.DataFrame({
    'Feature1': np.random.randn(100),
    'Feature2': np.random.randn(100),
    'Label': np.random.choice(['A', 'B'], 100)
})

# Visualize data
sns.scatterplot(x='Feature1', y='Feature2', hue='Label', data=data)
plt.title("Random Data Visualization")
plt.show()