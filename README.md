# TITLE : MdAuction : Recommendation System

## 1.Methodology
 * Models: Our application has three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings.
 * Create Listing: Users are able to visit a page to create a new listing. They are able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
* Active Listings Page: The default route of our web application lets user view all of the currently active auction listings. For each active listing, this page displays (at minimum) the title, description, current price, and photo (if one exists for the listing).
 * Listing Page: Clicking on a listing takes users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
If the user is signed in, the users are able to add the item to their “Watchlist.” If the item is already on the watchlist, the user are able to remove it.
If the user is signed in, the users are able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user be presented with an error.
If the user is signed in and is the one who created the listing, the user have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
 * Watchlist: Users who are signed are able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
 * Categories: Users are able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
 * Django Admin Interface: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.



## 2.Description
This is the project I made which is an e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a watchlist.When users are shopping online, not all will end up purchasing something. Most visitors to an online shopping website, in fact, likely don't end up going through with a purchase during that web browsing session. It might be useful, though, for a shopping website to be able to predict whether a user intends to make a purchase or not: perhaps displaying different content to the user, like showing the user a discount offer if the website believes the user isn't planning to complete the purchase.We build a nearest-neighbor classifier to solve this problem. Given information about a user — how many pages they've visited, whether they're shopping on a weekend, what web browser they're using, etc. — this classifier will predict whether or not the user will make a purchase.

Best Model : nearest-neighbor classifier
<br>
Correct: 4073
Incorrect: 859
True Positive Rate: 6.37%
True Negative Rate: 76.22%

## 3.Input/Output
Input: Meta data along with search history
<br>Output: Recommendation of product

## 4.Live Link
Link : [http://mdauction.herokuapp.com/](http://mdauction.herokuapp.com/)
Video : [Design a eBay-like e-commerce auction site that will allow users to post auction listings,place bids](https://youtu.be/Mr235c-7P_A)

## 5.Screenshot of Interface
![image](https://user-images.githubusercontent.com/67876213/208265384-2f91230b-060e-4060-8c5a-3f12901f0299.png)
![image](https://user-images.githubusercontent.com/67876213/208265405-fafdf004-3a2c-4ae4-98bd-4b33ce0c67ab.png)
![image](https://user-images.githubusercontent.com/67876213/208265436-b368afcc-8a11-4df3-9552-e38d5be8105d.png)


