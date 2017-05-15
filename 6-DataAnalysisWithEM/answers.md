### Answers

Each answer of question 5 is a different source for the answer vector.
Using EM we can associate each answer (4 dimensional data) to one of the 5 clusters corresponding to a possible answer of question 5.
After running EM, we will have associated each answer vector to a source cluster, giving us the vote of each person.
Maybe we can use answers to the 5 questions to better guess initial values (by taking empirical means and variance).

After running EM we can predict whether someone is undecided and target these people with publicity.
