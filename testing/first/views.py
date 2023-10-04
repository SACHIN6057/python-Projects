from django.shortcuts import get_object_or_404
from turtle import home
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from .models import UserData,PostData
from .forms import UserForm,PostForm
import sqlite3


# Create your views here.


def Index(request):
  
    return render(request,'home.html')



def delete1(request,post_id):
    post = get_object_or_404(PostData, id=post_id)
    post.delete()
    data_from_database = PostData.objects.all()       
    return render(request,'content.html',{'data': data_from_database})    



def login(request):
    
    if request.method == 'POST':
        Username=request.POST['UserName']
        Password=request.POST['Password']
        
        conn = sqlite3.connect('db.sqlite3')  # Replace 'your_database_name.db' with your SQLite database file name
        cursor = conn.cursor()

        # SQLite query to retrieve user data based on the provided username
        cursor.execute("SELECT * FROM first_userdata WHERE UserName=?", ( Username,))

        user_data = cursor.fetchone()
        print(user_data)
        if user_data and user_data[5] == Password:  # Assuming the password is stored in the fifth column
            response = HttpResponse("Login successful")
         # Cookie expires in 1 hour (3600 seconds)
            response.set_cookie('username', Username)
            
            response = redirect('/content')
            response.set_cookie('username', Username)
        
            
            
            cursor.close()
            conn.close()
             
            return response
        else:
            print("wrong")
            cursor.close()
            conn.close() 
            return render(request,'login.html')
        
        # user = auth.authenticate(username=Username, password=Password)
        # print(Username)
        # print(Password)
        # print(user)         
        # if user is not None:
        #     auth.login(request, user)
        #     return render(request,'content.html')
        # # Authentication successful, redirect to a success page or perform other actions
        # else:
        #     return render(request,'home.html')
        # # Authentication failed, show an error message or redirect back to the login page
            
    return render(request,'login.html')        
        
    #     conn = sqlite3.connect('..\db.sqlite3')  # Replace 'your_database.db' with the path to your SQLite database file
    #     cursor = conn.cursor()

    # # Execute the SQL query to check if the username and password exist
    #     cursor.execute("SELECT * FROM first_userdata WHERE Username = ? AND Password = ?", (Username, Password))

    # # Fetch the result
    #     result = cursor.fetchone()

    # # Close the database connection
    #     conn.close()

    # # If result is not None, username and password exist in the database
    #     if result:
    #         return render(request,content.html)
          
    return render(request,'login.html')









def content(request):
     data_from_database = PostData.objects.all()
     username = request.COOKIES.get('username', 'Default Username')
     print(username)       
     return render(request,'content.html',{'data': data_from_database,'username': username})



def create(request):
    if request.method=='POST':
        abc=PostForm(request.POST)
        if abc.is_valid():
            print(abc)
            form_instance = abc.save(commit=False)  # Create an instance of the model but don't save it to the database yet
            # You can perform additional processing on the form instance here if needed
            # form_instance.some_field = some_value
            form_instance.save()  # Save the form data to the database
           
            
            return redirect('/content')
        return render(request,'create.html')
    else:
        return render(request,'create.html')

    


def delete(request):
    response = HttpResponse("Logout successful")   
    response.delete_cookie('username')     
    response = redirect('/home')
    return response




def signup(request):
    if request.method=='POST': 
           abc=UserForm(request.POST)
           if abc.is_valid():
                form_instance = abc.save(commit=False)  # Create an instance of the model but don't save it to the database yet
            # You can perform additional processing on the form instance here if needed
            # form_instance.some_field = some_value
                form_instance.save()  # Save the form data to the database
                return redirect('/login')
            # Redirect to a success page or render a success template
            # ...
    else:
        return render(request, 'signup.html')

    return render(request, 'signup.html')
        
    
