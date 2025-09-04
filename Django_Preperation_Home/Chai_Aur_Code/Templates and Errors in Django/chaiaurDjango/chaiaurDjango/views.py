from django.http import HttpResponse     # whenever request/responce came in Django we can able to use both hhtp-request and http-responce


# Now, we've to create some methods or functions to handle the requests and send responses.

def home(request):   # whenever a request comes to home page this method will be called, and we've to return the home-method
    return HttpResponse("This is Home Page of Chai Aur Django")   # this will send the response to the browser

# In-case we want to create some other "Routes" or "Endpoints" in our project, we can create more methods like this.
def about(request):   
    return HttpResponse("This is About Page of Chai Aur Django")  

def contact(request):  # we can assign the name of the method whatever we want
    return HttpResponse("This is Cotact Page of Chai Aur Django")   