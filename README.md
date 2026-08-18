Project Title: Road Accident Analysis & Visualization
Overview:
This repository contains the Exploratory Data Analysis (EDA) and visualization code for analyzing a dataset of synthetic road accidents. The project aims to identify patterns, correlations, and high-risk factors—such as environmental, structural, and situational conditions—that contribute to the likelihood of road accidents.

Objectives:
Examine the distribution of accidents across various road types (rural, urban, highway).  Analyze the impact of infrastructural factors like curvature, speed limits, and number of lanes.  Investigate the influence of environmental and situational conditions, including lighting, weather, time of day, and seasons on accident risk.  Discover correlations between these conditions and accident severity using visual data-driven interpretations rather than predictive modeling.

Dataset:
The project utilizes the synthetic_road_accidents_2k.csv dataset, which contains over 2000 rows of road accident records. Key features analyzed include Road Type, Curvature, Speed Limit, Weather, Lighting Conditions, Time of Day, and a calculated Accident Risk score (on a 0–1 scale). 

Tech Stack:
Data Processing: Python (pandas)  Data Visualization: matplotlib, seaborn, and squarify  
Visualizations Used: Countplots, Box plots, KDE Plots, Heatmaps, and Line Charts  

Key Insights & Findings:
Road Types: Highways and rural roads generally demonstrate higher accident risks compared to urban roads.  
Infrastructural Impact: Accident risk generally increases with higher speed limits and greater road curvature.  
Environmental Factors: Nighttime (dim lighting) and adverse weather conditions (such as rain or fog) correspond to higher accident probabilities.  
Correlations: Correlation coefficients highlight that curvature and lighting are the top numerical influencers of accident risk.  
