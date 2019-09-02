import React from 'react';
import { shallow } from 'enzyme';
import Counter from './Counter';


describe('<Counter />', () => {
  // 여기서는 mount 대신에 shallow 함수를 썼는데
  // shallow 함수는 컴포넌트 내부에 또 다른 리액트 컴포넌트가 있을 때
  // 이를 렌더링하지않음
  
  // 1. 클래스형 컴포넌트의 테스팅
  it('matches snapshot', () => {
    const wrapper = shallow(<Counter />);
    expect(wrapper).toMatchSnapshot();
  });
  
  it('has initial number', () => {
    const wrapper = shallow(<Counter />);
    expect(wrapper.state().number).toBe(0);
  });
  
  it('increases', () => {
    const wrapper = shallow(<Counter />);
    wrapper.instance().handleIncrease();
    expect(wrapper.state().number).toBe(1);
  });
  
  it('decreases', () => {
    const wrapper = shallow(<Counter />);
    wrapper.instance().handleDecrease();
    expect(wrapper.state().number).toBe(-1);
  });
  
  // 2. DOM 이벤트 시뮬레이트
  it('calls handleIncrease', () => {
    // 클릭이벤트를 시뮬레이트하고, state 를 확인
    const wrapper = shallow(<Counter />);
    const plusButton = wrapper.findWhere(
      node => node.type() === 'button' && node.text() === '+1'
    );
    plusButton.simulate('click');
    expect(wrapper.state().number).toBe(1);
  });
  
  it('calls handleDecrease', () => {
    // 클릭 이벤트를 시뮬레이트하고, h2 태그의 텍스트 확인
    const wrapper = shallow(<Counter />);
    const minusButton1 = wrapper.findWhere(
      node => node.type() === 'button' && node.text() === '-1'
    );
    minusButton1.simulate('click');
    const buttons = wrapper.find('button');
    // const plusButton = buttons.get(0); // 첫번째 버튼 +1
    const minusButton2 = buttons.at(1); // 두번째 버튼 -1
    minusButton2.simulate('click');
    const number = wrapper.find('h2');
    expect(number.text()).toBe('-2');
  });
});