# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# As per lecture 17 ,we are removing some of the below commands as we dont need
# them in the further video 


# dataset$Age = ifelse(is.na(dataset$Age),
#                      ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),
#                      dataset$Age)
# dataset$Salary = ifelse(is.na(dataset$Salary),
#                      ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)),
#                      dataset$Salary)
# 
# # Section 2 lecture 13: Categorical data
# # Encoding categorical data the dataset
# country = dataset$Country
# country = factor(country,
#                  levels = c('France', 'Spain', 'Germany'),
#                  labels = c(1,2,3)
# )
# dataset$Country = country
# 
# purchased = dataset$Purchased
# purchased = factor(purchased,
#                  levels = c('No', 'Yes'),
#                  labels = c(0,1))
# 
# dataset$Purchased = purchased

# Splitting the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
 training_set[,2:3] = scale(training_set[,2:3])
 test_set[,2:3] = scale(test_set[,2:3])
 