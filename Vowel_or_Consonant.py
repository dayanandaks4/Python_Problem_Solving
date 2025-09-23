# Take a character and check if it is a vowel or consonant.

# While used for Checking Continuously Checking number.

while True:
    def chracter(user):
        Vowel = ["a","e","i","o","u"]
        if user in Vowel:
            print("Vowel")
        else:
            print("Consonant")
    chracter(user=input("Enter the Character:").lower())
