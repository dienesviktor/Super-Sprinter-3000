# Super-Sprinter-3000

A simple web application to help teams track their progress during a project in Agile system.

The Agile methodology is a way to manage a project by breaking it up into several phases.
It involves constant collaboration with stakeholders and continuous improvement at every stage.
Once the work begins, teams cycle through a process of planning, executing, and evaluating.
Continuous collaboration is vital, both with team members and project stakeholders.

### Description
1. The opening page list all User Stories.
    - The opening page of the website (`/`) shows all data of the saved user stories.
    - The columns of the table are "Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", and "Status".
    - There is an "Add a new User Story" link on the top of the page, pointing to the `/story` page.
    - The Story titles are links, pointing to the `/story/<id>` page where the User Story can be updated.

2. It is possible to add a new User Story through a web form on page `/story`.
    - The `/story` page shows an empty web form.
    - The form has an input field for all User Story fields except for `id` and `status`.
    - Clicking the "Add new User Story" button results in the form submitting the data that gets saved.
    - When a new User Story is saved, a unique `id` is generated for it.

3. It is possible to update an existing User Story through a web form on page `/story/<id>`.
    - The `/story/<id>` page shows the same web form as on the "Add new" page but filled in with data of the given User Story.
    - The form has an input field for all the User Story fields except `id`.
    - The "Status" field also appears as a dropdown value list, with options `planning`, `todo`, `in progress`, `review`, `done`.
    - The current status of the User Story is selected by default.
    - Clicking the "Update User Story" button updates the existing entry and does not create a new one.

4. The application persists data using a `.csv` file.
    - The User Story list and the form data are loaded from a `.csv` file upon update.
    - Form data is saved to a `.csv` file.

### Instruction:

To start:
```
python server.py
```

To install requirements:
```
pip install -r .\requirements.txt 
```
