import os   
    
cwd = os.getcwd()
print(cwd)   

file_path = '/home/nick/project/devops/python/test_2.txt'


message = 'yo dude sup sup'


# with open(file_path, 'w') as file_path:
#     file_path.write(message)



# 


# try:
    
#     with open(file_path, 'w') as file_path:
            
#         file_path.write(message)

# except Exception as exception_object:
#     print("Unexpected exception", exception_object)

try:
    
    with open(file_path, 'r') as file_path:
        x = file_path.read()
        print(x)

except Exception as exception_object:
    print("Unexpected exception", exception_object)