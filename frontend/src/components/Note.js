import React, {Component} from 'react';
import "./Note.css"

class Note extends Component {
  render() {
    const {username, title, content} = this.props;
    return (
      <div className='Note col s12 m4 l3'>
        <div className='DeleteBtn'>
        </div>
        <div className='card yellow lighten-4'>
          <div className='card-content black-text'>
            <span className='card-title'>{title}</span>
            <p>{content}</p>
            <p>{username}</p>
          </div>
        </div>
      </div>
    );
  }
}

export default Note;

// {/*<div>*/}
// {/*Note*/}
// {/*<span> {index}</span>*/}
// {/*<span> {username} </span>*/}
// {/*<span> {title} </span>*/}
// {/*<span> {content} </span>*/}
// {/*</div>*/}