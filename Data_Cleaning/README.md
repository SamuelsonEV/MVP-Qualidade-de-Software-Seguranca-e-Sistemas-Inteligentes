# Data Cleaning

O dataset original foi adquirido no [UCI](https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik)

## Informações do Dataset Original:

A total of 3810 rice grain's images were taken for the two species, processed and feature inferences were made. 7 morphological features were obtained for each grain of rice.
Among  the certified rice grown in TURKEY,  the  Osmancik species, which has a large planting area since 1997 and the Cammeo species grown since 2014 have been selected for the study.  When  looking  at  the  general  characteristics  of  Osmancik species, they have a wide, long, glassy and dull appearance.  When looking at the general characteristics of the Cammeo species, they have wide and long, glassy and dull in appearance.  A total of 3810 rice grain's images were taken for the two species, processed and feature inferences were made. 7 morphological features were obtained for each grain of rice.

Features
Variable Name	Type
* Area	Integer		Returns the number of pixels within the boundaries of the rice grain
* Perimeter	Continuous		Calculates the circumference by calculating the distance between pixels around the boundaries of the rice grain
* Major_Axis_Length	Continuous		The longest line that can be drawn on the rice grain, i.e. the main axis distance
* Minor_Axis_Length	Continuous		The shortest line that can be drawn on the rice grain, i.e. the small axis distance
* Eccentricity	Continuous		It measures how round the ellipse, which has the same moments as the rice grain
* Convex_Area	Integer		Returns the pixel count of the smallest convex shell of the region formed by the rice grain
* Extent	Continuous		Returns the ratio of the region formed by the rice grain to the bounding box

Target
* Class	Binary		Cammeo and Osmancik


### Additional Variable Information
1.  Area: Returns  the  number  of  pixels  within  the boundaries of the rice grain.
2.  Perimeter: Calculates the circumference by calculating  the  distance  between  pixels around the boundaries of the rice grain.
3.  Major Axis Length: The longest line that can be drawn on the rice  grain,  i.e.  the  main  axis  distance, gives.
4.  Minor Axis Length: The shortest line that can be drawn on the rice  grain,  i.e.  the  small  axis  distance, gives.
5.  Eccentricity: It measures how round the ellipse, which has  the  same  moments  as  the  rice  grain, is.
6.  Convex Area: Returns  the  pixel  count  of  the  smallest convex shell of the region formed by the rice grain.
7.  Extent: Returns the ratio of the regionformed by the rice grain to the bounding box pixels.
8.  Class: Cammeo and Osmancik rices

---

##  Limpando Dataset 
Para trabalharmos com este dataset realizaremos a seguintes operações: 
* Abrir arquivo arff como Dataframe do Pandas
* Separar 200 para serem o golden dataset
* Subistituir o tipo do arroz para Cammeo ou Osmancik por 1 ou 0
* Salvar ambos os Datasets nos seus diretorios finais.

## Dataset Golden
Foi separado 200 entradas ser o dataset golden, escolhidas de forma aleatória. Os demais ficaram no dataset para treinar o modelo.

Para tal execute o ```data_cleanner.py```  
```shell
python data_cleanner.py
```
Resultando no arquivo "clean-healthcare-dataset-stroke-data.csv" no mesmo diretório.