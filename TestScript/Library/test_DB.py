import  Library.DBConnect

# def test_insert_DB():
#     str_query = "Insert into Employees (FirstName, LastName, Age, Address ) Values('a1', 'b1', 11, 'c1')"
#     class_a = Library.DBConnect.query_update(str_query)

# def test_update_DB():
#     str_query = "Update Employees Set FirstName= 'Mai', LastName='Tai' Where Age = 30"
#     class_a = Library.DBConnect.query_update(str_query)

def test_update_DB():
    str_query = "Update Employees Set FirstName= 'hoa', LastName='sen' Where Age = 30"
    class_a = Library.DBConnect.exe_sql_query(str_query)