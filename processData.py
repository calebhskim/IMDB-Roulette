import MySQLdb as mdb
import sys
import re

def main():
    """
    reads all data from file into database
    """

#    try:
#        with open("/data/db_info.txt") as f:
#            host = f.readline().split()[1]
#            user = f.readline().split()[1]
#            passw = f.readline().split()[1]
#            db = f.readline().split()[1]
#        con = mdb.connect(host, user, passw, db)
#
#    except mdb.Error, e:
#        
#        print("Error %d: %s" % (e.args[0],e.args[1])
#        sys.exit(1)

    readfile("./data/ratings.list")

def readfile(filename):

    with open(filename) as f:
        f.readline() #consume first line (describes data)
        for line in f:
            data = line.split()

            dist = data[0]
            votes = int(data[1])
            rating = float(data[2])
            metadata = " ".join(data[3:])

            open_paren = metadata.find("(")
            close_paren = metadata.find(")", open_paren)
            title = metadata[:open_paren-1]

#            print(metadata)
#            print(str(open_paren))
            year_indices = re.search("\(([1-2]\d\d\d)|(\?\?\?\?)", metadata)
#            print(year_indices.groups())
            try:
                year = int(metadata[year_indices.start()+1:year_indices.end()])
            except :
                year = 0000
            desc = metadata[year_indices.end()+1:]
            
            cur = Rating(dist, votes, rating, title, year, desc)
            print(cur)


class Rating:    
    def __init__(self, dis="**********", v=0, r=0.0, t="", y=0, des=""):
        self.dist = dis
        self.votes = v
        self.rating = r
        self.title = t
        self.year = y
        self.desc = des

    def __str__(self):
        return ("Dist: " + self.dist + "\nVotes: " + str(self.votes) + 
            "\nRating: " + str(self.rating) + "\nTitle: " + str(self.title) +
            "\nYear: " + str(self.year) + "\nDesc: " + str(self.desc) + "\n")

 
if __name__ == "__main__":
    main()
