import React, {Component} from 'react';
import NoteList from './NoteList'
import NoteWriter from './NoteWriter'

class NoteApp extends Component {
  state ={
    notes : [
      {id: 1, username:'user1', title: 'title1', content: 'content1'},
      {id: 2, username:'user2', title: 'title2', content: 'content2'},
      {id: 3, username:'user3', title: 'title3', content: 'content3'},
    ]
  }
  // handleChange=(e)=>{
  //   const {notes} = this.state;
  //   // console.log(notes);
  //
  //   this.setState({notes:{id:1, username:'user0'}})
  //   // this.setState({
  //   //   [e.target.name]:e.target.value
  //   //   });
  // }
  
  render() {
    const {notes} = this.state;
    return (
      <div>
        <NoteWriter />
        <NoteList notes={notes}/>
      </div>
    );
  }
}
export default NoteApp;