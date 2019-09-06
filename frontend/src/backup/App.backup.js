import React, { Component } from "react";
import * as service from "./services/noteAPI";
import WritingBackup from "./Writing.backup";
import NoteBackup from "./Note.backup";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fetching: false,
      savedNotes: [
        { id: 0, title: "title1", content: "default1" }
        // { id: 1, title: "title2", content: "default2" },
        // { id: 2, title: "title3", content: "default3" }
      ]
    };
  }
  componentDidMount() {
    this.fetchPostInfo(1);
  }

  fetchPostInfo = async postId => {
    this.setState({
      fetching: true // requesting..
    });
    try {
      const info = await Promise.all([service.getMemo()]);
      // console.log(info);
      info[0].data.map((data, index) => (this.state.savedNotes[index] = data));
      this.setState({
        fetching: false // done!
      });
    } catch (e) {
      // if err, stop at this point
      this.setState({
        fetching: false
      });
    }
  };

  save = writingState => {
    const { savedNotes } = this.state;
    const lastNoteId = savedNotes[savedNotes.length - 1].id;

    this.setState({
      savedNotes: [
        ...savedNotes,
        {
          id: lastNoteId + 1,
          title: writingState.title,
          content: writingState.content
        }
      ]
    });
  };

  delete = index => {
    console.log(`${index} will be deleted`);
    const { savedNotes } = this.state;
    savedNotes.splice(index, 1);
    this.setState({
      savedNotes: savedNotes
    });
  };

  render() {
    // console.log(this.state)
    return (
      <div>
        <WritingBackup save={this.save} />
        <div className="row">
          {this.state.savedNotes.map((note, index) => (
            <NoteBackup
              delete={this.delete}
              title={note.title}
              content={note.content}
              index={index}
              key={note.id}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default App;
