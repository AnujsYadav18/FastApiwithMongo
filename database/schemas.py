def get_particular_data(Employee):
    return{
        "id":str(Employee["_id"]),
        "Name":Employee["emp_name"],
        "Position":Employee["emp_designation"],
        "PayScale":Employee["emp_salary"]
    }

def get_all_data(Employees):
    return[get_particular_data(Employee) for Employee in Employees]