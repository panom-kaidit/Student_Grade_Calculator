#!/usr/bin/env python3
#I am using arrays so simplicity
FA_list=[]
SA_list=[]
FA_weight=[]
SA_weight=[]
Overall_assign=[]
Overall_weight=[]
overall_grades=[]
FA_weight_count=0
SA_weight_count=0
weight_count=0 

class Validation:
    def __init__(self, input):
        self.input = input
    def check_if_empty(self):
        if not self.input.strip():
            print("\n------------Error!-----------\nInput can not be empty. Please try again.\n")
            return True
        return False
    def range_validation(self):
        try:
            value = int(self.input)
            if  value not in range(0,101):
                print('------Error!------\n Not in in range ')
                return True
            return False
        except ValueError:
            print("Invalid Input")
            return True
    def resubmissions(self):
        Failed_subjects=[]
        for g in range(len(Overall_assign)):
            grade= overall_grades[g]
            subject= Overall_assign[g]
            weight= Overall_weight[g]
            if grade < 50:
                Failed_subjects.append(
                    {"Assignment": subject,
                    "Grades": grade,
                    "Weight": weight})
        
        resubmission_list=[]
        highest_weight=0
        for items in Failed_subjects:
            if items["Weight"] > highest_weight:
                highest_weight=items["Weight"]
        for items in Failed_subjects:
            if items["Weight"] == highest_weight:
                resubmission_list.append(items["Assignment"])

        return ",".join(resubmission_list)
    def GPA_generator(self):
        Total_FA=sum(FA_list)
        Total_SA=sum(SA_list)
        Total_FA_Weight=sum(FA_weight)
        Total_SA_Weight=sum(SA_weight)
        Total_Weight=Total_FA_Weight+Total_SA_Weight
        Total_grades= Total_FA+Total_SA
        FA_Pass_Mark= (Total_FA/Total_FA_Weight)*100
        SA_Pass_Mark= (Total_SA/Total_SA_Weight)*100
        Status=None
        if Total_FA_Weight == 0 or Total_SA_Weight == 0:
            print("Error: Missing assignment!")
            return
        if FA_Pass_Mark >= 50 and SA_Pass_Mark >= 50:
            Status= "Pass"
        else:
            Status= "Fail"

        message = "--------RESULTS---------\n"
        message += f"Total Formative: {Total_FA}/{Total_FA_Weight}\n"
        message += f"Total Summative: {Total_SA}/{Total_SA_Weight}\n"
        message += "-------------------------\n"
        message +=  f"Total Grade:    {(Total_grades/Total_Weight)*100}/100\n"
        message += f"GPA:             {((Total_grades/Total_Weight))*5.0}\n"
        message += f"Status:          {Status}\n"
        resub = Final_message.resubmissions()
        if resub:
            message += f"Resubmission:    {resub}\n"
        else:
            message += "Resubmission:    None\n"
        print (message)
        print(Overall_weight)
        print(Overall_assign)
        print(overall_grades)

    def category_validation(self):
        """This is a method tha
        """
        if self.input == "fa" or self.input== "FA" or self.input == "Fa":
            return "FA"
        if self.input == "SA" or self.input == "sa" or self.input == "Sa":
            return "SA"
        return False

class Logic:
    """" Logic is where the calculations take place. for the weighed grades"""
    def __init__(self,input,weight,category):
        self.input = input
        self.weight = weight
        self.category = category
    def weightedGrade(self):
        percentage = self.input/100
        weightedGrade = percentage*self.weight
        if self.category == "FA":
            FA_weight.append(self.weight)
            FA_list.append(weightedGrade)

        if self.category == "SA":
            SA_weight.append(self.weight)
            SA_list.append(weightedGrade)
        # # else:
        # return ('-----------Invalid input-----------\n Please enter FA" for Formative or "SA" for summartive.\n')

