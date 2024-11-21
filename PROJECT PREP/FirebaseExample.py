import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("lc-sandbox-c942a-firebase-adminsdk-mkl9j-f991d41c76.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://lc-sandbox-c942a-default-rtdb.europe-west1.firebasedatabase.app/'})

#databaseReference
ref = db.reference('/') # reference the root node of the database

mydataDictionary ={
    "Books":{
    "Book1":
    {
        "Title": "The Fellowship of the Ring",
        "Author": "J.R.R. Tolkien",
        "Genre": "Epic fantasy",
        "Price": 100
    },
    "Book2":
    {
        "Title": "The Two Towers",
        "Author": "J.R.R. Tolkien",
        "Genre": "Epic fantasy",
        "Price": 100    
    },
    "Book3":
    {
        "Title": "The Return of the King",
        "Author": "J.R.R. Tolkien",
        "Genre": "Epic fantasy",
        "Price": 100
    },
    "Book4":
    {
        "Title": "Brida",
        "Author": "Paulo Coelho",
        "Genre": "Fiction",
        "Price": 100
    }
}
}

ref.set(mydataDictionary) #set puts the data at the ref location(address at top). It deletes any other data at that location
# 
book4 = ref.child("Books").child("Book4").child("Title").get()#Child changes to a different branch of the data
book2 = ref.child('Books').child('Book3').child('Author').get()
print(book4)
print(book2) #get gets the data at the reference location
# 
ref = db.reference("/")
ref.child("Books").update({"Best Sellers4": [1,2,3,4,5,6,7]  })# update updates the data at a certain location or adds a new branch
# 
# ref.set({}) #Deletes all the data in a location