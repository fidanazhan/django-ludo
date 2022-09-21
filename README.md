Sport App which users can host or participate for sport games in their local area. Created using Django for the backend and simple Html, CSS and Javascript for the frontend

# LUDO - V1
Sport App which user can host or participate to sport game in local area. Created using django for the backend and simple html css for the frontend.

## TABLE OF CONTENTS
  
  -  [Overview](#overview)
  -  [Technology](#technology)
  -  [Requirement](#requirement)
  -  [Screenshot](#screenshot)
  -  [Status](#status)
  -  [Contact](#contact)

## **OVERVIEW**

Ludo is a sport app where users can host and participate in a sport game in their local area. This simple app was created because there was a difficulty in gathering people to play certain sports. A host (people who host a game) can create a game, set venue and date before accepting any join request from other users. Participants (users who want to join) can see the sport type, venue, location, date and price to join before they send a join request to the host. With this app, users can play their favorite sport with strangers and can make new friends.

## **TECHNOLOGY** 

- Framework/Stack : Django, HTML, CSS, Javascript, PostgreSQL
- System Architecture : Monolithic (without using API)
- Software Architecture : MVT

## **REQUIREMENT**

- User can see list of games
- (Host) User can create new game
- (Participant) User can send request to join the game.
- (Host) User can approve or decline the join request.
- (Participant) User can unsent the join request.
- (Host) User can remove the player from the game.
- (Participant) User can unjoin the game.
- User can see the list of games that they had joint or games that they will play soon.
- Send notifications to the user.
- User can see list of received notifications.

## SCREENSHOT

**Dashboard pages** - Place where users can see their games played, number of games created and number of join requests sent. The two boxes in the center will be graphs that show analytics for the games played by the user (not completed yet). The row below the graphs is the data of incoming games that the user will play. Accepted user by host to join the game can cancel their joining by clicking the ‘Unjoin’ button.

![Dashboard Page](https://user-images.githubusercontent.com/108860416/191470739-30f30461-3aed-405b-89ec-dd76763caf76.PNG)
&nbsp;

**Game page** - Page where users can see available games.

![Games Page](https://user-images.githubusercontent.com/108860416/191470746-4c7aad70-8652-4ddc-954b-9be0c98085ff.PNG)
&nbsp;

**Host - Games Page** - Page where the users can see the list of games they created. When they click to the blue button, they can see the list of join requests sent by other users for that specific game (redirect to Host Join Request for Game Page). 

![Host - Game Page](https://user-images.githubusercontent.com/108860416/191470754-46814f9e-c581-4cf2-9bac-c6690371159d.PNG)
&nbsp;

**Host - Join Request for Game Page** - Page where you can see a list of join requests for specific game.

![Host - Join Request for Game Page](https://user-images.githubusercontent.com/108860416/191470769-67e1a501-b4da-43f3-923a-3e972a181555.PNG)
&nbsp;

**Participant - Join Requests Page** - Page that list all join requests that you have applied as a participant. You can manage your join request here. Cancel any requests that you have applied for if you have any business on the date. 

![Participant - Join Request for Game Page](https://user-images.githubusercontent.com/108860416/191470779-eb8c6594-f527-4f61-a795-685f2df93ece.PNG)
&nbsp;

**The Notification page**, **Profile page** and **Competition page** is still in development.

## STATUS

Not Completed. Ongoing development.

## CONTACT 

Created by [Fidan Azhan](https://github.com/fidanazhan) - feel free to contact me!
