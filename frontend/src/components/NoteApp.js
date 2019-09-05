import React, {Component} from 'react';
import NoteList from './NoteList'
import NoteWriter from './NoteWriter'
import * as service from "../services/noteAPI";

class NoteApp extends Component {
  state ={
    fetching: false,
    notes : [
      {id: 1, title: 'title1', content: 'content1', password:'password1'},
      {id: 2, title: 'title2', content: 'content2', password:'password2'},
      {id: 3, title: 'title3', content: 'content3', password:'password3'},
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
      const receivedNotes = info[0].data;
      receivedNotes.reverse();
      // console.log(receivedNotes);
      // console.log(notes);
      if (receivedNotes.length < 4){
        receivedNotes.map((note, index) => {
          notes[index].id=index;
          notes[index].title=note.title;
          notes[index].content=note.content;
          notes[index].password=note.password;
        });
      }
      else {
        this.setState({
          fetching: false, // done!
          notes:receivedNotes,
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
    const { notes } = this.state;
    this.setState({
      fetching: true // requesting..
    });
    try {
      const info = await Promise.all([service.postNote(newNote)]);
      // console.log(info[0].data[0]);
      const postedNotes = info[0].data;
      postedNotes.reverse();
      // if (receivedNotes.length < 4){
      //   receivedNotes.map((receivedNote, index) => notes[index]=receivedNote);
      // }
      // else {
      //   this.setState({
      //     fetching: false, // done!
      //     // notes:receivedNotes,
      //     notes:[
      //       ...receivedNotes,
      //     ]
      //   });
      // }
      this.setState({
        fetching: false, // done!
        // notes: postedNotes,
        notes:[
          ...notes,
          ...postedNotes,
        ]
      });
    } catch (e) {
      // if err, stop at this point
      this.setState({
        fetching: false
      });
    }
  };
  
  render() {
    const {notes} = this.state;
    // console.log(notes);
    return (
      <div>
        <NoteWriter save={this.save}/>
        <NoteList   notes ={notes}/>
      </div>
    );
  }
}
export default NoteApp;