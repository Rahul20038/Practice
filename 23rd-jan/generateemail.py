def generate_mailId(firstname, lastname, domain):
    email = f'{firstname.lower()}.{lastname.lower()}@{domain}'
    return email
firstname = "Nallamothu"
lastname = "Rahul"
domain = "csk.in"
email = generate_mailId(firstname, lastname, domain)
print("Generated_Email_Id:", email)