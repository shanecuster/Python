#!/usr/bin/python3

from datetime import datetime, timedelta

def save_event(event, date):
    with open('events.txt', 'a') as file:
        file.write(f'{event},{date}\n')

def load_events():
    try:
        with open('events.txt', 'r') as file:
            events = [line.strip().split(',') for line in file.readlines()]
        return events
    except FileNotFoundError:
        return []

def calculate_days_until(event_date):
    today = datetime.now().date()
    event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
    days_until = (event_date - today).days
    return max(days_until, 0)

def main():
    while True:
        print("\n1. Add new event\n2. View events\n3. Quit")
        choice = input("Enter your choice (1/2/3): \n")

        if choice == '1':
            event_name = input("Enter the name of the event: ")
            event_date = input("Enter the date of the event (YYYY-MM-DD): ")
            save_event(event_name, event_date)
            print("Event added successfully!")

        elif choice == '2':
            events = load_events()
            if not events:
                print("No events found.")
            else:
                events.sort(key=lambda x: calculate_days_until(x[1]))
                for event in events:
                    event_name, event_date = event
                    days_until = calculate_days_until(event_date)
                    print(f"{event_name} - Date: {event_date}, Days until: {days_until}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

