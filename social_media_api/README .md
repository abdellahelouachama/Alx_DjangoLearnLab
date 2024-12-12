    socail medai API
### Athentication system : 
## Register :
RegisterView: is a view that handle new user creation with POST method

It takes username and password, email as a required fields

first name, last name, profile picture, and bio as an opetionl fields

if required fields are provided and valid it return seccuss message with this http code status "HTTP_201_CREATED"

else it returns a message indicating an error with this code status "HTTP_400_BAD_REQUEST"

Url Path : POST/user/register/

## Login:
LoginView: is a view that handle login operation through validationg credentials with POST method

It takes username and password:

if they are valid it generates new token and return a response that contains seccuss message with the token and this http code status"HTTP_200_OK"

if they are not valid it return a message indicating that credentials are not valid with this http code status "HTTP_400_BAD_REQUEST"

Url Path: POST/user/login/

## Logout:
LogoutView: is a view that handle logout operation through destroying the token with POST method

It required the user to be authenticated

It takes the token and delete it

if deleted successfuly it return a message indicating seccussful logout and this http code status "HTTP_200_OK"

else it return an error with this message "Token does not exist." and this http code status "HTTP_400_BAD_REQUEST"

Url Path: POST/user/logout/  

### User Profile Management : 
UserAPIView : is a viewset that handle user profile management through handling reteriving updating and deleting user  
Note: user creation is handled in RegisterView as a part of the authentication system  

Reterive user: this operation handle user reteriving with usename as a lookup field accessing this action required authentication and the authenticated user been the obj he wants to reterive (you can't access others profile)  

Update user: this operation handle user updation with username as a lookup field and required all the fields to be provided accessing this action required authentication and the authenticated user been the obj he wants to update (you can't update others profile)  

Partial Update: this operation handle user updating with username as a lookup field and it doesn't required all fields the provided fields will be update and the others keep them with thier previous values accessing this action required authentication and the authenticated user been the obj he wants to update (you can't update others profile)  

Delete user : this operation handle use deletion with username as a lookup field accessing this action required authentication and the authenticated user been the obj he wants to delete (you can't delete others accounts)  
