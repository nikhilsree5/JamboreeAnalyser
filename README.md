# Jamboree Analyser

Jamboree has helped thousands of students like you make it to top colleges abroad. Be it GMAT, GRE or SAT, their unique problem-solving methods ensure maximum scores with minimum effort. They recently launched a feature where students/learners can come to their website and check their probability of getting into the IVY league college. This feature estimates the chances of graduate admission from an Indian perspective.This analysis will help Jamboree in understanding what factors are important in graduate admissions and how these factors are interrelated among themselves. It will also help predict one's chances of admission given the rest of the variables.
## 🎯 Objective
This analysis is aimed to help Jamboree in understanding what factors are important in graduate admissions and how these factors are interrelated among themselves. The correlation of different factors with the target variable are to be analysed as well as between different variables. The relation can be verified by formulating a Linear Regression model using the variables. It will also help predict one's chances of admission given the rest of the variables.
## 📝 Project Report
- You can access the complete project python file here - [[Python]](https://github.com/nikhilsree5/Jamboree-Education---Linear-Regression/blob/main/Jamboree_Education_Business_Case%20(1).ipynb)
## 📚 About Data
The data contains 500 entries of students and 8 attributes like GRE score and TOEFL score. GRE scores vary from 290 to 340 where TOEFL score vary from 92 to 120. They follow non normal distribution with mean value of 316.47 and 207.19 respectively.CGPA is varying from 6.8 to 9.92. It follows a normal distribution with mean value of 8.58. 280 students among the 500 have research experience.

**Product Portfolio**
Specializing in distinctive all-occasion gifts, the company's clientele includes a significant number of wholesale customers. 
  
| Feature | Description |
|:--------|:------------|
| Serial No. | Unique row ID|
| GRE Scores | out of 340|
| TOEFL Scores | out of 120 |
| University Rating | out of 5|
| Statement of Purpose Strength | out of 5 |
| Letter of Recommendation Strength | out of 5 |
| Undergraduate GPA | out of 10 | 
| Research Experience | either 0 or 1 | 
| Chance of Admit | ranging from 0 to 1 | 
# Business Recommendations
The most significant predictor variable is CGPA. Followed by GRE score.
TOEFL score, LOR strength and research experience have moderate impact on the chance of admittance.

**Additional data sources for model improvement**

Incorporating diverse and relevant data sources can enhance the predictive power of the Linear Regression model. For example:

Feature Diversity: Add new independent variables (predictors) related to the target variable.
Temporal Data: Include time-series data for seasonal or trend analysis.
Demographic Data: Use geographic or applicant-specific details like age, education level, or region to capture hidden patterns.
Quality Improvements: Ensure data accuracy and completeness, possibly through enriched datasets from third-party providers, or surveys.

**Model implementation in real world**

The model outcome implications in real world is affected by several factors many of which can be quantified. These different factors can be identified and added to the model with deep understanding of the domain and research. Also tracking the key metrices in real time will enhance the performance and alert on model performance degradation.
