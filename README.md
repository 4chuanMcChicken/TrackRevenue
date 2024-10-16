# Assignment Submission

Thank you for considering my application!

For this assignment, I began by reading and parsing the JSON file to extract the data. I then created a dictionary to assign weights to each permission, ensuring that the permission columns are displayed in the same order as shown in the example. By iterating through each user's permissions, I determined whether to append "1" or "0" based on whether the user has the corresponding permission.

To generate the CSV file, I utilized Python's `csv` module to write the processed rows to a file.

For integration with the Google API, I set up credentials for a **service account**, which is ideal for server-side operations or running scripts. Using these credentials, I updated the generated rows to a Google Sheet.

I have added `credentials.json` in the `.gitignore`, but I have an example `example_credentials.json`, which has the same format.

The Google Sheet URL is:

[Google Sheet Link](https://docs.google.com/spreadsheets/d/e/2PACX-1vT6LvIUwm5H7KCwIlPS1bE674EmujGbvxqiXdOSmGGHnkMQZttB4IW69TeLTuXJkN_T3-e9wCwJyCx_/pubhtml)
