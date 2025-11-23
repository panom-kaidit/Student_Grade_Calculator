#!/usr/bin/env python3
import csv
#I am using arrays so simplicity
FA_list=[]
SA_list=[]
FA_Categ=[]
FA_assName=[]
FA_weight=[]
SA_weight=[]
Ovarall_category=[]
Overall_assign=[]
Overall_weight=[]
overall_grades=[]
FA_weight_count=0
SA_weight_count=0
weight_count=0 
# List containing dictionary of assignment details
Transcript_details=[]
class Validation:
    def __init__(self, input):
        self.input = input
    def check_if_empty(self):
        if not self.input.strip():
            print("-------------------------------------------")
            print("\n***************** Error! ******************\nInput can not be empty. Please try again.\n")
            print("-------------------------------------------")
            return True
        return False
    
    def range_validation(self):
        try:
            value = int(self.input)
            if  value not in range(0,101):
                print("--------------------------------------\n")
                print('**************** Error! ****************\n       Not in in range      ')
                print("\n--------------------------------------")
                return True
            return False
        except ValueError:
            print("--------------------------------------\n")
            print("------------ Invalid Input -------------")
            print("\n--------------------------------------")
            return True
    def csv_preparation(self):
        csv_file='grades.csv'
        Grade_Transcript=[]
        for g in range(len(Overall_assign)):
            grade= overall_grades[g]
            subject= Overall_assign[g]
            weight= Overall_weight[g]
            category= Ovarall_category[g]
            Grade_Transcript.append({"Assignment": subject,
                                    "Category": category,
                                     "Grades": grade,
                                     "Weight": weight})
        Ass_names = ["Assignment","Category", "Grades", "Weight"]
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Ass_names)
            writer.writeheader()
            writer.writerows(Grade_Transcript)
        print("--------------------------------------\n")
        print(f"    Data successfully saved to {csv_file}")
        print("\n--------------------------------------")
    def resubmissions(self):
        Failed_subjects=[]
        for g in range(len(FA_assName)):
            grade= FA_list[g]
            subject= FA_assName[g]
            weight= FA_weight[g]
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
            print("\n--------------------------------------\n")
            print("************ Error!*********************\n       Missing assignment!     ")
            print("\n--------------------------------------")
            return
        if FA_Pass_Mark >= 50 and SA_Pass_Mark >= 50:
            Status= "Pass"
        else:
            Status= "Fail"
        message = "-------------------------------------------------"
        message = "\n   --------RESULTS---------\n"
        message += f"   Total Formative: {Total_FA}/{Total_FA_Weight}\n"
        message += f"   Total Summative: {Total_SA}/{Total_SA_Weight}\n"
        message += "    -------------------------\n"
        message +=  f"  Total Grade:     {(Total_grades/Total_Weight)*100}/100\n"
        message += f"   GPA:             {((Total_grades/Total_Weight)*5.0):.2f}\n"
        message += f"   Status:          {Status}\n"
        resub = Final_message.resubmissions()
        if resub:
            message += f"   Resubmission:    {resub}\n"
        else:
            message += "    Resubmission:    None\n"
        message += "-------------------------------------------------\n"
        print (message)
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

