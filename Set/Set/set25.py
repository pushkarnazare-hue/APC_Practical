user1_friends = {"Rehan", "Soham", "Nisarg"}
user2_friends = {"Riya", "Nikhil", "siddhant", "Priya"}
print("Mutual friends:", user1_friends & user2_friends)
print("Friends unique to User 1:", user1_friends - user2_friends)
print("Friends unique to User 2:", user2_friends - user1_friends)
print("Total unique friends:", user1_friends | user2_friends)