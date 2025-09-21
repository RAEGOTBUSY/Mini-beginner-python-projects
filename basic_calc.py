#calculator 

#numbers 
print("---------------------------------------------------------------------" )
num_a= 6
num_b= 4
print("selected numbers are a:", num_a , " and b:" , num_b)
print("---------------------------------------------------------------------" )
#+,-,*,/,%,**
addition = num_a+num_b
print("addition = " , addition)
subtraction = num_a -num_b
print("subtraction =" , subtraction)
multiplication = num_a *num_b
print("multiplication = " , multiplication)
division =num_a/num_b
print ("division = ",division)
modulo = num_a%num_b
print("modulo = " ,modulo)
exponential = num_a**num_b
print ("exponential = ", exponential)
print("---------------------------------------------------------------------" )
print (" DECIMAL VALUES")
# decimal values 
decimal_of_addition = float(addition)
print("addition = ",decimal_of_addition)
decimal_of_subtraction= float(subtraction)
print("subtraction = ",decimal_of_subtraction)
decimal_of_multiplication = float(multiplication)
print("multiplication= ", decimal_of_multiplication)


print("---------------------------------------------------------------------" )
# comparing values of each
print("COMPARING VALUES" )
print ("is addition  value greater than subtracted value : " , addition >= subtraction , " |  addition value  :" , addition , "  subtraction value  :" , subtraction  )
print ("is addition  value less than subtracted value : " , addition <= subtraction , " |  addition value  :" , addition , "  subtraction value  :" , subtraction  )
print ("is addition  value greater than multiplication value : " , addition >= multiplication , " |  addition value  :" , addition , "  multiplication value  :" , multiplication  )
print ("is addition  value less  than multiplication value : " , addition <= multiplication , " |  addition value  :" , addition , "  multiplication value  :" , multiplication  )
print ("is addition  value greater than division value : " , addition >= division , " |  addition value  :" , addition , "  division value  :" , division  )
print ("is addition  value less than division value : " , addition <= division , " |  addition value  :" , addition , "  division value  :" , division  )


#true or false ( a and b numbers have no value 0 among all the calculations )
print("---------------------------------------------------------------------" )
value = 0
results =[addition, subtraction,multiplication,division,modulo,exponential]
print (" Does value 0 exist in this calculation : ", value in results)
print("---------------------------------------------------------------------" )
