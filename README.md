# Final_Project_JCDS02Bandung
# Recommendation System (Content-Based) and Linear Regression Prediction of Zomato India
## By: Muhammad Irfan
### __Dataset__ : Zomato Restaurants Data 
## About
Zomato is a restaurant search site that provides information for eating out, take-out messages, cafes and nightlife for cities in Indonesia, India, Turkey, New Zealand, Philippines, South Africa, Sri Lanka, Qatar, United Arab Emirates, and English. According to the Alexa website, this site ranked 1,926 in the world and 205 in India in October 2013.Dataset was taken from Kaggle (reference:https://www.kaggle.com/shrutimehta/zomato-restaurants-data).

The collected data has been stored in the Comma Separated Value file Zomato.csv. Each restaurant in the dataset is uniquely identified by its Restaurant Id. Every Restaurant contains the following variables:

• Restaurant Id: Unique id of every restaurant across various cities of the world
• Restaurant Name: Name of the restaurant
• Country Code: Country in which restaurant is located
• City: City in which restaurant is located
• Address: Address of the restaurant
• Locality: Location in the city
• Locality Verbose: Detailed description of the locality
• Longitude: Longitude coordinate of the restaurant's location
• Latitude: Latitude coordinate of the restaurant's location
• Cuisines: Cuisines offered by the restaurant
• Average Cost for two: Cost for two people in different currencies
• Currency: Currency of the country
• Has Table booking: yes/no
• Has Online delivery: yes/ no
• Is delivering: yes/ no
• Switch to order menu: yes/no
• Price range: range of price of food
• Aggregate Rating: Average rating out of 5
• Rating color: depending upon the average rating color
• Rating text: text on the basis of rating of rating
• Votes: Number of ratings casted by people
## Data price prediction is processed using regression with the model taken using Gradient Boosting Classifer and data recommendation is processed using Count Vectorizer and Cosine Similarity.
### Apps
#### Home Page of Prediction
![Screenshot 2020-05-21 23 13 04](https://user-images.githubusercontent.com/60774720/82580750-caafdf00-9bb9-11ea-8e1a-6940a67300fa.png)
#### Result Prediction of Average Cost for Two ($USD)
![Screenshot 2020-05-21 23 14 04](https://user-images.githubusercontent.com/60774720/82580944-0a76c680-9bba-11ea-9036-6ccc39b28381.png)
#### Recommendation Input Page
![Screenshot 2020-05-21 23 14 38](https://user-images.githubusercontent.com/60774720/82581090-37c37480-9bba-11ea-9d41-3b7ba66a1254.png)
#### Recommendation Result Page
![Screenshot 2020-05-21 23 15 14](https://user-images.githubusercontent.com/60774720/82581143-4ca00800-9bba-11ea-9e0f-53bc11ea6215.png)

Hopefully this prediction engine and recommendation engine can help your problem!
