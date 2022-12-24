# Bank_data(Time taken : 23rd and 24th of december after my viva finished on 22nd.)
--> This is Django rest api for performing CRUD operations o data of certain banks and its branches.
--> Here i have also added some test cases under test.py file for testing response status code.
--> I have used sqllite3 in this project to store data.
--> Because i have deployed my website/web - application on heroku requirement.txt file include all the libraries required for this prroject.


-> Here first i have created 3 models(tables) as data demanded.then i have created serializer.py and made 'model_serialize' method for all 3 models and then in views.py   file i have created viewsets which later called by urlrouter in url.py file.


-> This project is working on main 3 tables 1.banks (name of banks)
                                            2.branches  (detail about branches of that banks)
                                            3.bank_branches (unnion of above both)
-> main url for seeing this project on browser is : ["https://bank-details.herokuapp.com/"] 
-> I have even attached all the data in form of csv files.


*NOTE* : I am not used to for writing readme files so if you have any query or doubt about my work please messege me i will love to solve your doubts.
