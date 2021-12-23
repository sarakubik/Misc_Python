library(tidyverse)


diabetes <- read.csv("C:\\Users\\hp\\Documents\\Data Science\\data_challenge_files\\diabetes.csv")
View(diabetes)
head(diabetes)
colnames(diabetes)

#frequencies
count(diabetes, 'Age')

#scatterplot with SkinThickness and BMI
ggplot(diabetes, aes(x = SkinThickness, y = BMI)) + 
  geom_point(color='red',alpha=0.5, size=2, shape=21) +
  labs(x="Skin Thickness", y="BMI", subtitle="Scatter plot with diabetes data")+
stat_smooth(method = 'lm')

ggsave("scatterplot_SkinThickness_BMI.jpg")

#linear regression
relation <- lm(BMI ~ SkinThickness, data = diabetes)   #Create the linear regression with x= SkinThickness and y=BMI
                                                        # where each increase in SkinThickness contributes to BMI increase   
                                                        # or you can say BMI is directly proportional to SkinThickness
summary(relation)                                       #Review the results
                                     #Since only linear regression, look at Multiple R-Squared.
                                    # R-squared is the percentage of the dependent variable variation that a linear model explains
                                    #usually the larger the better, so 42% of BMI is explained by SkinThickness.
                                                      # For coefficients, For every unit increase in SkinThickness, BMI should increase by .42

#to calculate the MeanSquared Error, which we want as low as possible
relation_summ <-summary(relation)
mean(relation_summ$residuals^2)
