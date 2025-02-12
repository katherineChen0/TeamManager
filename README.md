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
fullStackTeam/
├── templates/
│ ├── all_members.html
│ ├── add.html
│ ├── edit.html
│ └── master.html
├── models.py
├── views.py
└── urls.py


## Technical Details

- Built with Django web framework
- Uses SQLite database
- Client-side phone number formatting with JavaScript
- Responsive CSS styling
- Form validation for required fields
