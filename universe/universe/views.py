from django.http import HttpResponse
import os


def homePageView(request):
    # with open (os.getcwd() + '/universels/temp.txt') as spam:
    #     eggs = spam.read()    
    
    
    return HttpResponse("<h1>yo yo yo</h1>")


# with open (os.getcwd() + '/universe/uni/temp.txt') as spam:
#         eggs = spam.read()
#         a = eggs

# print(eggs)