import React from 'react';
import TodoLists from './TodoLists';
import { render, fireEvent } from '@testing-library/react';

describe('<TodoLists />', () => {
  const sampleTodos = [
    {
      id: 1,
      text: 'TDD 배우기',
      done: true
    },
    {
      id: 2,
      text: 'react-testing-library 사용하기',
      done: true
    }
  ];
  
  it('renders todos properly', () => {
    const { getByText } = render(<TodoLists todos={sampleTodos} />);
    getByText(sampleTodos[0].text);
    getByText(sampleTodos[1].text);
  });
  
  it('calls onToggle and onRemove', () => {
    const onToggle = jest.fn();
    const onRemove = jest.fn();
    const { getByText, getAllByText } = render(
      <TodoLists todos={sampleTodos} onToggle={onToggle} onRemove={onRemove} />
    );
    
    fireEvent.click(getByText(sampleTodos[0].text));
    expect(onToggle).toBeCalledWith(sampleTodos[0].id);
    
    fireEvent.click(getAllByText('삭제')[0]); // 첫번째 삭제 버튼을 클릭
    expect(onRemove).toBeCalledWith(sampleTodos[0].id);
  });
});