Customer Feedback Analyzer 
Introduction
This project is a simple command line based application. It tries to analyze customer feedback and understand what the user has review about the product. The idea is not very complex but still useful. It takes a  input and then gives output in terms of sentiment and the main aspect related to that feedback.
 It checks whether the feedback is positive, negative, or neutral. It also tries to figure out if the feedback is about delivery, product, or service. Sometimes it works really well, sometimes the data is less but overall decent.


How it works 
The method employed by the system is rule-based. No machine learning model that has been trained is used. It uses pre-made lists of words. 
The user inputs a sentence at the beginning. The software breaks the sentence up into individual words and changes everything to lowercase. 
Each word is then compared to various categories, such as aspect-related words, negative words, and positive words. 
  There is a brief logic for dealing with negation. For instance, the system will interpret the input as negative rather than positive if it contains something like "not good." Although this negation is not very sophisticated, it enhances the system. 
The system determines the overall sentiment and the primay aspect based on the scores.

Features 
1)This project runs in the terminal because it is entirely CLI-based. There is no GUI utilised. 
2)Sentiment detection, aspect detection, and simple negation handling are the primary features.
 3)it displays the score of both positive and negative matches, which facilitates comprehension of the decision-making process. 
4)It is simple to run on any system because it is lightweight and doesn't require any external libraries. 



Technology used 
Python is used in the project's implementation. There is no need for external libraries or modules. Basic Python ideas like dictionaries, condition statements, and loops are used for everything.


How to run
1)First install python and then save feedback analyzer.py in your system
2)Open terminal and run
3)python feedback_analyzer.py
4)Now you can enter feedback directly in the terminal.
5)To quit the program, just type exit.

Example
If you enter:
The product is good but delivery was late
The output :
Sentiment: Neutral  
Aspect: delivery  
Scores: {'positive': 1, 'negative': 1}
