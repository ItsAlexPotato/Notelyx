from note import Note

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, title, content):
        self.notes.append(Note(title, content))

    def edit_note_title(self, index, new_title):
        self.notes[index].title = new_title

    def edit_note_content(self, index, new_content):
        self.notes[index].content = new_content

    def delete_note(self, index):
        del self.notes[index]

    def get_notes(self):
        return self.notes

    def modify_note(self, index, title=None, content=None, tags=None):
        try:
            note = self.notes[index]
        except IndexError:
            print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
            return

        if title is not None:
            note.title = title
        if content is not None:
            note.content = content
        if tags is not None:
            note.tags = tags

        print("\033[92mNote modified.\033[0m")

    def search_notes(self, query):
        return [note for note in self.notes if note.match(query)]

    def add_tags(self, index, tags):
        try:
            note = self.notes[index]
        except IndexError:
            print("\033[91mInvalid index. Please enter a valid index number.\033[0m")
            return

        note.tags.extend(tags)

    def export_to_file(self, filename, notes_to_export=None):
        if notes_to_export is None:
            notes_to_export = self.notes
        with open(filename, "w") as f:
            for note in notes_to_export:
                f.write(f"{note.title}\n")
                f.write(f"{note.creation_date}\n")
                f.write(f"{note.tags}\n")
                f.write(f"{note.content}\n")
                f.write("===\n")
