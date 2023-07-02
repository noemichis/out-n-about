Back to [README.md](README.md)

- [Testing](#testing)
    - [User story testing](#user-story-testing)

- [Bugs](#bugs)

## TESTING

### FEATURE TESTING

|Page|Feature|Test Scenario|Test Case|Result|
|:---|:---:|:---:|:---:|:---:|
|All pages|Navbar|Go to Home page|Click Home link|Pass|
|All pages|Navbar|Go to Home page|Click Logo|Pass|
|All pages|Navbar|Go to About page|Click About link|Pass|
|All pages|Navbar|Go to Sign Up page|Click Sign Up link|Pass|
|All pages|Navbar|Go to Login page|Click Login link|Pass|
|All pages|Navbar|Go to Sign Out page|Click Sign Out link|Pass|
|All pages|Navbar|Display Login & Sign Up if not authenticated|Logout|Pass|
|All pages|Navbar|Display username & Sign Out if authenticated|Login|Pass|
|All pages|Navbar|Open Category dropdown|Click Categories link|Pass|
|All pages|Navbar|Go to selected Category|Click selected category|Pass|
|All pages|Category slide|Display all categories|All categories display|Pass|
|All pages|Category slide|Go to selected Category page|Click selected category|Pass|
|All pages|Form field validation|Required field not empty|Leave field empty|Pass|
|All pages|Messages|Message on user action is displayed|Login/ SignUp/ SignOut/ Comment/ Like|Pass|
|Home page|Hero button|Go down to all posts|Click Visit button|Pass|
|Home page|Hero message|Display message if user not authenticated|Click Sign out|Pass|
|Home page|Hero message|Do not display message if user authenticated|Click Sign in|Pass|
|Home page|Hero message|Go to Login page|Click Login button|Pass|
|Home page|Hero message|Go to Sign Up page|Click Sign Up button|Pass|
|Home page|Card loop|Display all cards|All cards display correctly|Pass|
|Home page|Cards loop|Go to selected Post page|Click selected post|Pass|
|Categories page|Category slide|Category active|Click selected category|Pass|
|Categories page|Conditional check posts|Show posts from selected category only|Click selected category|Pass|
|Post Detail page|Like button if authenticated|Register like on page|Click regular thumbs up icon|Pass|
|Post Detail page|Like button if not authenticated|Button not clickable|No action|Pass|
|Post Detail page|Unlike post|Remove like from page|Click solid thumbs up icon|Pass|
|Post Detail page|Leave a comment if authenticated|Comment submitted|Add comment and submit|Pass|
|Post Detail page|Leave a comment if not authenticated|Not shown|No action|Pass|
|Post Detail page|Edit and Delete buttons if user=creator|Show buttons|Login|Pass|
|Post Detail page|Edit and Delete buttons if user!=creator|Not shown|Logout|Pass|
|Post Detail page|Edit comment|Go to Comment Edit page|Click Edit button|Pass|
|Post Detail page|Delete comment|Open Comment Delete Modal|Click Delete button|Pass|
|Post Detail page|Confirm Comment Delete|Confirm Delete comment|Click Delete button|Pass|
|Post Detail page|Close Comment Delete Modal|Close Modal|Click Close button/Click X on top|Pass|
|Comment Edit page|Edit comment|Update existing comment|Edit then click Update button|Pass|
|Sign Up page|Redirect to Login|Go to Login page|Click login link|Pass|
|Sign Up page|Sign Up button|Sign Up and go to Home page|Click Sign Up button|Pass|
|Sign Up page|Username validation|Username exists|Enter existing username|Pass|
|Sign Up page|Password validation|Password too short/common|Enter short/common password|Pass|
|Sign Up page|Password validation|Password must be same in both fields|Enter different password in again field|Pass|
|Login page|Login button|Login and go to Home page|Click Login button|Pass|
|Login page|Password/username validation|Password and username must exist|Enter incorrect credentials|Pass|
|Login page|Remember me checkbox|Allow user to stay authenticated|Checkbox active|Pass|
|Sign Out page|Sign Out button|Sign Out and go to Home page|Click Sign Out button|Pass|
|Footer|Social links|Go to social page|Facebook/ Instagram/ Twitter|Pass|

### USER STORY TESTING

|ID|User Story|Acceptance criteria|Test Case|
|--|:---|:---|:---|
|1|As a **user** I can **create an account** so that **I can comment and like**|Account can be created and functional|Pass|
|2|As a **registered user** I can **login** so that **I can interact with the site**|Login with username/email and password|Pass|
|3|As an **authenticated user** I can **easily find the log out button** so that **I can log out at anytime**|Place the logout button evidently/ Logout function works|Pass|
|4|As a **user** I can **select different categories** so that **the content is better sorted**|Posts are organized in categories/ Each category can be selected|Pass|
|5|As a **user** I can **view a list of posts** so that **I can select one to read**|Posts are listed on landing page/ Posts are listed under Category page|Pass|
|6|As a **user** I can **see the post description** so that **I know what it will be about**|Post summary visible for all users|Pass|
|7|As a **user** I can **open a post** so that **I can view it's contents**|A user can select a post and open it/ All post information is available once opened|Pass|
|8|As a **user** I can **view the comments** so that **I can see others opinion**|Comments can be viewed by all users|Pass|
|9|As an **authenticated user** I can **comment on a post** so that **I get engaged in the conversation**|Comments can be posted and are visible|Pass|
|10|As an **authenticated user** I can **update my comments** so that **I can edit it again**|Comments can be updated by creator|Pass|
|11|As an **authenticated user** I can **delete my comments** so that **it's not visible to others**|Comments can be deleted by creator|Pass|
|12|As a **user** I can **intuitively navigate the page** so that **I have the full experience**|Intuitive navigation page|Pass|
|13|As a **user** I can **view the number of likes** so that **I know how popular a post is**|Like count is visible to all users|Pass|
|14|As an **authenticated user** I can **like/unlike a post** so that **I can interact with the content**|Like button can be clicked, then unlicked|Pass|



|ID|Admin User Story|Acceptance criteria|Test Case|
|--|:---|:---|:---|
|1|As an **admin user** I can **set up an admin user** so that **I have access to the admin site**|Admin panel ready to use|Pass|
|2|As an **admin user** I can **create, update and delete posts** so that **I can manage the content**|Post can be created, updated, deleted via the Admin site|Pass|
|3|As an **admin user** I can **edit and delete comments** so that **I can moderate the content**|Comments can be updated/deleted from the Admin site|Pass|



## BUGS