while True:
    name = input("Please Enter Assignment Name: ")
    AssiName= Validation(name)
    if AssiName.check_if_empty():
        continue
    while True:
        category =input('Enter Category \n("FA" for Formative, "SA" for Summative): ')
        AssiCategory=Validation(category)
        if category.lower() == "fa" and FA_weight_count == 60:
            print("You cannot add more Formatives. You have already added all the Formative assignments.")
            continue
        if category.lower() =="sa" and SA_weight_count == 40:
            print("You cannot add more Summatives. You have already added all the Summative assignments.")
            continue
        if AssiCategory.check_if_empty():
                print(AssiCategory.check_if_empty())
                continue
        if  not AssiCategory.category_validation():
            print('-----------Invalid input-----------\n Please enter FA for Formative or "SA" for summartive.\n')
            # print(AssiName.category_validation())
            continue
        category = AssiCategory.category_validation()
        Overall_assign.append(name)
        break

    while True:
        grades = input("Enter grades obtained(0-100): ")
        GradesValidation = Validation(grades)
        if grades.isalpha():
            print("wrong Input. Please try a number.")
            continue
        if GradesValidation.check_if_empty():
            continue
        if GradesValidation.range_validation():
            continue
        grades = int(grades)
        overall_grades.append(grades)
        break

    while True:
        weight = input("Enter the Assignment weight: ")
        valid_weight = Validation(weight)
        if weight.isalpha():
            print("wrong Input. Please try again.")
            continue
        if valid_weight.check_if_empty():
            continue
        weight=int(weight)
        if weight_count + weight > 100 and  weight_count <= 100:
            print("----------Error!-------------")
            print("Total weight cannot exceed 100!")
            print(f"Current FA total:  {FA_weight_count}\nCurent SA: {SA_weight_count}")
            print(f"Current total:     {weight_count}\nCurrent + This :", weight_count + weight)
            print(f"Remaining Weight:  {(100-weight_count)}")
            continue
        if category =="FA" or category =="SA":
            if category=="FA":
                if FA_weight_count ==60:
                    print("You have sucessfully added all Formatives")
                if FA_weight_count + weight <= 60:
                    print("Assignment successfully added.")
                    print(f"Total FA weight: {FA_weight_count + weight}\n")
                    print(f"Remaining FA weight: {60 - (FA_weight_count + weight)}\n")
                    FA_weight_count += weight
                    Overall_weight.append(weight)
                elif FA_weight_count + weight > 60:
                    print("Total FA weight can not exceed 60")
                    print(f"Your recent FA weight: {FA_weight_count + weight}\nAdded FA weight: {(FA_weight_count + weight)-60}")
                    print(f"Remaining Total FA weight: {60-FA_weight_count}")
                    print("Please make sure Total FA weight Add up to 60.\n")
                    continue
            if category=="SA":
                if SA_weight_count ==40:
                    print("You have sucessfully added all Summatives")
                if SA_weight_count + weight <= 40:
                    print("Assignment successfully added.")
                    print(f"Total SA weight: {SA_weight_count + weight}\n")
                    print(f"Remaining SA weight: {40 - (SA_weight_count + weight)}\n")
                    SA_weight_count += weight
                    Overall_weight.append(weight)
                elif SA_weight_count + weight > 40:
                    print("Total SA weight can not exceed 40")
                    print(f"Your recent SA weight: {SA_weight_count + weight}\nAdded SA weight: {(SA_weight_count + weight)-40}")
                    print(f"Remaining Total SA weight: {40-SA_weight_count}")
                    print("Please make sure Total SA weight Add up to 40.\n")
                    continue

        break
    grade=Logic(grades,weight,category)
    grade.weightedGrade()
    if FA_weight_count == 60 and SA_weight_count == 40:
        break
    while True:
        choice = input("Do you want to add another assignment?(y/n): ")
        if choice == "Y" or choice == "y":
            break
        elif choice == "N" or choice == "n":
            if not FA_list or not SA_list :
                if not FA_list:
                    print("Formative  can not be empty")
                    print(f"You have {60-FA_weight_count}% worth Of weight for FA(Formatives) Remaining.\n")
                    continue
                if not SA_list:
                    print("Summatives can not be empty")
                    print(f"You have {40-SA_weight_count}% worth Of weight for SA(Summatives)\n")
                    continue
            if SA_weight_count != 40 or FA_weight_count != 60:
                if FA_weight_count < 60:
                    print("Formative weight must add up to 60%")
                    print(f"Current fA: {FA_weight_count}\nRemaining FA weight: {60-FA_weight_count}")
                    continue
                if SA_weight_count < 40:
                    print("Summatives weight must add up to 40%")
                    print(f"Current SA: {SA_weight_count}\nRemaining SA weight: {40-SA_weight_count}\n")
                    print("Please make sure to add SUmmartive assignment.")
                    continue
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue

Final_message=Validation("None")
Final_message.GPA_generator()
