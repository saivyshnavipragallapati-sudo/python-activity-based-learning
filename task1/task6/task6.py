
n = int(input("Enter number of passengers: "))
for i in range(n):
    print("\nPassenger", i + 1)
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

    fare = distance * rate + slab_charge
    if age < 5:
        fare = 0
        reservation = 0
    elif age >= 60:
        fare = fare * 0.8
    total = fare + reservation
    print("\n--- Ticket Details ---")
    print("Name:", name)
    print("Class:", class_name)
    print("Base fare:", round(fare, 2))
    print("Reservation fee:", reservation)
    print("Total fare: Rs.", round(total, 2))
    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty
        print("Cancellation penalty: Rs.", round(penalty, 2))
        print("Refund amount: Rs.", round(refund, 2))
    else:
        print("Reservation confirmed!")

