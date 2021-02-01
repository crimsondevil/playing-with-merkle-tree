# playing-with-merkle-tree

All the screenshots are based in a Windows OS environment; so instead of "cat" command, I have used "type" command to view the files on cmd.

# buildmtree.py

In this file, the names(leaf nodes) are given as argument in the command line along with the script to run the file. The program then uses the names and creates hashes of them using SHA256 and forms a binary tree to produce a merkle tree hash and store them in a file called "merkle.tree". Upon viewing the file "merkle.tree", we can see the names with their hash, then combining the hashes 2 at a time to generate a new hash which continues up to the level where we generate the root node hash, thereby creating a merklr tree.
  
Sample commands to run the file "buildmtree.py" and view "merkle.tree" :-
  
    py buildmtree.py alice bob carlol david
    type merkle.tree

# checkinclusion.py

In this file, it searches for the name given in command line in the previously created "merkle.tree", and checks if it exists as one of the leaf nodes. If it does not have a match in the tree, it prints a "No." in the cmd; If it finds a match in the tree, it prints "Yes." along with the hashes leading from the leaf node of that name to the root node of the tree. 

Sample commands to run the file "checkinclusion.py" :-

    py checkinclusion.py richard
    
    py checkinclusion.py david

# checkconsistency.py

In this file, it, first, creates 2 merkle trees and stores them in a file called "merkle.trees". It, then, checks if the first tree is a subset of the second tree, if all the names from the first tree are found in the same order in the second tree, and if all the new names in the second tree append the names from the first tree in the same sequence. If any of the conditions are not met, then it prints a "no.". If all the conditions are met accordingly, then it prints a "yes." along with the hashes leading from the root node of the first tree that is also present in the second tree to the root of the second tree. 

Sample commands to run the file "checkconsistency.py" and view "merkle.trees" :-

    py checkconsistency.py [alice, bob, carlol, david] [alice, bob, carlol, david, eve, fred]
    type merkle.trees
    
    py checkconsistency.py [alice, bob, carlol, david] [alice, bob, david, eve, fred]
    type merkle.trees
    
    py checkconsistency.py [alice, bob, carlol, david] [alice, bob, carlol, eve, fred, david]
    type merkle.trees
