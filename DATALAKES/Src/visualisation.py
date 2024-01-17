import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data='train.csv'
df=pd.read_csv(data)
print(data)
# Affichage des premières lignes du DataFrame
df.head()
 
///////////
 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
Data = 'train.csv'
df = pd.read_csv(Data)
 
# Affichage du graphique de distribution des survivants
sns.countplot(x='Survived', data=df)
plt.title('Répartition des survivants')
plt.show()
 
 
/////////
 
 
import seaborn as sns
import matplotlib.pyplot as plt
Data = 'train.csv'
df =pd.read_csv(Data)
sns.countplot(x='Pclass', hue='Sex', data=df, palette='Set2')
plt.title('Survie en fonction de la classe sociale et du sexe')
plt.show()
#La relations entre les variables
 
 
 
//////
 
 
import seaborn as sns
import matplotlib.pyplot as plt
Data = 'train.csv'
df =pd.read_csv(Data)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df , palette='viridis')
plt.title('Relation entre l\'âge et le tarif payé en fonction de la survie')
plt.show()
#"Relation entre l'âge, le tarif payé et la survie des passagers du Titanic."