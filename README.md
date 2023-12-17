# Nutrition Tracker Project

## Description
This project constitutes an integral part of a fitness centre's digital ecosystem, empowering users to meticulously track their nutritional intake through personalized notes. It seamlessly integrates with a diverse range of meal plans, 
offering users a comprehensive tool to manage and follow their dietary routines.

### Check it out
https://nutrition-tracker-z8km.onrender.com/

#### Use these credentials:

  - Login: `UserBIT`
  - Password: `Bit11222`

### Key Features:

1) Nutrition Tracking with Notes: Users can log detailed notes on their daily nutritional intake, precisely capturing the specifics of each meal.
2) Meal Plan Integration: The platform offers seamless integration with various pre-designed meal plans catering to different fitness goals, including weight loss, muscle gain, cardiovascular health, and more.
3) It provides food nutrition data to users.

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

### Run project on your own Desktop:

  Python 3.8+ is required 

1) `python manage.py migrate`

2) Use the following command to load prepared data from fixture to test and 
debug: `python manage.py loaddata test_data.json`

3) `python manage.py runserver`

- After loading data from the fixture you can use the following superuser to log in to the site:
  - Login: `admin`
  - Password: `admin`

# Site description

### Home Page
Displays the total number of users, food items, and available meal plans.
![home_page](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/0675cdbc-efb7-4be4-a91c-2dccd20ca718)

### Food Page
Presents a table listing each food item.
![food_list](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/930761ea-32ee-4bac-981b-cfec99b242aa)

### Meal Plans Page
Showcases available meal plans ready for assignment.
![meal_plans](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/d53c7e23-e4d1-4f8b-a4fb-a365dcfff2b8)

### Tracker Page
Features a personalized nutrition tracker, displaying user-specific data.
![nutrition_tracker](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/a5b63855-5e23-4f8c-a82b-b0683147599e)

### Users Page
Showcases all registered users.
![users](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/f8cfa298-50eb-46f5-8248-71462eb5c791)

### Meal Plan Detail Page
Provides detailed information about a specific meal plan.
![meal_plan_detail](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/d90b887b-70b0-4797-803a-043ca26551b3)

### Login Page
Offers a login form.
![login_page](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/72be36a4-707f-4cec-981f-464bdf1bb605)

### User Registration Page
Presents a form for new user registration.
![registration_form](https://github.com/Shatrovskyi/nutrition_tracker/assets/61559978/67cf8739-3e06-41ba-937b-d25bf86f315b)
