from django.http import HttpResponse     # whenever request/responce came in Django we can able to use both hhtp-request and http-responce
from django.shortcuts import render  # to render the templates in the browser

# # // // Now, we've to create some methods or functions to handle the requests and send responses.
# # // // Whenever a request comes to the server, Django will look for the urls.py file to check which method has to be called for that particular request.

# # // Direct Method to handle the request and send the response, (without using templates)

# def home(request):   # whenever a request comes to home page this method will be called, and we've to return the home-method
#     return HttpResponse("This is Home Page of Chai Aur Django")   # this will send the response to the browser
# # In-case we want to create some other "Routes" or "Endpoints" in our project, we can create more methods like this.
def about(request):   
    return HttpResponse("This is About Page of Chai Aur Django")  
def contact(request):  # we can assign the name of the method whatever we want
    return HttpResponse("This is Cotact Page of Chai Aur Django")   



def home(request):   
    # return HttpResponse("This is Home Page of Chai Aur Django")   
    return render(request, 'website/index.html')   # this will render the index.html file in the browser
