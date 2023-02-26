from notebook import Notebook
import sys


class NoteApp:
    def __init__(self):
        self.notebook = Notebook()

    def run(self):
        while True:
            command = input("Enter a command (new, edit, delete, view, list, search, sort, tag, export, quit): ")
            if command == "new":
                title = input("Enter the note title (or type 'cancel' to cancel): ")
                if title.lower() == "cancel":
                    continue
                content = input("Enter the note content (or type 'cancel' to cancel): ")
                if content.lower() == "cancel":
                    continue
                self.notebook.new_note(title, content)
                print("\033[92mNote created.\033[0m")
            elif command == "edit":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found. Create some using the [new] command.\033[0m")
                    continue
                index = input("Enter the index of the note you want to edit (or type 'cancel' to cancel): ")
                if index.lower() == "cancel":
                    continue
                try:
                    index = int(index)
                    note = notes[index]
                except (ValueError, IndexError):
                    print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
                    continue
                new_title = input("Enter the new title of the note (or type 'cancel' to cancel): ")
                if new_title.lower() == "cancel":
                    continue
                new_content = input("Enter the new content of the note (or type 'cancel' to cancel): ")
                if new_content.lower() == "cancel":
                    continue
                self.notebook.edit_note_title(index, new_title)
                self.notebook.edit_note_content(index, new_content)
                print("\033[92mNote updated.\033[0m")
            elif command == "delete":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found. Create some using the [new] command.\033[0m")
                    continue
                index = input("Enter the index of the note you want to delete (or type 'cancel' to cancel): ")
                if index.lower() == "cancel":
                    continue
                try:
                    index = int(index)
                    note = notes[index]
                except (ValueError, IndexError):
                    print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
                    continue
                confirm = input(f"Are you sure you want to delete the note '{note.title}'? (y/n): ")
                if confirm.lower() == "y":
                    self.notebook.delete_note(index)
                    print("\033[92mNote deleted.\033[0m")
                else:
                    print("\033[91mDeletion cancelled.\033[0m")
            elif command == "view":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found. Create some using the [new] command.\033[0m")
                    continue
                index = input("Enter the index of the note you want to view (or type 'cancel' to cancel): ")
                if index.lower() == "cancel":
                    continue
                try:
                    index = int(index)
                    note = notes[index]
                except (ValueError, IndexError):
                    print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
                    continue
                print(f"\033[1m{note.title}\033[0m\n\n{note.content}")
            elif command == "list":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found.\033[0m")
                    continue
                for i, note in enumerate(notes):
                    print(f"\033[1m{i}\033[0m: {note.title}")
            elif command == "search":
                query = input("Enter a search query: ")
                notes = self.notebook.search_notes(query)
                if not notes:
                    print("\033[91mNo notes found.\033[0m")
                    continue
                for i, note in enumerate(notes):
                    print(f"\033[1m{i}\033[0m: {note.title}")
            elif command == "sort":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found.\033[0m")
                    continue
                sort_type = input("Enter sort type (title, date): ")
                if sort_type.lower() == "title":
                    sorted_notes = sorted(notes, key=lambda note: note.title)
                elif sort_type.lower() == "date":
                    sorted_notes = sorted(notes, key=lambda note: note.creation_date)
                else:
                    print("\033[91mInvalid sort type. Please enter 'title' or 'date'.\033[0m")
                    continue
                for i, note in enumerate(sorted_notes):
                    print(f"\033[1m{i}\033[0m: {note.title}")
            elif command == "tag":
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found.\033[0m")
                    continue
                index = input("Enter the index of the note you want to tag (or type 'cancel' to cancel): ")
                if index.lower() == "cancel":
                    continue
                try:
                    index = int(index)
                    note = notes[index]
                except (ValueError, IndexError):
                    print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
                    continue
                tags = input("Enter tags separated by commas (or type 'cancel' to cancel): ")
                if tags.lower() == "cancel":
                    continue
                tags = [tag.strip() for tag in tags.split(",")]
                self.notebook.add_tags(index, tags)
                print("\033[92mTags added.\033[0m")
            elif command == "export":
                filename = input("Enter the filename: ")
                notes = self.notebook.get_notes()
                if not notes:
                    print("\033[91mNo notes found.\033[0m")
                    continue
                self.notebook.export_to_file(filename)
                print(f"\033[92mNotes exported to '{filename}'.\033[0m")
            elif command == "quit":
                confirm = input("Are you sure you want to quit? Any unsaved changes will be lost. (y/n): ")
                if confirm.lower() == "y":
                    sys.exit(0)
                else:
                    continue
            else:
                print("\033[91mInvalid command. Please enter a valid command.\033[0m")

    def _print_notes(self, notes):
        for i, note in enumerate(notes):
            print(f"{i}. {note.title}")