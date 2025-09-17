import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
sns.histplot(df["total_bill"],bins=20,kde=True,color="skyblue")         #Histogram + KDE
plt.title("Histogram + KDE")
plt.show()