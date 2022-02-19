# Assignment 07
# c0829441 – Stuart Daniells
# Question 11
# Date of submission: 2021-12-06

if __name__ == '__main__':
    
    # creating a new html file to add web contents
    webpage = open("webpage.html", 'w')
    
    # Prompting user input
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    
    # Adding the html tags along with user input
    htmlPage1 = "<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>"+name+"</h1>\n"
    webpage.write(htmlPage1)
    
    htmlPage2 = "\t</center>\n\t<hr />\n\t"+description+"\n\t<hr />\n</body>\n</html>"
    webpage.write(htmlPage2)
    
    # closing the file
    webpage.close()
    
    
    
