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

    # 1.Create barplot
    colors = ['#E69F00', '#56B4E9', '#F0E442'] 
    ax = sns.countplot(x=df["activity_swim_surf"], hue=df["fatal_(y/n)"], data = df, palette=colors)
    ax.set_facecolor('#F0F0F0')

    plt.xlabel('Type of activity', fontsize=14)
    plt.ylabel('Count of shark attacks', fontsize=14)
    plt.title('Percentage of attack type to swimmers or surfers', fontsize=16)

    for p in ax.patches:
        height = int(p.get_height())
        percentage = height / len(df) * 100
        ax.annotate(f'{height}\n{percentage:.1f}%', 
                (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='baseline', 
                fontsize=12, color='black')

    ax.legend(labels=["NOT fatal attack", "YES fatal attack", "missing values"], title_fontsize=12)  # Replace 'Other' with appropriate label
    sns.despine()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.set_ylim(0, 1200)  # Replace 60 with the desired maximum value for y-axis

    plt.savefig("figures/graph_1.png")
    plt.show()

    # 3. Open file
    os.system("start figures/graph_1.png")



def visualizing_question_2_a (df):
 
    # 1.Create histplot
    
    colors = ['#E69F00', '#56B4E9'] 
    graph = sns.histplot(data=df, x="age", hue="fatal_(y/n)", multiple="stack",  palette=colors)
    graph.set_facecolor('#F0F0F0')

    plt.xlabel("Age")
    plt.ylabel("Count of shark attacks")
    plt.legend(labels = ["YES fatal attack", "NOT fatal attack"], loc = 'upper right')
    plt.title("Age distribution by shark attack type", fontsize= 16)
    
    graph.margins(x=0)  

    graph.axvline(x=df.age.mean(), c="red", label = "Mean")

    plt.savefig("figures/graph_2.png")
    plt.show()

    # 2. Open file
    os.system("start figures/graph_2.png")



def visualizing_question_2_b (df):
 
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

    # 1.Create lineplot
    graf_4 = df.groupby(['year'])['year'].count().plot.line().get_figure()
    plt.axvline(x=1975, c="red", label = "jaws")
    plt.legend()
    plt.title("Count of shark attacks by year", fontsize= 16)
    plt.savefig("figures/graph_4.png")
    plt.show()

    # 2. Open file
    os.system("start figures/graph_4.png")
