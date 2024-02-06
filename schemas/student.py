#schemas helps to serializer and also convert mongodb format to our ui needed json
def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item.get("student_name", "N/A"),
        "email": db_item.get("student_email", "N/A"),
        "phone": db_item.get("student_phone", "N/A"),
        "program": db_item.get("student_program","N/A"),
        "department":db_item.get("student_department","N/A")
    }


def listOfStudentEntity(db_item_list) -> list:
    list_stud_entity = []
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))

    return list_stud_entity   
