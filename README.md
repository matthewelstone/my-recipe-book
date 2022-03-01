# Milestone Project Three / My Recipe Book

[View the live project here](https://my-recipe-book-matt.herokuapp.com/)

<img src="assets/images/my-recipe-book-responsive.png">

## Contents

- [User Expreience](#user-experience)

  - [User Stories](#user-stories)
  - [Owner Goals](#owner-goals)
  - [Design](#design)

- [Features](#features)
   
  - [Current Features](#current-features)
  - [Features which I want to implement in the future](#Features-which-I-want-to-implement-in-the-future)

- [Technologies Used](#technologies-used)

- [Testing](#testing)
  - [User Stories](#user-stories) 
  - [Owner Goals](#owner-goals)
  - [Lighthouse Testing](#lighthouse-testing)
  - [HTML and CSS Testing](#html-and-css-testing)
  - [Known Bugs](#known-bugs)

- [Deployment](#deployment)

- [Credits](credits)

## User Experience

### User Stories

- **First Time Visitor Goals**

1. As a first time visitor, I want to easily understand the main purpose of the site.
2. As a first time visitor, I want to easily navigate through the site.
3. As a first time visitor, I want to be able to view other peoples recipes.
4.  As a first time visitor, I want to be able to search for existing recipes.
5.  As a first time visitor, I want to be able to register an account easily.

- **Returning Visitor Goals**

1.  As a returning visitor, I want to be able to view other peoples recipes.
2.  As a returning visitor, I want to be able to add my own recipes to the site.
3.  As a returning visitor, I want to be able to edit and delete my own recipes
4.  As a returning visitor, I want to be able to follow the site through social links

- **Admin Goals**

1. As an admin I would like full access to all pages
2. As an admin I would like to be able to remove any recipe from the site.

- **Site Goals**
1. I want the site to be attractive, responsive and easy to navigate for the user.
2. I want users to be able to add their own recipes to the site. 

### Design 

- ### Color Scheme

I wanted to choose a fairly minimal color scheme for this project as there would be pictures uploaded to the site via URL from the user.  Not knowing what these pictures would be I kept the colours minimal as to try and avoid clashing.
The colours used were based off of the colour sage #9DC183 to tie in with the food theme. 

- ### Fonts

All text is rendered in Roboto as it is easy to read and widely used. Giving the site a sense of familiarity to new users. This was obtained from Google Fonts. 

- ### Layout 

The site is designed to work and be used on various screen sizes with the layout changing responsively thanks to Materializecss.

### Deployment

- Creation 

I first created this repository by doing the following.

1. Logging into GitHub and clicking the green New button in the top right corner of the screen.
2. I then created a new repository using the Code Institute-Org/gitpod-full-template and used the repository name MyRecipeBook I then clicked create repository.
3.I had the Gitpod chrome plugin downloaded so I clicked the green Gitpod button on the repository where I could start to write code for the site.

### Forking the Repository

To fork the repository to contribute to the project you can do the following.
1. Log in to GitHub and open the MyRecipeBook repository.
2. At the top right hand side of the page underneath your profile there is a fork symbol.
3. Once you have clicked this the repository will be forked.

### Cloning the Repository

If you wish to clone the repository you can do the following.
1. Go to [My account](https://github.com/matthewelstone) and sellect the MyRecipeBook repository.
2. Next to the GitPod button (if you have GitPod installed) or in the top right click the code button.
3. Click download zip.
4. You can then open the repository with your chosen code editor.

### Create A MongoDB Database

A MongoDB Account is required for this.

1. Create a new database in MongoDB
2. Create collections for users, recipes, types and cuisines

### Environment Variables 

1. Create your env.py file which will contain sensitive information. Because of this add it to your .gitignore file. 
2. Within your env.py file
  - enter your Mongo_URI found within the 'connect' section of the cluster page.
  - set your IP and PORT
  - Create a secret key using [RandomKeygen](https://randomkeygen.com/)

### Heroku Deployment
A Heroku account is required for this.

1. Create a new app within Heroku.
2. Choose an original name for the app.
3. Within the deployment tab  select GitHub and link with your GitHub repository.
4. In settings reveal your config vars.
5. Add all the of the same environment variables as in the env.py file.
6. Within Deploy select enable Automatic deploys. Below this you can select which branch you would like to deploy.
7. Click this to open the App.

