# FastAPI-CRUD-Operation

### Install the required libraries 
pip install fastapi

pip install "uvicorn[standard]"

pip install typing

pip install pydantic

### After installing the libraries, run the following command to start the server.
uvicorn main:app --reload

The code has started, and the API's are running. 

![image](https://user-images.githubusercontent.com/64482329/193783775-a64d6c79-8b21-4aad-904d-c3e77c30e48a.png)

### For testing them, we can hit them using the brower or postman. 
URL for testing- 

http://127.0.0.1:8000/    (GET Method- base-url)
![image](https://user-images.githubusercontent.com/64482329/193786274-1659d75e-7e6b-4a53-83e1-939e5199ba57.png)

http://127.0.0.1:8000/app/v1/users/   (GET Method- Get list of all the Users)
![image](https://user-images.githubusercontent.com/64482329/193786377-5bd7abd7-63f7-465d-97a4-a08579c4bbf4.png)

http://127.0.0.1:8000/app/v1/users/   (POST Method- Add a user to the list of Users)
![image](https://user-images.githubusercontent.com/64482329/193786479-666e0940-5d02-45a5-a0d4-dc7220c668a2.png)

The new user has been added.

![image](https://user-images.githubusercontent.com/64482329/193786655-d990859c-0505-4ce3-b88c-398ddae9d806.png)

http://127.0.0.1:8000/app/v1/users/{id}   (PUT Method- Update the user details)
![image](https://user-images.githubusercontent.com/64482329/193786842-2acd32ce-99ee-4df3-ac1b-2b8194669d38.png)

The roles have been updated.

![image](https://user-images.githubusercontent.com/64482329/193786967-bda1e27c-e80a-4f0a-ad09-f170052fe34f.png)

### If user with id does not exist, then an exception will be thrown
![image](https://user-images.githubusercontent.com/64482329/193787464-9af3e831-99cb-4c51-bba7-a7fd8ab997aa.png)

http://127.0.0.1:8000/app/v1/users/{id}   (DELETE Method- Delete the user from the list)
![image](https://user-images.githubusercontent.com/64482329/193788561-eb2761de-f51e-48e6-8284-7759823a623c.png)

### If user with id does not exist, then an exception will be thrown
![image](https://user-images.githubusercontent.com/64482329/193788696-e1d500ff-3136-4e74-bff5-84957bed16ef.png)





