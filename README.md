# Event Registration & Meeting Manager

A Python command-line application for registering event guests and scheduling meetings. Inspired by my experience handling registration and client services at South Florida boat shows.

## Features

- Register guests with their name, email, and preferred language.
- Reject blank guest details and common email formatting errors.
- Prevent duplicate registrations using case-insensitive email comparisons.
- Schedule meetings for registered guests.
- Validate meeting dates and require the end time to follow the start time.
- Prevent overlapping bookings for the same guest, representative, or room.
- Allow back-to-back meetings.
- Display meetings in date and start-time order.
- Save guest and meeting records locally in CSV files.

## Technologies

- Python
- csv module for reading and writing records
- datetime module for date and time validation

No third-party packages are required.

## How to Run

With Python 3 installed, open a terminal in the project folder and run:

```bash
python3 app.py
```

Use the numbered menu to register guests, view guests, schedule meetings, or view meetings. Choose option 5 to exit.

Enter dates as YYYY-MM-DD and times as HH:MM using the 24-hour clock.

## Data Storage

The application creates guests.csv and meetings.csv when records are first saved. Run it from the project folder so it can find these files consistently.

Both data files are excluded from Git through .gitignore.

## Manual Testing

Checked the following scenarios during development:

- Valid guest registration and saved guest retrieval
- Blank guest fields and invalid email formats
- Duplicate email registration
- Scheduling for an unregistered guest
- Invalid dates and end times
- Overlapping room, representative, and guest bookings
- Back-to-back meetings
- Chronological display of meetings entered out of order
- Repeating menu, invalid menu choices, and exit