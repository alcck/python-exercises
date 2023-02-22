import numpy as np
import pandas as pd
import matplotlib as plt
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected=True)
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


def createdata(data):
    if (data == 1):
        x = np.random.rand(100, 5)
        df1 = pd.DataFrame(x, columns=['A', 'B', 'C', 'D', 'E'])
        print("Here is a visualization of your data.")
        print(df1.head())

    elif (data == 2):
        x = [0, 0, 0, 0, 0]
        r1 = [0, 0, 0, 0, 0]
        r2 = [0, 0, 0, 0, 0]
        r3 = [0, 0, 0, 0, 0]
        r4 = [0, 0, 0, 0, 0]

        print("Enter values for the columns: \n")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            x[i] = input()
            i = i + 1
        print("Enter values for the first row: \n")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r1[i] = input()
            i = i + 1
        print("Enter values for the second row: \n")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r2[i] = input()
            i = i + 1
        print("Enter values for the third row: \n")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r3[i] = input()
            i = i + 1
        print("Enter values for the fourth row: \n")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r4[i] = input()
            i = i + 1
        df1 = pd.DataFrame([r1, r2, r3, r4], columns=x)
        print("Here is a visualization of your data.")
        print(df1)

    elif (data == 3):
        file = input(("Enter the name of file you wish to upload: \n"))
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
        print("Here is a visualization of your data.")
        print(df1.head())

    else:
        print("Enter a valid number. \n")

    return df1


def plotter(plot):
    if (plot == 1):
        finalplot = df1.iplot(kind="scatter")
    elif (plot == 2):
        finalplot = df1.iplot(kind="scatter", mode="markers", symbol="x", colorscale="paired")
    elif (plot == 3):
        finalplot = df1.iplot(kind="bar")
    elif (plot == 4):
        finalplot = df1.iplot(kind="hist")
    elif (plot == 5):
        finalplot = df1.iplot(kind="box")
    elif (plot == 6):
        finalplot = df1.iplot(kind="surface")
    else:
        print("Enter a valid number. \n")
    return finalplot


def plotter2(plot):
    col = input("Enter the number of columns you want to plot by selecting 1,2 or 3: \n")
    col = int(col)
    if (col == 1):
        colm = input("Enter the columns you want to plot: \n")
        if (plot == 1):
            finalplot = df1[colm].iplot(kind="scatter")
        elif (plot == 2):
            finalplot = df1[colm].iplot(kind="scatter", mode="markers", symbol="x", colorscale='paired')
        elif (plot == 3):
            finalplot = df1[colm].iplot(kind="bar")
        elif (plot == 4):
            finalplot = df1[colm].iplot(kind="hist")
        elif (plot == 5):
            finalplot = df1[colm].iplot(kind="box")
        elif (plot == 6 or plot == 7):
            print("Bubble plot and surface plot requires more than one column argument.")
        else:
            print("Enter a valid number. \n")
        return finalplot

    elif (col == 2):
        print("Enter the columns you want to plot: \n")
        x = input("First column: \n")
        y = input("Second column: \n")
        if (plot == 1):
            finalplot = df1[[x, y]].iplot(kind="scatter")
        elif (plot == 2):
            finalplot = df1[[x, y]].iplot(kind="scatter", mode="markers", symbol="x", colorscale='paired')
        elif (plot == 3):
            finalplot = df1[[x, y]].iplot(kind="bar")
        elif (plot == 4):
            finalplot = df1[[x, y]].iplot(kind="hist")
        elif (plot == 5):
            finalplot = df1[[x, y]].iplot(kind="box")
        elif (plot == 6):
            finalplot = df1[[x, y]].iplot(kind="surface")
        elif (plot == 7):
            size = input("Please enter the size column for the bubble plot: \n")
            finalplot = df1.iplot(kind="bubble", x=x, y=y, size=size)
        else:
            print("Enter a valid number. \n")
        return finalpoint

    elif (col == 3):
        print("Enter the columns you want to plot: \n")
        x = input("First column: \n")
        y = input("Second column: \n")
        z = input("Third column: \n")
        if (plot == 1):
            finalplot = df1[[x, y, z]].iplot(kind="scatter")
        elif (plot == 2):
            finalplot = df1[[x, y, z]].iplot(kind="scatter", mode="markers", symbol="x", colorscale='paired')
        elif (plot == 3):
            finalplot = df1[[x, y, z]].iplot(kind="bar")
        elif (plot == 4):
            finalplot = df1[[x, y, z]].iplot(kind="hist")
        elif (plot == 5):
            finalplot = df1[[x, y, z]].iplot(kind="box")
        elif (plot == 6):
            finalplot = df1[[x, y, z]].iplot(kind="surface")
        elif (plot == 7):
            size = input("Please enter the size column for the bubble plot: \n")
            finalplot = df1.iplot(kind="bubble", x=x, y=y, z=z, size=size)
        else:
            print("Enter a valid number. \n")
        return finalplot
    else:
        print("Enter a valid number. \n")


def main(cat):
    if (cat == 1):
        print("Select the type of plot you need by writing 1-6: \n")
        print("1.Line plot")
        print("2.Scatter plot")
        print("3.Bar plot")
        print("4.Histogram")
        print("5.Box plot")
        print("6.Surface Plot")
        plot = int(input())
        output = plotter(plot)

    if (cat == 2):
        print("Select the type of plot you need by writing 1-7: \n")
        print("1.Line plot")
        print("2.Scatter plot")
        print("3.Bar plot")
        print("4.Histogram")
        print("5.Box plot")
        print("6.Surface Plot")
        print("7.Bubble Plot")
        plot = int(input())
        output = plotter2(plot)

    else:
        print("Enter a valid number. \n")


print("\n")
print("Select the type of data you wish to plot: \n")

print("1.Random data with 100 rows and 5 columns.")
print("2.Customize a data frame with 5 columns and 4 rows.")
print("3.Enter name of the csv file. (agri.csv,ece.csv,gdp.csv,iris.csv or tips.csv)")
data = int(input())
df1 = createdata(data)

cat = input("Press 1 to plot all columns or 2 to specify columns to plot: \n")
cat = int(cat)
main(cat)
