# Team Member Management Application

A simple web application for managing team members built with Django. This application allows users to view, add, edit, and delete team members with an intuitive interface.

## Features

- View all team members in a clean, organized list
- Add new team members with detailed information
- Edit existing team member details
- Delete team members
- Automatic phone number formatting (XXX-XXX-XXXX)
- Role-based member types (Admin/Regular)
- Responsive design

## Usage

### Viewing Team Members
- Navigate to the home page to see all team members
- Members are displayed with their name, phone number, and email
- Admin members are marked with "(admin)" next to their name

### Adding a Team Member
1. Click the "+" button in the top right corner
2. Fill in the required information:
   - First Name
   - Last Name
   - Email
   - Phone Number (automatically formatted)
   - Role (Regular/Admin)
3. Click "Save" to add the member or "Cancel" to discard

### Editing a Team Member
1. Click on any team member in the list
2. Modify their information as needed
3. Click "Save" to update or "Cancel" to discard changes
4. Click "Delete" to remove the team member


## Project Structure
```bash
my-project/
├── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   └── __init__.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├── requirements.txt
└── setup.py
```

## Technical Details

- Built with Django web framework
- Uses SQLite database
- Client-side phone number formatting with JavaScript
- Responsive CSS styling
- Form validation for required fields


## Testing

The application includes comprehensive tests covering all major functionality. To run the tests:
```bash
python manage.py test
```
The test suite includes:
- Member list view testing
- Member creation testing
- Member editing testing
- Member deletion testing
- Phone number format validation
- Required fields validation

### Test Coverage

The tests cover:
1. **View Testing**
   - Member list page loads correctly
   - Members are displayed with correct information
   - Add member form works properly
   - Edit member form works properly
   - Delete functionality works as expected

2. **Data Validation**
   - Phone number format validation
   - Required fields validation
   - Email format validation

3. **Model Testing**
   - Member creation
   - Member updates
   - Member deletion

### Running Specific Tests

To run a specific test case:
```bash
python manage.py test
fullStackTeam.tests.TeamMemberTests.test_member_list_view
```
To run tests with more detailed output:
```bash
python manage.py test -v 2
```

### Test Database

Tests use a separate test database, so your development database won't be affected by running tests.
