"""
IT Ticket Tracker
-----------------
A simple help-desk ticket system that runs in the terminal.
You can add a ticket, list all tickets, search by keyword,
and update a ticket's status. Tickets are saved to a JSON
file so they are still there the next time you run it.

Built by: Tamara Geffrard
Concepts used: functions, lists, dictionaries, JSON file storage,
               loops, user input, string methods
"""

import json
import os

DATA_FILE = "tickets.json"


def load_tickets():
    """Load tickets from the JSON file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tickets(tickets):
    """Save all tickets back to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tickets, file, indent=4)


def add_ticket(tickets):
    """Ask the user for ticket details and add a new ticket."""
    name = input("Requester name: ").strip()
    issue = input("Issue description: ").strip()
    if not name or not issue:
        print("A ticket needs both a name and an issue. Nothing was saved.")
        return
    priority = input("Priority (Low / Medium / High): ").strip().capitalize()
    if priority not in ("Low", "Medium", "High"):
        priority = "Medium"

    new_id = len(tickets) + 1
    ticket = {
        "id": new_id,
        "name": name,
        "issue": issue,
        "priority": priority,
        "status": "Open",
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print(f"Ticket #{new_id} created and saved.")


def show_ticket(ticket):
    """Print one ticket in a clean format."""
    print(
        f"#{ticket['id']} | {ticket['name']} | {ticket['priority']} | "
        f"{ticket['status']} | {ticket['issue']}"
    )


def list_tickets(tickets):
    """Print every ticket, or a message if there are none."""
    if not tickets:
        print("No tickets yet.")
        return
    for ticket in tickets:
        show_ticket(ticket)


def search_tickets(tickets):
    """Print tickets whose issue or name contains the search word."""
    word = input("Search word: ").strip().lower()
    found = [
        t for t in tickets
        if word in t["issue"].lower() or word in t["name"].lower()
    ]
    if found:
        for ticket in found:
            show_ticket(ticket)
    else:
        print("No tickets matched that word.")


def update_status(tickets):
    """Change one ticket's status from Open to Closed (or back)."""
    try:
        ticket_id = int(input("Ticket number to update: "))
    except ValueError:
        print("Please enter a number.")
        return

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            if ticket["status"] == "Open":
                ticket["status"] = "Closed"
            else:
                ticket["status"] = "Open"
            save_tickets(tickets)
            print(f"Ticket #{ticket_id} is now {ticket['status']}.")
            return
    print("I could not find that ticket number.")


def main():
    tickets = load_tickets()

    while True:
        print("\n--- IT TICKET TRACKER ---")
        print("1. Add a ticket")
        print("2. List all tickets")
        print("3. Search tickets")
        print("4. Open / close a ticket")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_ticket(tickets)
        elif choice == "2":
            list_tickets(tickets)
        elif choice == "3":
            search_tickets(tickets)
        elif choice == "4":
            update_status(tickets)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
