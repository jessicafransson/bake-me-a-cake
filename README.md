# Bake me a cake

Here's a link to the live project (https://bakemeacake2022.herokuapp.com/)
------
### Bake me a cake is a online recipe-sharing website for people that love baking, and being creative in the kitchen when it comes to cakes or treats.

This project is built using Django Framework in Python.


![responsive](assets/images/mockup.jpg)
------

## Content 

- User experience
 * user stories

- Design
 * color and inspiration

- features
 *

- technologies
 * libraries and languages

- testing (#TESTING.md)

- deployment 

- credits 


------
## User experience (UX)

The one visiting bake me a cake is most likely someone who loves to bake, and is looking for new recipes, or who wants to share their favourites and connect with other like minded people. 

------

## User stories

Following is a list of my user stories and it can also be found [here] (https://github.com/jessicafransson/bake-me-a-cake/issues).

### EPIC | Navigation
- As a User I can immediately understand the website's purpose so that I know if it's what I'm looking for.
- As a User I can navigate around the site so that I can easily view the content.
- As a User I can view a list of recipes so that I can choose one to read.
- As a User I can click on a recipe to see the full recipe
- As a User I can click on the recipe to like and leave feedback.

### EPIC | User's Recipes
- As a User I can create recipes so that other users can view them
- As a User I can edit recipes and the image so that I can update any changes or mistakes to my recipes.
- As a User I can delete recipes so that I can remove any unwanted recipes I have made.

### EPIC | User Interaction
- As a User I can like/unlike recipes so that I can mark which recipes I enjoyed.
- As a User I can leave a comment so that I can give my feedback to others.
- As a User I can view the number of likes on each post.
- As a User I can view comments on recipes so that I can read feedback on recipes.

### EPIC | Sign in
- As a User I can register for an account so that I can add my own posts
- As a User i can register for an account so that I can add comments and like posts
- As a user i can log in to like recipes, comment and manage my own posts

### EPIC | Admin
- As an Admin I can view, create, edit and delete all recipes so that I can control the website's content.
- As an admin i can view, create, edit and delete all comments so i can control the content of the recipes.

------

## Design

The look of this project is inspired by Code Institutes "I think therefor I blog" project and swedish pastry Queen Camilla Hamid. Find her live website [here] (https://mykitchenstories.se/)

### Color Scheeme 
- I wanted to keep this website basic and easy to navigate. The color of header and footer is taken from Camilla Hamid, but text is altered to a black-ish color to update the accessibility score. 
- I also want to make sure that the images from the recipes pop-out, as users can add any image. 

### Images
- The images has been taken from pixabay that is currently displayed on the project, future images will be uploaded by various users. 

### Wireframe 

- I planned out my project using Figma, designing a style i was going for,
and with inspiration from earlier mentioned website [Camilla Hamid](https://mykitchenstories.se/) i came up with the final design.

* First mockup design looked like this:

![Mockup](assets/images/figma_mockup.png)

------

## Features

### Home page

- #### Navigation bar
    - The navbar is always present at the top of the page and houses the links to add recipe, login, logout, create account and home. 
    - The option to add a recipe will only be displayed when a user is logged in
    - The navbar is always a hamburger bar, to make it as easy as possible to focus on the recipes displayed. 

    ![Navbar](assets/images/navbar.png)

------

- #### Hero image
    - The hero image will be displayed on all pages you visit on the website.
    - The hero image contains a text welcomming them to a world of awesome cakes.

     ![Hero Image](assets/images/heroimage.png)
    
------

### Recipe detail 

- #### Displaying recipes
    - The main page displays an image of the recipe along with the author, title of recipe and will display amount of likes.
    - It also displays the date and time the recipe was created

    ![Recipes](assets/images/recipes.png)

- #### Recipe view
    - When the user clicks a recipe they get to the full recipe page

    ![Recipe view](assets/images/recipeview.png)


-------

- #### Interactivity 
    - The user can see the amount of likes and comments at the top of the recipe:

    ![View Likes and comments](assets/images/likes_comments.png)

    - The user can also like the post at the top of the recipe, by clicking the heart:

    ![Liked Recipe](assets/images//liked_post.png)

    - The user can view and read the feedback left on a recipe: 

    ![View Comment](assets/images/view_comments.png)

    - The user can leave feedback in the end of the recipe:

    ![Leave Comment](assets/images/leave_comment.png)

    - The user can add their own recipes:

    ![Add Recipe](assets/images/add_recipe.png)

    - The user sees the choise to edit/delete recipes:

    ![Edit and delete buttons](assets/images/edit_delete_buttons.png)

    - The user can edit their own recipes:

    ![Edit Recipe](assets/images/edit_recipe.png)

    - The user can delete their own recipes:

    ![Delete Recipe](assets/images/warning_delete_post.png)

------ 

- #### Pagination
    - In the end of the page the user will see buttons for going to next page, or back up to previous page.

    ![Next](assets/images/pagination_next.png)
    ![Previous](assets/images/pagintion_prev.png)

-------

- #### Footer 
    - At the end of each page the user will be displayed with the footer.
    - The footer contains clickable links.
    - The links to Twitter and Facebook links to the general log in page.
    - The link to GitHub directs the user to my GitHub profile for this project.

    ![Footer](assets/images/footer.png)

-------

### Accounts

- #### User Registration
    - The user gets this view when asked to sign up:

    ![Sign up](assets/images/signup.png)

- #### User Login 
    - The User gets this view when logging in:

    ![Log in](assets/images/signin.png)

- #### User Logout
    - The user sees this when signing out:

    ![Sign out](assets/images/signout.png)

--------

## Features to add

### For the recipe owner 

    - Add the possibility for users to add specified allergies.
    - Add the possibility for users to add ingredients in it's own box.
    - For the user to add a rating system as to how difficult the recipe is.
    - For the user to be able to share the recipe on social media.

### For the visitor

    - For the logged in visitor to add a rating system on each recipes after trying the recipe.

### For the site owner

    - To add a search bar to easy find recipes.
    - To add a users profile page where the user can see their own recipes easily.
    - To add a featured recipe that changes regularly.
    - To add boxes per category, etc one for chocolates, one for candy, one for christmas.


-------

## Technologies

### Languages used:

- HTML 5
- CSS3
- Python

### Libraries and Programs used: 

- Git, for version control.
- GitHub, for storing code and deploying site.
- Gitpod, Used to build project and editing the code.
- Django, a python based framework to develop this project
- Bootstrap, for HTML design templates.
- Cloudinary, to store images. 
- Figma, to mockup the design.
- ElephantSQL, database through Heroku.
- W3C for validation of HTML and CSS.
- Pep8CI for validation of Python.
- Summernote, for usage in the admin panel.
- Heroku, for deploying the project. 
- Convertion, for converting JPG to AVIF. 

## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

- The project is deployed with Heroku and GitHub, with following steps: 

