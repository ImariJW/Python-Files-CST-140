#Prompt the user for classification.
SENIOR = 'senior'
JUNIOR = 'junior'
SOPHOMORE = 'sophomore'
FRESHMAN = 'freshman'
Y = 'yes'
N = 'no'
cLass = input("What is your classification?: ")
#Ask questions based on their classification (Control if) & #Display to user.
if cLass == SENIOR or cLass == JUNIOR:
    postGrad = input("Are you attending post-graduate school?: ")
    if postGrad == Y:
        print("You are a", cLass, "and you have plans on going to grad school!")
    elif postGrad == N:
        ynWork = input("Are you going to work?: ")
        if ynWork == Y:
            print("You are a", cLass, "and you have plans on going to work!")
        elif ynWork == N:
            otherP = input("Do you have other plans?: ")
            if otherP == Y:
                answerP = input("What are they?: ")
                print("You are a", cLass, "and you plan to", answerP , "!")
            elif otherP == N:
                print("You are a", cLass, "and you have no plans.")
            else:
                print("INVALID ENTRY")
        else:
            print("INVALID ENTRY")
    else:
        print("INVALID ENTRY")
elif cLass == SOPHOMORE or cLass == FRESHMAN:
    major = input("What is your major?: ")
    college = input("What college do you attend?: ")
    print("You are a", cLass, "and you are a(n)", major, "major attending", college + "!")
else:
    print("INVALID ENTRY")
