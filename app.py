import csv
from datetime import datetime


while True:
    print("Event & Meeting Manager")
    print("-----------------------")
    print("1. Register a guest")
    print("2. View guests")
    print("3. Schedule a meeting")
    print("4. View meetings")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":

        name = input("Guest name: ").strip()
        email = input("Guest email: ").strip()
        language = input("Preferred language: ").strip()

        if not name or not email or not language:
            print("All guest fields are required. Guest was not saved.")
            continue
        if email.count("@") != 1 or " " in email:
            print("Please enter an email like alex@example.com.")
            continue

        local_part, domain = email.split("@")

        if not local_part or "." not in domain or domain.startswith(".") or domain.endswith("."):
            print("Please enter an email like alex@example.com.")
            continue

        duplicate = False

        try:
            with open("guests.csv", "r", newline="", encoding="utf-8") as file:
                for guest in csv.reader(file):
                    if len(guest) == 3 and guest[1].strip().lower() == email.lower():
                        duplicate = True
                        break
        except FileNotFoundError:
            pass

        if duplicate:
            print("A guest with this email is already registered.")
            continue
        with open("guests.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, language])

        print("Guest saved to guests.csv!")
    elif choice == "2":
        try:
            with open("guests.csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                print("\nRegistered guests:")

                for guest in reader:
                    if len(guest) == 3:
                        print(f"Name: {guest[0]} | Email: {guest[1]} | Language: {guest[2]}")

        except FileNotFoundError:
            print("No guests registered yet.")
    elif choice == "3":
        guest_email = input("Guest email: ").strip().lower()
        registered = False

        try:
            with open("guests.csv", "r", newline="", encoding="utf-8") as file:
                for guest in csv.reader(file):
                    if len(guest) == 3 and guest[1].strip().lower() == guest_email:
                        registered = True
                        break
        except FileNotFoundError:
            pass

        if not registered:
            print("Guest not found. Register the guest using option 1 first.")
            continue
        representative = input("Representative name: ").strip()
        room = input("Meeting room: ").strip()
        date = input("Meeting date (YYYY-MM-DD): ").strip()
        start_time = input("Start time (HH:MM, 24-hour): ").strip()
        end_time = input("End time (HH:MM, 24-hour): ").strip()
        if not representative or not room:
            print("Representative and room are required. Meeting was not saved.")
            continue

        try:
            start = datetime.strptime(date + " " + start_time, "%Y-%m-%d %H:%M")
            end = datetime.strptime(date + " " + end_time, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date or time. Use YYYY-MM-DD and HH:MM.")
            continue

        if end <= start:
            print("End time must be after start time.")
            continue

        conflict = False

        try:
            with open("meetings.csv", "r", newline="", encoding="utf-8") as file:
                for meeting in csv.reader(file):
                    if len(meeting) != 6:
                        continue

                    existing_start = datetime.strptime(
                        meeting[3] + " " + meeting[4], "%Y-%m-%d %H:%M"
                    )
                    existing_end = datetime.strptime(
                        meeting[3] + " " + meeting[5], "%Y-%m-%d %H:%M"
                    )

                    overlaps = start < existing_end and end > existing_start
                    same_guest = guest_email == meeting[0].strip().lower()
                    same_rep = representative.lower() == meeting[1].strip().lower()
                    same_room = room.lower() == meeting[2].strip().lower()

                    if overlaps and (same_guest or same_rep or same_room):
                        conflict = True
                        break
        except FileNotFoundError:
            pass
        except ValueError:
            print("A saved meeting has an invalid date or time. Check meetings.csv.")
            continue

        if conflict:
            print("Scheduling conflict: guest, representative, or room is busy.")
            continue
        with open("meetings.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                guest_email,
                representative,
                room,
                date,
                start_time,
                end_time
            ])

        print("Meeting saved to meetings.csv!")
    elif choice == "4":
        try:
            with open("meetings.csv", "r", newline="", encoding="utf-8") as file:
                meetings = [
                    row for row in csv.reader(file)
                    if len(row) == 6
                ]

            meetings.sort(
                key=lambda meeting: datetime.strptime(
                    meeting[3] + " " + meeting[4],
                    "%Y-%m-%d %H:%M"
                )
            )

            if not meetings:
                print("No meetings scheduled yet.")
            else:
                print("\nScheduled meetings:")

                for meeting in meetings:
                    print("-----------------------")
                    print("Guest email:", meeting[0])
                    print("Representative:", meeting[1])
                    print("Room:", meeting[2])
                    print("Date:", meeting[3])
                    print("Time:", meeting[4], "-", meeting[5])

        except FileNotFoundError:
            print("No meetings scheduled yet.")
        except ValueError:
            print("A saved meeting has an invalid date or time. Check meetings.csv.")
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")