def welcome_message():
    print("""
===========================================
WELCOME TO THE STUDENT GRADE CALCULATOR
===========================================
Please follow the instructions provided'
""")
while True:
    welcome_message()
    name = input("Enter the assignment name: ")
    AssiName= Validation(name)
    if AssiName.check_if_empty():
        continue

    while True:
        category = input('Enter Category ("FA" for Formative, "SA" for Summative): ')
        AssiCategory=Validation(category)
        if category.lower() == "fa" and FA_weight_count == 60:
            print("--------------------------------------\n")
            print("All Formative assignments have already been added.\n Please choose a different category.")
            print("--------------------------------------")
            continue
        if category.lower() =="sa" and SA_weight_count == 40:
            print("\n--------------------------------------\n")
            print("All Summative assignments have already been added.\n Please choose a different category.")
            print("\n--------------------------------------")
            continue
        if AssiCategory.check_if_empty():
            print(AssiCategory.check_if_empty())
            continue
        if not AssiCategory.category_validation():
            print("--------------------------------------\n")
            print('************ Invalid input **************\n Please enter FA for Formative or "SA" for summartive.\n')
            print("--------------------------------------")
            continue
        category = AssiCategory.category_validation()
        Ovarall_category.append(category)
        Overall_assign.append(name)
        break

    while True:
        grades = input("Enter grades obtained(0-100): ")
        GradesValidation = Validation(grades)
        if grades.isalpha():
            print("--------------------------------------\n")
            print(" wrong Input. Please try a number.")
            print("\n--------------------------------------")
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
            print("--------------------------------------\n")
            print(" wrong Input. Please try again.")
            print("\n--------------------------------------")
            continue
        if valid_weight.check_if_empty():
            continue
        weight=int(weight)
        if weight_count + weight > 100 and weight_count <= 100:
            print("--------------------------------------\n")
            print("************ Error! ****************")
            print("Total weight cannot exceed 100!")
            print(f"Current FA total:  {FA_weight_count}\nCurent SA: {SA_weight_count}")
            print(f"Current total:     {weight_count}\nCurrent + This :", weight_count + weight)
            print(f"Remaining Weight:  {(100-weight_count)}")
            print("\n--------------------------------------")
            continue
        if category == "FA" or category == "SA":
            if category == "FA":
                if FA_weight_count == 60:
                    print("--------------------------------------\n")
                    print("You have successfully added all Formative assignments.\n")
                    print("--------------------------------------\n")
                if FA_weight_count + weight <= 60:
                    print("--------------------------------------\n")
                    print("Assignment successfully added.")
                    print(f"Total FA weight: {FA_weight_count + weight}")
                    print(f"Remaining FA weight: {60 - (FA_weight_count + weight)}\n")
                    print("--------------------------------------")
                    FA_weight_count += weight
                    FA_assName.append(name)
                    FA_weight.append(weight)
                    Overall_weight.append(weight)
                elif FA_weight_count + weight > 60:
                    print("--------------------------------------\n")
                    print("Error: Total FA weight cannot exceed 60%.")
                    print(f"Current Total (FA): {FA_weight_count + weight}")
                    print(f"Excess Weight Added: {(FA_weight_count + weight) - 60}")
                    print(f"Remaining FA weight: {60 - FA_weight_count}")
                    print("Please ensure the total FA weight adds up to 60%.\n")
                    print("--------------------------------------")
                    continue
            if category == "SA":
                if SA_weight_count == 40:
                    print("You have successfully added all Summative assignments.\n")
                if SA_weight_count + weight <= 40:
                    print("--------------------------------------\n")
                    print("Assignment successfully added.")
                    print(f"Total SA weight:        {SA_weight_count + weight}")
                    print(f"Remaining SA weight:    {40 - (SA_weight_count + weight)}\n")
                    print("--------------------------------------")
                    SA_weight_count += weight
                    Overall_weight.append(weight)
                elif SA_weight_count + weight > 40:
                    print("----------------------------------------------\n")
                    print("Error: Total SA weight cannot exceed 40%.")
                    print(f"Current Total (SA): {SA_weight_count + weight}")
                    print(f"Excess Weight Added: {(SA_weight_count + weight) - 40}")
                    print(f"Remaining SA weight: {40 - SA_weight_count}")
                    print("Please ensure the total SA weight adds up to 40%.\n")
                    print("------------------------------------------------")
                    continue

            print(f"""
-------------------------------------------------------------------------
                            RESULTS
--------------------------------------------------------------------------
| {'ASSIGNMENT':<15} | {'CATEGORY':<10} | {'GRADES':<10} | {'WEIGHT':<8} |
--------------------------------------------------------------------------
| {name:<15} | {category:<10} | {grades:<10} | {weight:<8} |
--------------------------------------------------------------------------
""")
            print("\n--------------------------------------------------------------")
            print("Assignment added successfully. All details have been recorded.")
            print("\n--------------------------------------------------------------")
            break
    grade = Logic(grades, weight, category)
    grade.weightedGrade()

    if FA_weight_count == 60 and SA_weight_count == 40:
        break

    while True:
        choice = input("Do you want to add another assignment? (y/n) or (E) to Exit: ").strip().lower()
        if choice == "y":
            break
        elif choice =="e":
            exit()
        elif choice == "n":
            if not FA_list or not SA_list:
                if not FA_list:
                    print("--------------------------------------\n")
                    print("Formative assignments cannot be empty.")
                    print(f"Remaining FA weight: {60 - FA_weight_count}%\n")
                    print("--------------------------------------")
                    continue
                if not SA_list:
                    print("--------------------------------------\n")
                    print("Summative assignments cannot be empty.")
                    print(f"Remaining SA weight: {40 - SA_weight_count}%\n")
                    print("--------------------------------------")
                    continue
            if SA_weight_count != 40 or FA_weight_count != 60:
                if FA_weight_count < 60:
                    print("--------------------------------------\n")
                    print("Formative weight must total 60%.")
                    print(f"Current FA weight: {FA_weight_count}")
                    print(f"Remaining FA weight: {60 - FA_weight_count}\n")
                    print("--------------------------------------")
                    continue
                if SA_weight_count < 40:
                    print("--------------------------------------\n")
                    print("Summative weight must total 40%.")
                    print(f"Current SA weight: {SA_weight_count}")
                    print(f"Remaining SA weight: {40 - SA_weight_count}\n")
                    print("Please be sure to add Summative assignments.")
                    print("\n--------------------------------------")
                    continue
            
            break

        else:
            print("--------------------------------------\n")
            print("Invalid input. Please enter 'y' or 'n'.\n")
            print("--------------------------------------")
            continue

Final_message=Validation("")
Final_message.GPA_generator()
#Saving them to csv file
Final_message.csv_preparation()