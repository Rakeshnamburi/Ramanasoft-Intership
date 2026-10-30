# Assignment 2: Social Media Analytics - Hashtag Trending System  


# Sample Input:  
posts = [  
"Just finished my work out!          #fitness    #gym    #motivation         #healthy",  
"Beautiful sunset today              #nature     #photography    #sunset     #peaceful",  
"New recipe tried today              #cooking   #food          #healthy           #delicious",  
"Weekend vibes                       #weekend   #relaxation      #peaceful    #family",  
"Morning jog completed               #fitness   #running       #motivation    #morning",  
"Family dinner was amazing            #family    #food         #weekend       #love"  
] 


# 1. Extract all unique hashtags from posts 

hashtags_set = set()
for post in posts:
    words = post.split()
    for word in words:
        if word.startswith("#"):
            hashtags_set.add(word)
            print(f"Extracted Hashtag: {word}")

# ekkada hasjtag ne find out cheyamanaru so manam hashtags_set lo add chesamu. 
# Ikkada manam unique hashtags ni extract chesamu.
# words ekkada nuchi start itundhi "#' tho a words print avali


# 2. Find hashtags that appear in multiple posts (trending hashtags)

hashtag_count = {}
for post in posts:
    words = post.split()
    unique_hashtags_in_post = set()
    for word in words:
        if word.startswith("#"):
            unique_hashtags_in_post.add(word)
    for hashtag in unique_hashtags_in_post:
        if hashtag in hashtag_count:
            hashtag_count[hashtag] += 1
        else:
            hashtag_count[hashtag] = 1
            print(f"Hashtag Count Updated: {hashtag} appears in {hashtag_count[hashtag]} posts")


# 3. Identify hashtags that are unique to specific posts  

unique_hashtags_per_post = []
for post in posts:
    words = post.split()
    unique_hashtags_in_post = set()
    for word in words:
        if word.startswith("#"):
            unique_hashtags_in_post.add(word)
    unique_hashtags_per_post.append(unique_hashtags_in_post)

    print(f"Unique Hashtags in Post: {unique_hashtags_in_post}")


    # 4. Count hashtag frequency and find top trending tags

    for hashtag, count in hashtag_count.items():
        print(f"Hashtag: {hashtag}, Frequency: {count}")    
        print("Top Trending Hashtags:")
        