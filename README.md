# **Colorado U.S. congressional voting results**

**Analysis Overview:** The analysis is focused on revealing results for recent U.S. congressional precint in Colorado where we have three methods to get votes: mail-in ballots, punch cards and direct recording electronics (DRE). Although we have different voting methods we will be focusing on analyzing overall results so this audit will be standardized for other type of local elections.

#### Election results

Total votes: 369,711

  ***Percentage and total votes per county***
  - Denver:     82.8%;  306,055 votes ****Largest county***
  - Jefferson:  10.5%;  38,855 votes
  - Arapahoe:   6.7%;   24,801 votes

  ***Percentage and total votes per candidate***
  - Diana DeGette:     73.8%;  272,892 votes ****WINNER***
  - Charles Stockham:  23.0%;  85,213 votes
  - Raymon Doane:      3.1%;   11,606 votes

#### Looking forward with election audits

For further elections this same analysis can be used using the same code but we can add extra value to it by using other known data like the voting method summary and also specifying the election purpose; U.S. congressional / Senator / Local election)

Once we receive the voting method data we need to add three variables to the code:
- Voting method list
- Voting method dictionary
- Each method count
We need to add two for loops, first one that will list the voting methods and then another that will count each method

For the election purpose we just need to indicate in the f-string the purpose.

**Alejandro Madrigal**

**Data Analysis**
