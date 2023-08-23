import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo  # Content
        self.tags = tags  # title
        self.creation_date = datetime.date.today()  # timestamp
        global last_id
        last_id += 1
        self.id = last_id  # id

    def match(self, filter):  # search
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags."""

        return filter in self.memo or filter in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):  # empty list of note
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    # l=[1,2,3,4,5,6]
    # l=[note1,note2,note3,....]
    def new_note(self, memo, tags=''):  # add note
        '''Create a new note and add it to the list.'''
        # n1=Note(memo, tags)
        note = Note(memo, tags)
        self.notes.append(note)

    def modify_memo(self, note_id, memo):  # modify content
        '''Find the note with the given id and change its
        memo to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):  # modify tag
        '''Find the note with the given id and change its
        tags to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):  # search for specifc not
        '''Find all notes that match the given filter
        string.'''
        # l=[note1,note2,note3,....]
        return [note for note in self.notes if
                note.match(filter)]
#
