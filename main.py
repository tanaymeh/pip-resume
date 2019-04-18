from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Token, style_from_dict, Separator
import sys
import pyfiglet

result = pyfiglet.figlet_format("Tanay\nMehta", font = "isometric1" ) 
print(result) 

skills_output = "\n1.Javascript - Intermediate\n2.Python - Intermediate\n3.C# - Intermediate\n4.C & C++ - Rookie\n----------Frameworks----------\n-----Python-----\n1.Tensorflow - Intermediate\n2.SciPy Libraries (Numpy, Pandas, Matplotlib, Sklearn, Keras etc..) - Intermediate\n3.PyInquirer - Intermediate\n-----Javascript-----\n1.ReactJS - Advanced\n2.NodeJS - Advanced\n3.THREE.js (WebGL Based 3D Graphics Library) - Advanced\n4.Express - Intermediate\n5.MongoDB - Intermediate\n----------More Coming in the Next Commit----------"
education_output = "\n1.Bachelor of Technology - JECRC University, Jaipur, Rajasthan (India) (2018-2022)\n2.High School (11th and 12th Grade) - Springdales Childrens School, Kota, Rajasthan (India)\n3. Junior High School - Emmanuel Mission School, Bundi, Rajasthan (India)"
certifications_output = "\n1.Making Interactive Prototypes using Javascript (July, 2018) - MicrosoftX (edX)\n2.Microsoft Technology Associate in Cloud Fundamentals - Microsoft\n----------More Coming Soon----------"
experience_output = "\n1.Physics Content Writer at TheGoPhysics - June 2018, April 2019\n"


def index_loop():
    index_prompt = {
        'type':'list',
        'name':'index',
        'message':'Please choose one of the above to know more:',
        'choices': [
            'Skills', 
            'Education', 
            'Certifications', 
            'Experience',
            Separator(),
            'Exit'
        ]
    }
    answers = prompt(index_prompt)
    return answers['index']


def main():
    print("\nWelcome to Tanay's Resume, What would you like to know about him?\n")
    call_check()


def call_check():
    index = index_loop()
    if (index == "Skills"):
        print(skills_output)
        print("\nMy Github Repository: https://github.com/heytanay\nMy LinkedIn Profile: https://www.linkedin.com/in/tanay-mehta-8337b3150/")
    elif (index == "Education"):
        print(education_output)
        print("\nMy Github Repository: https://github.com/heytanay\nMy LinkedIn Profile: https://www.linkedin.com/in/tanay-mehta-8337b3150/")
    elif (index == "Certifications"):
        print(certifications_output)
        print("\nMy Github Repository: https://github.com/heytanay\nMy LinkedIn Profile: https://www.linkedin.com/in/tanay-mehta-8337b3150/")
    elif (index == 'Experience'):
        print(experience_output)
        print("\nMy Github Repository: https://github.com/heytanay\nMy LinkedIn Profile: https://www.linkedin.com/in/tanay-mehta-8337b3150/")
    elif (index == 'Exit'):
        print("\nOk Bye!\n")
        print("\nMy Github Repository: https://github.com/heytanay\nMy LinkedIn Profile: https://www.linkedin.com/in/tanay-mehta-8337b3150/")
        sys.exit()

    call_check()

main()
