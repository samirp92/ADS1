import numpy as np   # Import the numpy library as np
import pandas as pd  # Import the pandas library as pd
import matplotlib.pyplot as plt # Import matplotlib.pyplot library as plt

df = pd.read_csv('china_population.csv') # To load csv file
print(df) # To print the data set

# Line graph-1
plt.figure(dpi = 300) # To create figure with required resolution
plt.plot(df['Year'], df['Population'], label = 'Total Population') # To plot line graph of Year vs China's total population
plt.plot(df['Year'], df['Urban Population'], label = 'Urban Population') # To plot line graph of Year vs Urban Population
plt.xlim(1955, 2020)  # To set the limit on x-axis        
plt.xlabel('Year', fontsize = 12) # To label the x-axis
plt.ylabel('Population', fontsize = 12) # To label the y-axis
plt.title('China Population', size = 16, color = 'black') # To give title of graph
plt.legend() # To show the elements of the graph
plt.grid()   # To show grid on graph
plt.savefig('line_graph-1.jpeg', dpi = 300) # To save the graph
plt.show()   # To show the graph 

# Line graph-2
plt.figure(dpi = 300)
plt.plot(df['Year'], df['Urban Pop %'], label = 'Urban Pop %') # To plot line graph of Year vs Urban Pop %
plt.xlim(1955, 2020)             
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Urban Population %', fontsize = 12)
plt.title("China's Urban Population %", size = 16, color = 'black')
plt.legend()
plt.grid()
plt.savefig('line_graph-2.jpeg', dpi = 300)
plt.show()

# Line graph-3
plt.figure(dpi = 300)
plt.plot(df['Year'], df['Fertility Rate'], label = 'Fertility Rate') # To plot line graph of Year vs Fertility Rate
plt.xlim(1955, 2020) 
plt.ylim(0,7)  # To set the range on y-axis            
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Fertility Rate', fontsize = 12)
plt.title("Fertility Rate of China's Population", size = 16, color = 'black')
plt.legend()
plt.grid()
plt.savefig('line_graph-3.jpeg', dpi = 300)
plt.show()

# Bar chart
df.sort_values(['Year'], inplace = True) # To make column values in ascending orders
df['Population_Density'] = df.iloc[:,7]  # To copy the 8th column with a new name to plot the bar graph because the existing column name can't be accessible
df.plot.bar(x = 'Year', y = 'Population_Density', rot = 'vertical', width = 0.6, color = 'green') # To plot bar chart of Year vs Population_Density
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Population_Density per km^2', fontsize = 12)
plt.title("China's Population Density per km^2", size = 16, color = 'black')
plt.savefig('bar_graph.jpeg', dpi = 300)
plt.show()

# Pie chart
plt.figure(dpi = 300)
plt.pie(df["Country's Share of World Pop"], labels = df["Year"], autopct='%1.0f%%', startangle = 90, rotatelabels = True, counterclock = False, pctdistance = 0.75, labeldistance  = 1, radius = 0.9) # To plot pie chart of Country's Share of World Pop
plt.title("China's Share of World Population", size = 14, color = 'black')
plt.savefig('pie_chart.jpeg', dpi = 300)
plt.show()
