# PASSWORD STRENGTH DEMO


# Determine Ticket Function
def checkPwdStrength(pwd):
    pwdLen = len(pwd)
    if pwdLen >= 13:
        return "Very Strong"
    elif pwdLen >= 9:
        return "Strong"
    elif pwdLen >= 5:
        return "Okay"
    else:
        return "Weak"


# Welcome
print("\nPASSWORD STRENGTH COMPARISON")
print("Compare the strength of two passwords...")

# Input
print("\nINPUT PASSWORDS:")
pwd1 = input("Enter first password: ")
pwd2 = input("Enter second password: ")

# Process
pwd1Str = checkPwdStrength(pwd1)
pwd2Str = checkPwdStrength(pwd2)

# Output
print("\nRESULTS:")
print(f"Password 1: {pwd1Str}.")
print(f"Password 2: {pwd2Str}.")
