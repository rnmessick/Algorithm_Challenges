users = [
  {
  "id": 1,
  "first_name": 'Johnny',
  "last_name": 'Rotten',
  "created_at":'2012-12-31 23:59:59',
  "updated_at":'2012-12-31 23:59:59'
  },
  {
  "id": 2,
  "first_name": 'Amy',
  "last_name": 'Brown',
  "created_at":'2012-12-31 23:59:59',
  "updated_at":'2012-12-31 23:59:59'
  },
  {
  "id": 3,
  "first_name": 'Alice',
  "last_name": 'Roh',
  "created_at":'2012-12-31 23:59:59',
  "updated_at":'2012-12-31 23:59:59'
  },

]


usersHaveBooks = [
  {
    'id':1,
    'user_id':1,
    'book_id':1,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':1,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':1,
    'book_id':3,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':1,
    'user_id':2,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },

]

books = [
  {
  'id': 1,
  'book_title': 'Grapes of Wrath',
  'book_subject': 'The hard life during the depression',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 2,
  'book_title': 'Metamorphosis',
  'book_subject': 'The degradation of humanity, reflected in a single man',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
  {
  'id': 3,
  'book_title': 'The Coming Plague',
  'book_subject': 'Infectious diseases',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
]

def innerJoin(user_list, book_list, usersbook_list):
  joinedArray = []
  temp = []
  for ubIndex in range(len(usersbook_list)):
    temp.append(usersbook_list)
    u = usersbook_list[ubIndex]["user_id"]
    b = usersbook_list[ubIndex]["book_id"]
    for userIdx in range(len(user_list)):
      if user_list[userIdx]["id"] == u:
        temp.append(user_list[userIdx])
    for booksIdx in range(len(book_list)):
      if book_list[booksIdx]["id"] == b:
        temp.append(book_list[booksIdx])
    joinedArray.append(temp)
    temp = []
    return joinedArray
joinedArray = innerJoin(users, books, usersHaveBooks)
print joinedArray

