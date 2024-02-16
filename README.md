
**A coding challenge for Bertram Labs**

******************************

    Coffee Roulette

    By: Garrett Hoiness

    Working as of 2/15/24

******************************

Program prints current coffee prices, sizes, milk options and flavorings

Program iterates through each employee in the roster

    *if the employee is present, they can choose to have their usual or something different
    *if usual is chosen, ingredients are printed along with price
    *if usual is not chosen, components are stepped through to make a drink
    
Once all drinks are taken in, the most expensive coffee is tallied and displayed for bragging or shame accordingly

The total price is also displayed

The users present are then placed in a list and assigned a number

These numbers are then shuffled 3 times in the spirit of 3DES i.e. it doesnt do anything but it helps the creator sleep at night

The top value of the shuffled list is then chosen as the employee to pay

    *if the employee has already paid once that week, they will have a 1 attached to their name in the roster
    *if their name comes up on top, a collision detection is printed
    *shuffling will continue until the employee on top hasnt paid yet

**Usage:**

Please follow this link to the REPL of this program:

https://replit.com/@case85/coffeeroulette

Just press the run button and follow the prompts!

**Assumptions:**

-I assumed that there is a outside file containing the employee roster that would contain some sort of permanent tally 
of who has paid in a week already. For ease of experimentation, I used a roster stored in a list. To see what happens
when many employees have already paid in a week, there are several lines to uncomment around line 400.

-I assumed that there will be no new employees

-I assumed that the user can enter somewhat correct entries. There is some error catching, but it could use more
testing to handle edge cases

-I assume that the program will be run once per day, and did not implement a day of the week tracker
