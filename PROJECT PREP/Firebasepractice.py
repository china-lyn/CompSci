import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("lc-sandbox-c942a-firebase-adminsdk-mkl9j-222ca58f51.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://lc-sandbox-c942a-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference('/') # reference to database

with open('Firebase practice file - Python.csv', 'r') as f:
    movies = {}
    title, numcritic, dur, dlikes, act3likes, act1likes, gross, numvote, castlikes, nuserreview, budget, year, imdb = f.readline().strip().split(',')
    row = 0
    
    for line in f:
        row += 1
        l = line.strip().split(',')
        movie = {
            title: l[0],
            numcritic: l[1],
            dur: l[2],
            dlikes: l[3],
            act3likes: l[4],
            act1likes: l[5],
            gross: l[6],
            numvote: l[7],
            castlikes: l[8],
            nuserreview: l[9],
            budget: l[10],
            year: l[11],
            imdb: l[12]
        }
        movies[f'Movie {row}'] = movie
print(movies)
            
            
ref.set(movies) # sets movie dictionary in database

movie1 = ref.child('Movie 1').child(title).get()
print(movie1)
    
        
    