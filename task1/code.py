 Calculatorn = int(input("Enter number of passengers: "))
for i in range(n):    print("\nPassenger", i + 1) 
  name = input("Enter passenger name: ")   
age = int(input("Enter age: ")) 
  distance = int(input("Enter travel distance in km: ")) 
  print("Classes: 1.Sleeper  2.3AC  3.2AC")   
choice = int(input("Select class: "))  
if choice == 1:    
  rate = 1.0    
  reservation = 20    
  class_name = "Sleeper"  
elif choice == 2:  
rate = 2.0      
reservation = 40
class_name = "3AC"  
else:  
rate = 3.0      
reservation = 50 
class_name = "2AC"    
if distance <= 100:    
  slab_charge = 50  
elif distance <= 300:     
slab_charge = 100 
else:     
slab_charge = 200
Enter number of passengers: 1

Passenger 1
Enter passenger name: Ravi
Enter age: 65
Enter travel distance in km: 250
Classes: 1.Sleeper  2.3AC  3.2AC
Select class: 2

--- Ticket Details ---
Name: Ravi
Class: 3AC
Base fare: 480.0
Reservation fee: 40
Total fare: Rs. 520.0
Cancel ticket? (yes/no): yes
Cancellation penalty: Rs. 130.0
Refund amount: Rs. 390.

1. Passenger details: Reads the name, age, and travel distance.
2. Travel class: Selects Sleeper, 3AC, or 2AC, each with a different rate and reservation fee.
3. Distance slabs: Adds a fixed charge based on the distance travelled.
4. Age concession: Children below 5 have zero fare in this simplified model; passengers aged 60 or above receive a 20% concession.

