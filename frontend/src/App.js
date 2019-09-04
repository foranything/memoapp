import React, {Component} from 'react';
import NoteApp from './components/NoteApp'
import "./App.css"

class App extends Component {
  render() {
    return (
      <div className="row">
        <NoteApp />
      </div>
    );
  }
}
export default App;