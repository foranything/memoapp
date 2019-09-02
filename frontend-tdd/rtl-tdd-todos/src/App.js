import React from 'react';
import TodoApp from './TodoApp'
import TodoItem from './TodoItem'
import DelayedToggle from './DelayedToggle';
import UserProfile from './UserProfile'
import './App.css';

function App() {
  
  return (
    <div>
      <UserProfile id={1}/>
      {/*<DelayedToggle />*/}
      {/*<TodoApp/>*/}
    </div>
  );
}

export default App;
