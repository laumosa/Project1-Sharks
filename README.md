# Project1-Sharks
## Goal
The goal of this project is to analyze the sharks attack database.

## Database description
- Each row of the database refers to a shark attack.
- For each shark attack it is given certain information such as the age of the victim, the species of the shark, the country where it happened, etc.
- The data is mostly qualitative, except for the variables age and time
- The database contains 25.723 rows and 24 columns

## Hypothesis
1. Surfers are more likely to be fataly attacked by a shark than swimmers
2. Young people is more likely to be attacked by a shark than older people
3. The frequency of shark attacks has decreased since the JAWS film was released

## General cleaning:
- Set column names to lowercase and remove leading and trailing whitespaces
- Drop null values
- Drop duplicates
- Drop selected columns useless for the analysis

## Cleaning data for the HYPOTHESIS 1
```
Variables involved:
- "activity": refers to the activity carried out by the vitctim at the moment of the shark attack (eg. swimmming, surfing, fishing, etc.)
- "fatal_(y/n)": refers to the type of the shark attack (fatal or not)
```
**General cleaning:**
- Drop null values
- Cast values into string, so it is possible to run string methods

**"activity" cleaning:**
- Set values to lowercase
- Filter to keep only the rows where the "activity" column contains the words "swim" or "surf"
- Create new column called "activity_swim_surf", with values of "swim" or "surf" depending on whether the word "swim" is present in the "activity" column or not

**"activity" cleaning:**
- Set values to lowercase and remove leading and trailing whitespaces
- Filter to exclude those rows where the value in the "fatal_(y/n)" column is "UNKNOWN"

**Plot results**
![graph_1](figures/graph_1.png)


 
