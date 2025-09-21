# number comparison game 

print("--------------------------------------------------------------------------------")

# assigning values to 10 numbers 

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = 9,3,6,8,2,4,17,32,2,1
print("selected numbers for he game are: ",n1,n2,n3,n4,n5,n6,n7,n8,n9,n10  )

print("--------------------------------------------------------------------------------")

#comparing the numbers 

game_1 = n1>n2 and n3>n4
game_2 = n3<n5 or n2>n7
game_3 = n6>n1 or n5==n9
game_4 = n5==n9 and n8<n4 
game_5 =  n5==n9 or n8<n4 
print ("chosen comparison is  9>3  and  6>8 : ", game_1 , "| its AND operator")
print ("chosen comparison is 6<2  and  3>17 : ", game_2 , "| its OR operator")
print ("chosen comparison is 4<9  and 2=2 : ", game_3, "| its OR operator")
print ("chosen comparison is 2==2 and 32<8 : ", game_4 , "| its AND operator")
print ("chosen comparison is 2==2 and 32<8 : ", game_5, "| its OR operator")
print("--------------------------------------------------------------------------------")

#DISPLAYING OVER ALL RESULTS 

print("""
overall result:-
Game 1""", game_1 , """
Game 2: """ , game_2, """
Game 3:""",game_3,"""
Game 4:""", game_4 , """
Game 5:""" , game_5, """
""")

