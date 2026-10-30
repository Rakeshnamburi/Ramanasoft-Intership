# Assignment 4: Text Analytics for Customer Reviews  


# Sample Input: 


reviews = [  
"The product quality is excellent and delivery was fast. Highly recommend!",  
"Poor customer service and the item arrived damaged. Very disappointed.",  
"Amazing features and great value for money. Love the design and functionality.",  
"Slow delivery and average quality. Could be better for the price.",  
"Outstanding performance and beautiful design. Worth every penny!",  
"Terrible experience. Product broke after one day. Waste of money." 
] 
positive_words = { 
"excellent", "fast", "recommend", "amazing", "great", "love", "outstanding", "beautiful", "worth", 
"good", "fantastic", "perfect" 
}  
negative_words = {  
"poor", "damaged", "disappointed", "slow", "average", "terrible", "broke", "waste", "bad", "awful", 
"horrible", "worst"  
}  
product_features = {  
"quality", "delivery", "service", "design", "functionality", "performance", "price", "value", "features"  
}


# 1. Extract and count positive/negative sentiment words

review_sentiment_count = []
for review in reviews:
    positive_count = 0
    negative_count = 0
    words = review.lower().split()
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    review_sentiment_count.append((review, positive_count, negative_count))
    print(f"Review: {review}, Positive Words: {positive_count}, Negative Words: {negative_count}")




# 2. Find most frequently mentioned product features  


feature_count = {}
for review in reviews:
    words = review.lower().split()
    for word in words:
        if word in product_features:
            if word in feature_count:
                feature_count[word] += 1
            else:
                feature_count[word] = 1
                print(f"Feature Count Updated: {word} appears {feature_count[word]} times")

# 3. Identify customer concerns and compliments
customer_concerns = []
customer_compliments = []
print("Identifying customer concerns and compliments...")
for review in reviews:
    words = review.lower().split()
    if any(word in negative_words for word in words):
        customer_concerns.append(review)
        print(f"Customer Concern Identified: {review}")
    elif any(word in positive_words for word in words):
        customer_compliments.append(review)
        print(f"Customer Compliment Identified: {review}")


# 4. Generate a sentiment score for each review 

sentiment_scores = []
for review, positive_count, negative_count in review_sentiment_count:
    sentiment_score = positive_count - negative_count
    sentiment_scores.append((review, sentiment_score))
    print(f"Review: {review}, Sentiment Score: {sentiment_score}")