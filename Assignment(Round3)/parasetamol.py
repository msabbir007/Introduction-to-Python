# Johdatus ohjelmointiin
# Parasetamol

def calculate_dose(w,t,d):

    if t<6:
        return 0
    else:
        if d < 4000:
            weight_dose = w * 15
            if weight_dose <= (4000- d):
                return weight_dose
            else:
                possible_dose = (4000 - d)
                return possible_dose
        else:
            print("it not possible to give medicine")







def main():

   a=int(input("Patient's weight (kg): "))
   b=int(input("How much time has passed from the previous dose (full hours): "))
   c=int(input("The total dose for the last 24 hours (mg): "))
   print("The amount of Parasetamol to give to the patient:",calculate_dose(a,b,c))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

main()
