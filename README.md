# Voting-system-in-Beaker


have implemented a decentralized voting system using the Algorand Beaker framework and box storage. The system allows multiple voters to cast their votes in a secure and private manner, where each vote is stored in a separate box.

The voters input the person they want to vote for and the system checks if they have already voted by checking a data dictionary that stores the voter's account address. If they haven't voted yet, they can cast their vote and the system stores their address and the person they voted for in a box.

The system uses the Algorand network to ensure the security and transparency of the voting process. The boxes are encrypted and only accessible with a private key, which ensures the privacy of the voters and the accountability of the voting process. The system also provides a way for another address to be given access to the box storage by opting-in to the asset.

Overall, your decentralized voting system demonstrates how the Algorand Beaker framework and box storage can be leveraged to create secure and transparent decentralized applications.


## How the program works

First of all u gonna have to run the main.py it will create a json will if there is not any for storing the app id's then it will ask the person to tell the candidate they wanna vote where u gonna have to enter the candidate name and it will create a box storage and add it there and it will also add the app id with the person's address in the json and there will always a static address which u can assume as the official address which gonna store the same vlaue as the voters so that later on it can calcualte the result it also gonna keep tract that no one can't vote more than once.

<img width="310" alt="image" src="https://user-images.githubusercontent.com/121616196/217256569-1c452ed3-67c8-40ce-a77a-78ccdce3821e.png">

<img width="300" alt="image" src="https://user-images.githubusercontent.com/121616196/217256916-a608b47d-d26e-4d64-bef4-7170bb4ce9ef.png">

after everyone has voted now u can calulate the results what u have to do it run the results.py file it gonna read the json to take the app id's as its input and gonna take the content of them which is the candidate's names and gonna store them in a list and output it

<img width="107" alt="image" src="https://user-images.githubusercontent.com/121616196/217257307-d5321b95-97ac-4b3a-9cab-44294d43d3ff.png">

in this example there is just one candidate but there can be as many as u want.

