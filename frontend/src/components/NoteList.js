import React, {Component} from 'react';
import Note from './Note'

class NoteList extends Component {
  render() {
    const {notes} = this.props;
    return (
      <div className='NoteList'>
        {notes.reverse().map((note, index) =>
          <Note username={note.username} title={note.title} content={note.content} key={index}/>)}
      </div>
    );
  }
}

export default NoteList;

// {/*{notes.map(()=>(<Note/>))}*/}
// {/*notes.map(note=><Note note={note}/>)*/}