# Simple Flask Calculator with history
## Make sure to add a "project.db" database!

## Description:

#### Introduction:

Hello! My name is Zaid Yaseen and welcome to my 2024 cs50 Final project, it has been a very fun and educational journey which tough me a lot about many thing related to Computer Science including learning different programming languages and technical topics.

#### Why I chose this idea:

I initially wanted to do a e-commerce website for a computer shop, but found that I would run out of time perfecting everything and finalizing the design, so I chose a simple calculator web-app instead with some extra features which I thought were unique enough to not be a lazy project. A big reason I doubled down on the idea was thinking of implementing a history feature, which I haven’t seen implemented in a calculator project online.

## Design Choices:

#### Bootstrap:

I learned Bootstrap during week 9 about Flask, and I liked the way I can quickly display and style elements that look modern and sleek without having to go into a rabbit hole about CSS styling, syntax, allowed values, precedence etc. (spoiler alert: I still had issues with Bootstrap in some situations).

#### User Management:

I wanted to add some complexity to my project and apply the thing I learned in week 9 as much as possible (I really like week 9). There wasn’t any real beneficial reason why I added user management, but I did it correctly by adding security to the SQLite user database through hashing of user passwords.

#### Colours/Theming:

I initially wanted a fully dark theme revolving around dark green and using colours of my own choice, but later decided I preferred colours inspired by Bootstraps light theming, like the primary-subtle colour for the website’s background, danger and danger-subtle for error handling etc.. There’s also a calculator favicon for the website’s logo that’s shown in the browsers website tab.

#### Functionality:

As cool as the apology page error handling in the CS50Finance was, it wasn’t in the best interest of users, as it forced them to go to another page, and go back again to the page they made the error, whether it was during logging in or buying stocks etc. Every time they make an error which wasted time and maybe infuriate some. Which is why I made the login/register error handling in the form of a “Sticky form”, i.e the user stays on the same page when they make an error, and a simple error message appears instantly. It is a win-win situation for both the user and the coder (in terms of simplicity and time savings).

I also decided later in development that I wanted a backspace button on the calculator, which adds to the convenience of not having to retype the entire mathematic expression when the user makes a mistake.

## Code logic under the hood:

#### Flask/Python:

The Flask and Python parts of the project are responsible for routing across the different web pages, manage users in the project.db database, and making sure there is error handling in the login and registering forms as well as authorization and validation of user accounts.

The helpers Python file simply contained a function to help with the login procedure, and the requirements.txt file contained the Python packages and libraries needed for the project’s logic to function.

#### Jinja templates:

Jinja and other similar templating languages are a really good addition to any project; Because they save time by negating the need for constantly coding in elements of the design that are always there, and they help reduce the complexity of code and minimise confusion when reading the source code from an external point of view.

#### Calculator code design:

My decision to use a table layout for the main calculator elements instead of a form or some sort CSS flex grids was due to having more familiarity with tables than the other options, and that I could quickly change the position of the buttons, their size, the amount of buttons in each row etc.

#### JavaScript:

Embedded JavaScript scripts were used in calculating mathematic expressions, appending the clicked buttons the calculator’s display, backspace and clear abilities, elegant error mesasges in the login and registering forms, and various functions of the calculator history.

#### ⭐The History⭐:

The star ;) of the show and the big and unique feature of the project, it allows users the ability to remember their past mathematic operations, lock the history to important calculations visible and tidy, and copy them to share with friends and colleagues. It’s a simple yet useful part of the calculator inspired by my phone’s calculator app, but with an extra lock function!
