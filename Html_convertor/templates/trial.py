import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='fe_image',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO 
                          (id, name, image) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(image)
        '''file = convertToBinaryData(biodataFile)'''

        # Convert data into tuple format
        insert_blob_tuple = (id, name, image)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric","C:\xampp\htdocs\FE-ImageData\img")
