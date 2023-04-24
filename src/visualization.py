import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plot configuration
sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid") 




def visualizing_question_1 (df):
    """This function creates a barplot with two categories for swimmers and surfers and counts the 
    shark attacks they have suffered. The shark attacks are divided into fatal attacks or not. 
    """
    # 1. Create a function that adds percentage annotations to a bar plot.
    def with_hue(plot, feature, Number_of_categories, hue_categories):
        a = [p.get_height() for p in plot.patches]
        patch = [p for p in plot.patches]
        for i in range(Number_of_categories):
            total = feature.value_counts().values[i]
            for j in range(hue_categories):
                percentage = '{:.1f}%'.format(100 * a[(j*Number_of_categories + i)]/total)
                x = patch[(j*Number_of_categories + i)].get_x() + patch[(j*Number_of_categories + i)].get_width() / 2 - 0.15
                y = patch[(j*Number_of_categories + i)].get_y() + patch[(j*Number_of_categories + i)].get_height() 
                graph.annotate("           " + percentage, (x, y), size = 12)
        plt.show()

    # 2. Create barplot
    graph = sns.countplot(x= df["activity_swim_surf"], hue = df["fatal_(y/n)"])
    plt.xlabel("Type of activity")
    plt.ylabel("Count of shark attacks")
    plt.legend(labels = ["NOT fatal attack", "YES fatal attack", "missing values"])
    plt.title("Percentage of shark attacks by type of activity (swimmers or surfers)",fontsize= 16)
    with_hue(graph, df["activity_swim_surf"], 2, 3)
    plt.savefig("figures/graph_1.png")
    plt.show()

    # 3. Open file
    os.system("start figures/graph_1.png")



def visualizing_question_2_a (df):
    """This function creates a barplot with two categories for swimmers and surfers and counts the 
    shark attacks they have suffered. The shark attacks are divided into fatal attacks or not. 
    """

    # 1.Create histplot
    graph = sns.histplot(data=df, x="age", hue="fatal_(y/n)", multiple="stack")
    plt.xlabel("Age")
    plt.ylabel("Count of shark attacks")
    plt.legend(labels = ["YES fatal attack", "NOT fatal attack"], loc = 'upper right')
    plt.title("Age distribution by number of shark attacks and type of activity", fontsize= 16)
    graph.axvline(x=df.age.mean(), c="red", label = "Mean")
    plt.savefig("figures/graph_2.png")
    plt.show()

    # 2. Open file
    os.system("start figures/graph_2.png")




def visualizing_question_2_b (df):
    """This function creates a barplot with two categories for swimmers and surfers and counts the 
    shark attacks they have suffered. The shark attacks are divided into fatal attacks or not. 
    """

    # 1. Create boxplot
    graph = sns.boxplot(data=df, x="fatal_(y/n)", y="age", hue="fatal_(y/n)")
    plt.gca().get_legend().remove()
    plt.xlabel("Fatal attack")
    plt.ylabel("Age")
    plt.title("Age distribution by number of shark attacks and type of activity", fontsize= 16)
    plt.savefig("figures/graph_3.png")
    plt.show()

    # 2. Open file
    os.system("start figures/graph_3.png")




def visualizing_question_3 (df):
    """This function creates a barplot with two categories for swimmers and surfers and counts the 
    shark attacks they have suffered. The shark attacks are divided into fatal attacks or not. 
    """  

    # 1.Create lineplot
    graf_4 = df.groupby(['year'])['year'].count().plot.line().get_figure()
    plt.axvline(x=1975, c="red", label = "jaws")
    plt.legend()
    plt.title("Count of shark attacks by year", fontsize= 16)
    plt.savefig("figures/graph_4.png")
    plt.show()

    # 2. Open file
    os.system("start figures/graph_4.png")
