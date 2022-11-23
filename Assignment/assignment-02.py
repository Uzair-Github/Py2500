maths = int(input("Enter maths numbers:"))
english = int(input("Enter english numbers:"))
urdu = int(input("Enter urdu numbers:"))
science = int(input("Enter science numbers:"))
social_studies = int(input("Enter social studies numbers:"))

total_numbers = int(input("Enter total numbers per single subject"))

sum = maths+english+urdu+science+social_studies
percentage = sum/(total_numbers*5)*100

print("Your percentage is:",percentage)

if percentage >= 80:
    print ("Grade A")
elif percentage > 50 and percentage < 80:
    print("Grade B")
else:
    print("Grade C")
