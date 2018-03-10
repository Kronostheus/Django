# KronoPost
An attempt at creating a reddit like website using Django framework

### Built With
- [Django Web Framework 2.0.2] (https://www.djangoproject.com/)
- [Materialize CSS] (http://materializecss.com/)
- [jQuery] (http://code.jquery.com/)
- [XAMPP] (https://www.apachefriends.org/)

## Motivation
Decided to learn Django Framework by completing a project. Wanted to created something other than a blog (90% of tutorials out there).
I wrote code as I learned about the framework and searched online for help when stuck and by no means represents the best coding standards out there.
However, I did make an effort of keeping the code clean and simple, as well as trying to at least follow some of those standards.

## Features

### Navigation Bar
* Register, Log In, Log out
* Home button (KronoPost)
* Currently signed in user (right)
* Create Post (right - only available to signed in users)

### Link List
* List ordered by votes (descending order)
* Pagination implemented allowing (*currently*) 10 links per page

* Green *updoot* button for voting (user can only cast one *updoot* per link)
* Link (will go to link's page within KronoPost)
* Comment count


### Link Page
* Link Headline
* Link URL (if existing)
* Link Submitter
* Link Description (blank if non-existant)
* Comment Button (signed in only)
* Comments (threaded with ability to reply to existing comments)

Original Poster will be able to see orange wrench at bottom of the page that allows:
* Delete Post (with confirmation screen)
* Edit Post
