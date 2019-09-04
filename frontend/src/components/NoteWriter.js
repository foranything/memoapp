import React, {Component} from 'react';

class NoteWriter extends Component {
  state = {
    title:'',
    content:'',
    username:'',
  }
  
  handleChange=(e)=>{
    this.setState({
      [e.target.name]:e.target.value
    });
  }
  
  handleClick=(e)=>{
    const {saveNote} = this.props;
    this.setState({
      title:'',
      content:'',
      username:'',
    })
  }
  
  render() {
    // const {title, content, username} = this.state;
    console.log(this.state);
    const {handleChange, handleClick} = this;
    return (
      <div className='NoteWriter'>
        <input
          placeholder='제목을 입력하세요.'
          name='title'
          onChange={handleChange}
        />
        <input
          placeholder='내용을 입력하세요.'
          name='content'
          onChange={handleChange}
        />
        <button type='submit' onClick={handleClick}>
          제출
        </button>
      </div>
    );
  }
}
export default NoteWriter;