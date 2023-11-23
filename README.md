# Nutrition Tracker Project

## Description
This project constitutes an integral part of a fitness center's digital ecosystem, empowering users to meticulously track their nutritional intake through personalized notes. It seamlessly integrates with a diverse range of meal plans, 
offering users a comprehensive tool to manage and follow their dietary routines.

### Key Features:

1) Nutrition Tracking with Notes: Users can log detailed notes on their daily nutritional intake, capturing the specifics of each meal with precision.
2) Meal Plan Integration: The platform offers seamless integration with a variety of pre-designed meal plans catering to different fitness goals, including weight loss, muscle gain, cardiovascular health, and more.
3) It provides food nutrition data to user.

### Diagram
![Tracker](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/c79677ea-1d6d-473c-bc37-f79eed3473b2)

## Installation

### Set up the environment
    
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    

### Set up requirements
- Python 3.10

    ```
    pip install -r requirements.txt
    ```

### Set up database and make migrations
1) `python manage.py makemigrations`
2) `python manage.py migrate`
3) Use the following command to load prepared data from fixture to test and debug:
  
    `python manage.py loaddata test_data.json`

- After loading data from fixture you can use following superuser to log in to site:
  - Login: `admin`
  - Password: `admin`

# Site description

### Home Page
Displays the total number of users, food items, and available meal plans.

### Food Page
Presents a table listing each food item.

### Meal Plans Page
Showcases available meal plans ready for assignment.

### Tracker Page
Features a personalized nutrition tracker, displaying user-specific data.

### Users Page
Showcases all registered users.

### Meal Plan Detail Page
Provides detailed information about a specific meal plan.

### Login Page
Offers a login form.

### User Registration Page
Presents a form for new user registration.
