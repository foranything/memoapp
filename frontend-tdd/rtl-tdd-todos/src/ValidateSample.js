import React, {Component} from 'react';

class ValidateSample extends Component {
  state = {
    password: '',
    clicked: false,
    validated: false,
  }
  // input = React.createRef();
  handleChange = (e) => {
    this.setState({
      password: e.target.value
    });
  }
  handleButtonClick = () => {
    this.setState({
      clicked: true,
      validated: this.state.password === '0000'
    });
    this.input.focus();
  }
  render() {
    return (
      <div>
        <input
          // ref = {this.input}
          ref = {(ref) => this.input=ref}
          type="password"
          value = {this.state.password}
          onChange={this.handleChange}
          className = {this.state.clicked ? (this.state.validated ? 'success' : 'failure') : ''}
          />
        <button onClick={this.handleButtonClick}>검증하기</button>
        {(this.state.validated ? 'success' : 'failure')}
      </div>
    );
  }
}

export default ValidateSample;