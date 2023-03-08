def greet_family(name="John", surname="Doe"):
    print(f"Hello {name} {surname}!")

# Greet John first
greet_family()

# Create a list of family members
family_members = ["Tristram Mcbride", "Baldwin Preston", "Wally Collins"]

# Greet each family member using a for loop
for member in family_members:
    # Split the member's name into first and last name
    first_name, last_name = member.split(" ")
    # Call the greet_family function with the member's first and last name
    greet_family(first_name, last_name)