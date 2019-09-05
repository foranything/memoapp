import React, {Component} from 'react';

class NoteWriter extends Component {
  state = {
    title:'',
    content:'',
    password:'',
  };
  
  handleChange=(e)=>{
    this.setState({
        [e.target.name]:e.target.value,
      })
  };
  //
  // handleClick=()=>{
  //   const {save} = this.props;
  //   save(this.state);
  //   this.setState({
  //     title:'',
  //     content:'',
  //     password:'',
  //   })
  // };
  
  handleSubmit=(e)=>{
    const {save} = this.props;
    save(this.state);
    this.setState({
      title:'',
      content:'',
      password:'',
    })
    e.preventDefault();
  };
  
  render() {
    // console.log(this.state);
    const {title, content, password} = this.state;
    const {handleChange, handleSubmit} = this;
    
    return (
      <form className='NoteWriter' onSubmit={handleSubmit}>
        <input
          placeholder='제목을 입력하세요.'
          name='title'
          value={title}
          onChange={handleChange}
        />
        <input
          placeholder='내용을 입력하세요.'
          name='content'
          value={content}
          onChange={handleChange}
        />
        <input
          placeholder='비밀번호를 입력하세요.'
          type='password'
          name='password'
          value={password}
          onChange={handleChange}
        />
        <button type='submit'>
          등록
        </button>
      </form>
    );
  }
}
export default NoteWriter;