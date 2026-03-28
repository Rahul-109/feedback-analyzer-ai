def feedback (text):
    words = text.lower().split()

    reviewdic = {
        "positive": [ "good", "positive", "great", "excellent", "amazing", "awesome",
        "nice", "satisfied", "happy", "love", "fast",
        "perfect", "best", "smooth", "impressive",
        "fantastic", "wonderful", "brilliant", "superb",
        "pleased", "delightful", "outstanding", "reliable",
        "efficient", "quick", "easy" ],

        "negative": [ "bad", "negative", "poor", "worst", "slow", "late",
        "damaged", "broken", "hate", "terrible",
        "disappointed", "issue", "problem", "delay",
        "awful", "horrible", "useless", "faulty",
        "defective", "annoying", "frustrating",
        "unsatisfactory", "pathetic", "difficult", "hard"]
    }
    problemdic = {
        "delivery": [ "delivery", "late", "early","deliver", "delivered", "delivering", "shipping",
        "shipment", "ship", "courier", "dispatch", "dispatched",
        "arrival", "arrived", "arriving", "delay", "delayed",
        "late", "slow", "fast", "early", "on-time",
        "tracking", "track", "package", "parcel", "logistics",
        "transit", "route", "out-for-delivery", "received", "pickup" ],

        "product": [ "product",  "item", "goods", "quality", "material",
        "design", "size", "color", "colour", "feature", "performance", "build", "durability", "defect", "damaged", "broken", "working", "function", "fit", "finish", "original", "fake","packaging", "brand", "model", "specification",
        "condition", "value", "price", "worth"],

        "service": [ "service"," support", "customer", "help", "response",
        "staff", "team", "assistance", "behavior", "behaviour",
        "communication", "call", "email", "reply", "delay",
        "helpful", "unhelpful", "experience", "interaction",
        "attitude", "guidance", "resolution", "issue",
        "complaint", "handling", "feedback", "contact",
        "availability", "polite", "rude"]

    }
    reviewscore = {"positive": 0, "negative": 0}
    problemscore = {"delivery": 0, "product": 0, "service": 0}

    i=0
    while i < len(words):
        word = words[i]
        if word == "not" and i + 1 < len(words):
            otherwords = words[i + 1]
            if otherwords in reviewdic["positive"]:
                reviewscore ["negative"] += 1
            elif otherwords in reviewdic["negative"]:
                reviewscore ["positive"] += 1
            i+=2
            continue

        for r in reviewdic:
            if word in reviewdic[r]:
                reviewscore [r] += 1
        for p in problemdic:
            if word in problemdic[p]:
                problemscore [p] += 1
        i+=1

        if reviewscore["positive"] > reviewscore["negative"]:
            finalreview = "Positive"
        elif reviewscore["negative"] > reviewscore["positive"]:
            finalreview = "Negative"
        else:
            finalreview = "Neutral"


        main = max(problemscore,key=problemscore.get)
        if problemscore[main] == 0:
            main ="General"

    return finalreview,reviewscore,main

print("Customer Feedback Analyzer")
print(" To quit type exit \n")
while True:
    userinput = input("Enter your feedback: ")
    if userinput.lower().strip() == "exit":
        print("Thankyou")
        break

    review,scores, problem = feedback(userinput)

    print("Result ")
    print("Review:", review)
    print("scores:", scores)
    print("Category:", problem)

