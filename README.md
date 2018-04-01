# LoadedRPS

Repository for the King of the Hill in StackExchange:
https://codegolf.stackexchange.com/questions/122376/koth-loaded-rps


# The game

The game is a simple "Rock-Paper-Scissors" with a twist: Points gained with each victory increases during the match (your R, P or S get loaded).

 - Paper wins Rock
 - Scissors wins Paper
 - Rock wins Scissors

The winner gets as many points as the load on his play.

The loser increases by 1 the load on his play.

In the case of a tie, each player increases the load on his play by 0.5.

After 100 plays, the one with more points is the winner.

e.g.: P1 has loads [10,11,12] (Rock, Paper, Scissors) and P2 [7,8,9]. P1 plays R, P2 plays P. P2 wins and gets 8 points. P1 loads become [11,11,12], P2 loads stay the same.

# Challenge specifications
Your program must be written in Python (sorry, I don't know how to handle it otherwise). You are to create a function that takes each of these variables as an argument on each execution:

    my_points, opp_points, my_loaded, opp_loaded, my_history, opp_history
`points` - Current points (yours and your opp)

`loaded`- Array with loads (in order RPS) (yours and your opp)

`history`- String with all plays, last character is the last play (yours and your opp)

You must return `"R"`, `"P"` or `"S"`. If you want to return something different, it would be an automatic lose of the match.

# Rules
You cannot change built-in functions.

# Judging

The winner will be decided by selecting the person with the most win matches after 1000 full round-robins. Ties will be broken by matches tied.
1000 matches are being played rather than one because I expect a lot of randomness, and that way the randomness would be less relevant.

You can submit up to 5 bots.

The contest ends on July 4th (that will be the last day I'll accept any answer), and on July 5th I'll post the final standings (might try to post an advancement before).
