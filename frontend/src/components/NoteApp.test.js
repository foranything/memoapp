import React from 'react';
import NoteWriter from './NoteWriter';
import NoteList from './NoteList';
import Note from './Note';
import { render, fireEvent } from '@testing-library/react';
import "@testing-library/jest-dom/extend-expect";


describe('<Note />', () => {
  it('renders Note', () => {
    const utils = render(<Note index={1} username='김대운' title='제목' content='내용'/>);
    utils.getByText('김대운'); // Note 존재유무 확인
    expect(utils.container).toMatchSnapshot();
    utils.getByText('김대운'); // 김대운 라는 텍스트를 가진 엘리먼트가 있는지 확인
    utils.getByText('제목'); // 제목 라는 텍스트를 가진 엘리먼트가 있는지 확인
    utils.getByText('내용'); // 내용 라는 텍스트를 가진 엘리먼트가 있는지 확인
  
  });
});

describe('<NoteList />', () => {
  const sampleNotes = [
    {id: 1, username:'user1', title: 'title1', content: 'content1'},
    {id: 2, username:'user2', title: 'title2', content: 'content2'},
    {id: 3, username:'user3', title: 'title3', content: 'content3'},
  ]
  it('renders NoteList', () => {
    const utils = render(<NoteList notes={sampleNotes}/>);
    expect(utils.container).toMatchSnapshot();
    utils.getByText('user1'); // 김대운 라는 텍스트를 가진 엘리먼트가 있는지 확인
    utils.getByText('title1'); // 제목 라는 텍스트를 가진 엘리먼트가 있는지 확인
    utils.getByText('content1'); // 내용 라는 텍스트를 가진 엘리먼트가 있는지 확인
    // expect(utils.component.contains(<Note />)).toBe(true);
  });
});

describe('<NoteWriter />', () => {
  const save = jest.fn();
  it('renders NoteWriter', () => {
    
    // (1) UI 구성하기
    const utils = render(<NoteWriter save={save}/>);
    expect(utils.container).toMatchSnapshot();
    const input1 = utils.getByPlaceholderText('제목을 입력하세요.');
    const input2 = utils.getByPlaceholderText('내용을 입력하세요.');
    const input3 = utils.getByPlaceholderText('비밀번호를 입력하세요.');
    const btn = utils.getByText('등록');
    
    // (2) Input 상태 관리하기
    // 수정하고
    fireEvent.change(input1, {
      target: {
        value: '여기는제목'
      }
    });
    fireEvent.change(input2, {
      target: {
        value: '여기는내용'
      }
    });
    fireEvent.change(input3, {
      target: {
        value: '여기는비밀번호'
      }
    });
    expect(input1).toHaveAttribute('value', '여기는제목')
    expect(input2).toHaveAttribute('value', '여기는내용')
    expect(input3).toHaveAttribute('value', '여기는비밀번호')
    
    // (3) Submit 이벤트 관리하기
    // 버튼 클릭해서 리턴값 확인하기
    fireEvent.click(btn);
    expect(save).toBeCalledWith(
      {
        title:'여기는제목',
        content:'여기는내용',
        password:'여기는비밀번호'
      });
    expect(input1).toHaveAttribute('value', ''); // input1이 비워져야함
    expect(input2).toHaveAttribute('value', ''); // input2이 비워져야함
    expect(input3).toHaveAttribute('value', ''); // input3이 비워져야함
  });
});


// describe('<NoteWriter />', () => {
//   it('renders NoteList', () => {
//     const utils = render(<NoteWriter />);
//     expect(utils.container).toMatchSnapshot();
//     utils.getByText('user1'); // 김대운 라는 텍스트를 가진 엘리먼트가 있는지 확인
//     utils.getByText('title1'); // 제목 라는 텍스트를 가진 엘리먼트가 있는지 확인
//     utils.getByText('content1'); // 내용 라는 텍스트를 가진 엘리먼트가 있는지 확인
//   });
// });



//
// it('creates new todo', () => {
//   const { getByPlaceholderText, getByText } = render(<TodoApp />);
//   // 이벤트를 발생시켜서 새 항목을 추가하면
//   fireEvent.change(getByPlaceholderText('할 일을 입력하세요'), {
//     target: {
//       value: '새 항목 추가하기'
//     }
//   });
//   fireEvent.click(getByText('등록'));
//   // 해당 항목이 보여져야합니다.
//   getByText('새 항목 추가하기');
// });
//
// it('toggles todo', () => {
//   const { getByText } = render(<TodoApp />);
//   // TDD 배우기 항목에 클릭 이벤트를 발생시키고 text-decoration 속성이 설정되는지 확인
//   const todoText = getByText('TDD 배우기');
//   expect(todoText).toHaveStyle('text-decoration: line-through;');
//   fireEvent.click(todoText);
//   expect(todoText).not.toHaveStyle('text-decoration: line-through;');
//   fireEvent.click(todoText);
//   expect(todoText).toHaveStyle('text-decoration: line-through;');
// });
//
// it('removes todo', () => {
//   const { getByText } = render(<TodoApp />);
//   const todoText = getByText('TDD 배우기');
//   const removeButton = todoText.nextSibling;
//   fireEvent.click(removeButton);
//   expect(todoText).not.toBeInTheDocument(); // 페이지에서 사라졌음을 의미함
// });