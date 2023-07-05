# Inato Data Engineering technical assignment

## How to Successfully Complete this Technical Assignment

Follow the steps below to successfully complete the assignment and showcase your skills:

1. Clone the repository provided (do **not** fork it).
2. Work through each step, starting with Step 1.
3. Commit your code at the end of each step to track your progress.
4. Publish it on your GitHub (or Gitlab, or whatever...)
5. Send us the link and tell us approximatively how much time you spent on this assignment

Note that the test should take between 1 to 3 hours to complete.


## Guidelines for Success

To ensure success and demonstrate your abilities, please adhere to the following guidelines:

- Begin with a simple approach to complete the initial steps.
- Each step builds upon the previous one, allowing you to reuse code when applicable. However, as you progress, focus on refactoring your code to make it maintainable, clean, robust, and reliable.
- Use Python (3.9) to write your code.
- Write your program within the appropriate level directory.
- Do not modify the following scripts: `application_generator.py` and `application_file_generator.py`.


## Step 1 : Transforming Application Logs

- Run the `application_file_generator.py` program to generate application logs. The logs will be saved in the `./applications/` folder. Each file represents one application and follows this format:

`id=0a0bd4d3-05cf-4912-b6ee-40d79a4f9901|therapeutic_area=oncology|created_at=2023-07-26 18:30:07|site={'name': 'CHU Bordeaux', 'site_category': 'academic'}`

- Your task is to read all these files and transform them into JSON files in the `./processed/application-{id}.json` format. The transformed JSON files should look like this:

```
{
   'id':'0a0bd4d3-05cf-4912-b6ee-40d79a4f9901',
   'therapeutic_area':'oncology',
   'created_at':'2023-07-26 18:30:07',
   'site':{
      'name':'CHU Bordeaux',
      'category':'academic'
   }
}
```

## Step 2 : Storing Application Logs in a MySQL Database

- Instead of writing the logs to files, we want to store them in a MySQL database.
- Use the following table schema to create a table named `application`:

```
CREATE TABLE application(
   id varchar(100),
   therapeutic_area varchar(10),
   created_at timestamp,
   site_name varchar(50),
   site_category varchar(20)
)
```

## Step 3 : Answering Questions based on the Stored Data

Based on the previously created table, you need to answer the following questions:

- Oncology specialization rate: Calculate the ratio of applications for oncology trials to the total number of applications for each Academic site.
- List of sites: Provide a list of sites that applied to at least 10 trials during the 14 days following their first application.

Write your SQL queries to answer these questions in the level_3/queries.sql file.

Note:
- If you haven't completed step 2, you can use the data stored in `./sample/applications_sample.csv`.
- There is no requirement to set up a database; we will solely focus on the SQL code.


Enjoy the assignment and good luck!


## Data details

**Trial applications on Inato:**

- `id`: application ID
- `therapeutic_area`: therapeutic area of the study for which the site is applying
- `created_at`: timestamp when the study application started
- `site_name`: name of the site who took part in the trial
- `site_category`: category the site who took part in the trial
