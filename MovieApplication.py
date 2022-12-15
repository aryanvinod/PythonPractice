class Movie:
    '''Sample Movie class developed by Vinod'''
    def __init__(self,name,hero,heroine,showtime):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.showtime=showtime
    
    def info(self):
        print('Movie name:',self.name)
        print('Hero name:',self.hero)
        print('Heroine name:',self.heroine)
        print('Show Time:',self.showtime)

    
list_of_movies=[]
while True:
    print("*****Welcome to the Movie Hub*****")
    name=input("Enter Movie Name:")
    hero=input("Enter Hero Name:")
    heroine=input("Enter Heroine Name:")
    showtime=eval(input("Enter Show Time:"))
    m=Movie(name,hero,heroine,showtime)
    list_of_movies.append(m)
    print("Movie details added Successfully...")
    option=input("Do you want to add more movies in the watchlist:[Yes/No]")
    if option.lower()=='no':
        break

print("Please find all Movies details")
print("#*"*20)
for movie in list_of_movies:
    movie.info()
    print()





