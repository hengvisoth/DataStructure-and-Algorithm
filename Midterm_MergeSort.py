import facebook

likes = 0 # How many times they likes on your posts
friend = "Bob" # Your friends name

graph=facebook.GraphAPI(access_token="")
posts=graph.get_connections(id="me",connection_name="posts")
for w in range (0,5):
    p1=posts['data'][w]['likes']['data']
    for i in range (0,len(p1)):
      if friend == p1[i]['name']:
          likes += 1
print( likes )
