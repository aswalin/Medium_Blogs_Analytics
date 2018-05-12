# Medium Blogs Analytics
The goal of this project is to scrape the contents of medium blogs and understand the factors impacting the number of claps/likes on medium.com
We have extracted the contents of blogs related to data science, technology & programming.

This repository contains three files - 
```
1. scrape_links.ipynb - This notebook will first fetch links of blogs using selenium. It will 
then iterate over all the links to extract the features like text, images, links, read time, 
followers & tags etc 
```
```
2. rf_3_class.ipynb - This notebook will convert the number of likes into three bins and fit
a random forest classifier to predict the number bin of claps. It will further explain you the importance
of each feature in determining the number of likes
```

```
3. random_forest.ipynb - This file will use different number of bins to split the target variable. 
It will also extract some advanced features like sentiment score and see how well the new model fits the data
```
