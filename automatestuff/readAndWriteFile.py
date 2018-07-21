import os

os.path.join('usr', 'bin', 'spam')
print(os.getcwd())
print(os.path.join('usr', 'bin', 'spam'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join("E:\\Python_Documents", filename))

# os.makedirs('E:\\Python_Documents\\work')
print(os.listdir("E:\\Python_Documents"))

pythonFile = open("E:\\Python_Documents\\readFile.txt")
pythonFileContent = pythonFile.read()
print(pythonFileContent)
writePythonFiles = open("E:\\Python_Documents\\read.txt", "w")
writePythonFiles.write("Hello World")
writePythonFiles.close()
writePythonFiles = open("E:\\Python_Documents\\read.txt")
content = writePythonFiles.read()
writePythonFiles.close()
print(content)