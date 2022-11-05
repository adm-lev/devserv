import React from "react";


const NoteItem = ({note}) => {
    return (
        <ul class="note-item">
            <li>{note.project}</li>
            <li>{note.text}</li>
            <li>{note.dateCreated}</li>
            <li>{note.dateUpdated}</li>
            <li>{note.user}</li>
            <li>{note.isActive}</li>
        </ul>
    )
};

const NoteList = ({notes}) => {
    const clear_notes = []
    for (const i in notes.results){
        clear_notes.push(notes.results[i])
    }
    return (
        <div class="note-div">
            <ul class="note-list">
                <li>Project</li>
                <li>Text</li>
                <li>Date created</li>
                <li>Date updated</li>
                <li>Author</li>
                <li>Is active</li>               
            </ul>
            {clear_notes.map((note_) => <NoteItem note={note_}/>)}
        </div>    
    )
    
};

export default NoteList;