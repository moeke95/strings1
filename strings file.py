# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


player_name_0= "Ruud Gullit"
player_name_1= "Marco van Basten" 

goal_0= 32
goal_1= 54

print(player_name_0+ " " + str( goal_0) +", " + player_name_1+" " +str( goal_1))
scorers = (player_name_0+ " " + str( goal_0) +", " + player_name_1+" " +str( goal_1))
print (scorers )

report = f"{player_name_0} scored in the {goal_0}nd minute\n" + f"{player_name_1} scored in the {goal_1}th minute"

print (report)
       




player= "Marco_van_Basten"
first_name=  player[0:15]
print (first_name)
            
last_name_len= player.find  ("Marco_van_Basten")
print( last_name_len )

player = "Marco_van_Basten"
first_name = player[0:15]
print(first_name)

last_name_len = len(player.split("_")[-1])
print(last_name_len)

name_short= "Marco_van_Basten"