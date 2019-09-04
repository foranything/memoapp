import React, {Component} from 'react';
import Note from './Note'

class NoteList extends Component {
  render() {
    const {notes} = this.props;
    return (
      <div className='NoteList'>
        {notes.map((note, index) =>
          <Note index={index} username={note.username} title={note.title} content={note.content} key={note.id}/>)}
      </div>
    );
  }
}

export default NoteList;

// {/*{notes.map(()=>(<Note/>))}*/}
// {/*notes.map(note=><Note note={note}/>)*/}