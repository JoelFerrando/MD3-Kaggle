# MD3-Kaggle
### Nom:   Joel Ferrando Ruiz
### DATASET: Telugu Vowel Dataset
### URL: [kaggle](https://www.kaggle.com/syamkakarla/telugu-6-vowel-dataset)

## Descripció
El dataset utilitza dades del llenguatge Telegu on es diferencien els 'pixels' i la 'class'. <br>
Conté 1200 instàncies i 785 variables (tipus númeriques (Int64)). <br>
El dataset no conté cap Null.

## Objectiu
L'objectiu del Dataset será predir quina vocal del llenguatge Telegu és.

### Experiments
S'utilitzaren diferents models classificadors com el KNN, Random Forest, SVM... amb diferents configuracions de hiperparàmetres per aconseguir la millor 'Accuracy' possible.

### Model
KNN <br>
![imagen](https://user-images.githubusercontent.com/80484995/145729911-e8fc6367-b2a9-402c-a7a8-19dc6a0c5a9e.png)

Random Forest <br>
![imagen](https://user-images.githubusercontent.com/80484995/145729930-49c9dfde-9414-487e-ae6d-90fc20021a6c.png)

SVM <br>
![imagen](https://user-images.githubusercontent.com/80484995/145729941-f793014e-0d3f-438b-bc70-b22373a8af5f.png)

## Resultats finals
![imagen](https://user-images.githubusercontent.com/80484995/145730053-6b524039-ecb2-47be-930b-0d3390f46e4b.png)
![imagen](https://user-images.githubusercontent.com/80484995/145730035-d47b3061-7dd1-4338-a01b-313491515661.png)

## Conclusions
Després d'analitzar, preprocesar les dades, i utilitzar diferents models classificadors amb diferents hiperparàmetres podem concluir que el millor model classificador aplicat és SVM, tant per 'Accuracy' com en Temps.

## Idees per treballar en un futur
· Treballar amb més vocals del llenguatge Telegu. <br>
· Aplicar més models classificadors. <br>
· Probar més configuracions de hiperparàmetres. <br>

## Desenvolupament
El projecte s'ha realitzat utilizant PyCharm Community Edition 2021.2.2 i Google Colaboratory.
