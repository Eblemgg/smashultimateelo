# Smash Ultimate Elo
Repository for creating elo scores for Super Smash Bros. Ultimate professional players

# What is this?
This repository is a collection of data of head-to-head matchups between professional Smash players competing in national tournaments. It also contains the python code used to scrape the set data as well as the code to create the elo scores. Both of these files will need to modified by the user to work properly (explained in the smashgg-scrapper readme).

# What is Elo and how did you calculate it?
Elo was developed by Arpad Elo, a master-level chess player. The system was designed to be an objective way to evaluate player performance rather than subjectively giving a player points for placing in a tournament. The score has been used by the United States Chess Federation (USCF), college American football, tennis, scrabble, and various video games. There are more sophisticated methods to calculate a player's actual skill such as Glicko-2 and Microsoft's TrueSkill. However, Elo has the advantage of being simple to compute and easy to understand.

I calculated the score using a logistic curve (rather than a normal curve), consistent with the USCF. The default elo is 1000 and I set a constant K value of 32. The K value is a scalar applied to elo adjustments made after set wins and losses. Basically, a higher K value will result in more volatile elo score changes which is good for responsiveness. A lower K value gives more stable estimates. A value of 32 is a good balance between responsiveness and volatillity.

# Known data issues
It can never be simple, right? Data was very good for American and European tournaments. The only thing to note is that sometimes there are hidden blank matches on smashgg brackets when going from pool > farther bracket in the tourny > to Top 16 etc... The set win indicator will be 0 and the player scores will both be -2. These should be deleted (or coded better to ignore these). However, for real sets where the game score is not recorded and a checkmark is given to the player who won, the set indicator is correct but the player scores are -2. We do NOT want to delete these.

The Japanese tournaments are where we have the true issues. There are two main series: Sumabato and Umebura. Sumabato brackets are only on Challonge and must be recorded manually from there (use the log and excel magic skills to get these). Sponsors must be removed (e.g. sst_shuton to shuton). For Umebura, these are on smashgg but they use Japanese Kanji for player names except for some of the more well known players. The issue is I can not save Japanese Kanji to csv files due to a unicode error. I attempted to translate these using googletrans, a google translator. Many could not be translated (those that did are kind of interesting lol). These were defaulted to "Random_Japanese_Player". I used liquipedia to replace top 34 with actual names for those that I couldn't get from smashgg. Unfortunately, this means that most japanese players will be underrated due to playing against lower elo opponents than they should be.
