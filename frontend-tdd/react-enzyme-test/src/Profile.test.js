import React from 'react';
import {mount} from 'enzyme';
import Profile from './Profile';

describe('<Profile />', ()=>{
  it('atches snapshot', ()=>{
    const wrapper = mount(<Profile username="velopert" name="김민준" />);
    expect(wrapper).toMatchSnapshot();
  });
  
  it('renders username and name', () => {
    const wrapper = mount(<Profile username="velopert" name="김민준" />);
    
    // Props 접
    expect(wrapper.props().username).toBe('velopert');
    expect(wrapper.props().name).toBe('김민준');
  
    // DOM 확인
    const boldElement = wrapper.find('b');
    expect(boldElement.contains('velopert')).toBe(true);
    const spanElement = wrapper.find('span');
    expect(spanElement.text()).toBe('(김민준)');

  // find 함수를 사용하면 특정 DOM을 선택할 수 있습니다. 여기에 입력하는 값은 브라우저의 querySelector와 같습니다.
  // CSS 클래스는 find('.my-class'), id는 find('#myid'), 태그는 find('span') 이런식으로 조회를 할 수 있으며,
  // 여기에 컴포넌트의 Display Name 을 사용하면 특정 컴포넌트의 인스턴스도 찾을 수 있습니다. (예: find('MyComponent'))
  
  });
});