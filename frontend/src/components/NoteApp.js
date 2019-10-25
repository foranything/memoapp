import React, { Component } from 'react';
import NoteList from './NoteList'
import NoteWriter from './NoteWriter'
import * as service from "../services/noteAPI";

class NoteApp extends Component {
  state = {
    fetching: false,
    notes: [
      { id: 1, title: 'title1', content: 'content1', password: 'password1' },
      { id: 2, title: 'title2', content: 'content2', password: 'password2' },
      { id: 3, title: 'title3', content: 'content3', password: 'password3' },
    ]
  };

  componentDidMount() {
    this.fetchNotes();
  }

  fetchNotes = async postId => {
    const { notes } = this.state;
    this.setState({
      fetching: true // requesting..
    });
    try {
      const info = await Promise.all([service.getNote()]);
      const savedNotes = info[0].data;
      if (savedNotes.length <= 3) {
        notes.map((note, index) => {
          notes[index].id = index;
          notes[index].title = savedNotes[index].title;
          notes[index].content = savedNotes[index].content;
          notes[index].password = savedNotes[index].password;
          return null
        });
      }
      else {
        this.setState({
          fetching: false, // done!
          notes: savedNotes,
        });
      }
      this.setState({
        fetching: false, // done!
        // notes:receivedNotes,
        // notes:[
        //   ...receivedNotes,
        // ]
      });
    } catch (e) {// if err, stop at this point
      this.setState({
        fetching: false
      });
    }
  };

  save = async newNote => {
    // const { notes } = this.state;
    await Promise.all([service.postNote(newNote)]);
    this.fetchNotes();
  };

  render() {
    const { notes } = this.state;
    // console.log(notes);
    return (
      <div>
        <NoteWriter save={this.save} />
        <NoteList notes={notes} />
      </div>
    );
  }
}
export default NoteApp;