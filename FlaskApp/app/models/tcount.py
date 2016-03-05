'''
Tweets DB schema 
Json object example:
{
  "_id": ObjectId("56c8c1357e48b67d194d80c7"),
  "company": "Amazon",
  "count": 1000,
  "date": ISODate("2016-02-20T19:12:00Z")
}
'''

# These belongs to models. you should create a seperate folder for models.
# schema folder is just for any .sql file
class tcount():

  def __init__(self, company=None, count=None, score=None, date=None):
    self.company = company
    self.count = count
    self.score = score
    self.date = date

  def __repr__(self):
    return '<text %r %r %r %r>' % (self.company, self.count, self.score, self.date)

