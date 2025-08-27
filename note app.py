import os

FILENAME = "notes.txt"

def load_notes():
    """Read saved notes from the file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_notes(notes):
    """Save notes to the file."""
    with open(FILENAME, "w") as file:
        for note in notes:
            file.write(note + "\n")

def show_notes(notes):
    """Display all notes."""
    if not notes:
        print("\nNo notes yet.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def main():
    notes = load_notes()

    while True:
        print("\n--- Notes App ---")
        print("1. View notes")
        print("2. Add a note")
        print("3. Delete a note")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_notes(notes)
        elif choice == "2":
            new_note = input("Write your note: ")
            notes.append(new_note)
            save_notes(notes)
            print(" Note saved!")
        elif choice == "3":
            show_notes(notes)
            try:
                num = int(input("Enter the note number to delete: "))
                if 0 < num <= len(notes):
                    deleted = notes.pop(num - 1)
                    save_notes(notes)
                    print(f"🗑 Deleted: {deleted}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
