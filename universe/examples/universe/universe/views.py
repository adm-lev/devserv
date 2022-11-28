from django.http import HttpResponse
import os


def homePageView(request):
    # with open (os.getcwd() + '/universels/temp.txt') as spam:
    #     eggs = spam.read()    
    
    
    return HttpResponse("<h1>Home page!</h1>")

def testPageView(request):
    # with open (os.getcwd() + '/universels/temp.txt') as spam:
    #     eggs = spam.read()    
    
    
    return HttpResponse("<h1>Test page</h1>")


# with open (os.getcwd() + '/universe/uni/temp.txt') as spam:
#         eggs = spam.read()
#         a = eggs

# print(eggs)