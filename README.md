## Welcome to my API Test Automation - Home Assignment

### Exam 1 - Types
In this test I fetched the JSON from the specific type (fire) 
and save it in set to keep unique value only and assert its length to 20.


### Exam 2 - Pokemons in type JSON 
In this test I fetched the fire pokemons, 
validated the ID of the returned types and searched for 2 specific pokemons, 
one was supposed to exist there and one not.

### Exam 3 - The heaviest Pokemons
This test fetches the data in 2 steps. 
First - it fetches the pokemons list of Fire type, and then for each pokemon - it fetches the additional data to search for the weight field.
After all pokemons were fetched, we sort the pokemons list by their weight and take the first 5 ones in descending order.


## How to run 
1. Clone this project to your local computer.
2. This project already contains the packages (requests, configparser) folder for your ease, so if you're using Windows - just type in the terminal "pytest"
3. And everything is done!

Good luck! :)
