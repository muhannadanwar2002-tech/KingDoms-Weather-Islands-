# KingDoms-Weather-Islands-

## Play Weather Islands on Roblox:https://www.roblox.com/games/80518464244305/Weather-Islands

## KINGDOMS is a Saudi-inspired survival game project. Its first chapter takes place in the AlUla desert, where water, shelter, and player choices matter. Two machine learning notebooks explore different questions about that chapter. Can a player survive the conditions ahead? What does a choice reveal about how they play?

## Survival in AlUla

The survival notebook starts with 12,660 simulated scenarios across four biomes and selects the desert scenarios for modeling. It uses information available before play, including starting health, hydration, and expected exposure time, to predict whether the player survives. Scenarios that share a weather record stay together during splitting so the model is evaluated on unseen weather records.

Of the four models compared, logistic regression achieved the highest mean validation F1. The notebook reports 76.7% test accuracy, 0.591 survivor F1, and 73.7% survivor precision. In the held-out simulation, 157 of the 213 players predicted to survive actually survived. These results are exploratory because the initial data analysis included the full dataset.

## The Seven Sins choice classifier

The second notebook trains a decision tree on 20 hand-labeled choices. Each choice has seven consequence weights scored from 0 to 5. The tree uses those weights to classify one action as one of the seven deadly sins or as Neutral. For example, demanding extra coins before letting a caravan use the shade has an exploitation weight of 4 and receives the label Greed.

All 20 examples are used for training. To try a different decision, edit the consequence weights in the last cell. The choice description is printed for the reader, while the weights determine the prediction.

## Explore the project file
How to use it

KINGDOMS-Seven-Sins.html

Open the project presentation in a browser.

Seven_sins_classification (1) (1).ipynb

Open in Jupyter or Google Colab and run the cells in order. The 20 examples are included in the notebook.

Alula_KingDoms_Unit4&5_Project (4).ipynb

Open in Jupyter or Google Colab. To rerun the analysis, supply alula_survival_weather_skills_combined.csv in the notebook’s working directory, then run the cells in order. The CSV is a separate input.
