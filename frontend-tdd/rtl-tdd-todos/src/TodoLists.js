import React from 'react';
import TodoItem from './TodoItem';

const TodoLists = ({  todos, onToggle, onRemove  }) => {
  return (
    <ul data-testid="TodoList">
      {todos.map(todo => (
        <TodoItem
          todo={todo}
          key={todo.id}
          onToggle={onToggle}
          onRemove={onRemove} />
      ))}
    </ul>
  );
};
export default TodoLists;