# goodnotes_to_anki
A Python Skript that converts your Goodnotes flashcards into an file to import into Anki

For the Skript to work you first need two folders:
- A folder where your flashcards (as pictures) are imported (mine has the name: Import Index Cards)
- A folder where the cut flash cards are temporarily stored (mine has the name: Überbrückung)
Once created you of course need to cange the paths in the skript

Additionaly you need the folder where Anki reads their files from (for me that is: /Users/florianschwab/Library/Application Support/Anki2/User 1/collection.media/)
You need to change that, as well

Then you need to export your flashcards (Goodnotes Standard Flash cards) from Goodnotes as pictures (this is essential for the skript to cut the flash cards in half)
When finished put the flash cards into the first folder (mine is the folder: Import Index Cards)

After the skript is finished you should be able to import the .tsv file into Anki and Anki should be able to find the correct pictures and file names and put them together
