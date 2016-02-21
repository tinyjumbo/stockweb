'''
Tweets DB schema 
Json object example:
{
  "_id": ObjectId("56c2192c1117f91a648bc165"),
  "text": "Make money while you sleep with AUTOMATIC ",
  "hashtages": [
    {
      "indices": [
        72,
        82
      ],
      "text": "SeoExpert"
    }
  ],
  "time": "2016-02-15 13:30:04.184332"
}
'''

# These belongs to models. you should create a seperate folder for models.
# schema folder is just for any .sql file
class Tweets_sche():

    def __init__(self, creation_time, text, hashtages):
        self.creation_time = creation_time
        self.text = text
        self.hashtages = hashtages

    def __repr__(self):
        return '<text %r>' % (self.text)

