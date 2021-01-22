def are_valid_groups(listStudentNum, listOfGroups):
    students = 0
    for studentNum in listStudentNum:
        for group in listOfGroups:
            for memberStudentNum in group:
                if memberStudentNum == studentNum:
                    students = students + 1
    if students == len(listStudentNum):
        return True
    else:
        return False
                
                    
