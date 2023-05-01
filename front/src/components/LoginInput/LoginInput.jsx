import React from 'react'
import styled from "styled-components";
import {colors} from "../../utils/colors";


const StyledInput = styled.input`
  height: 50px;
  width: 400px;
  border: none;
  border-radius: 20px;
  background-color: ${colors.lightGray};
  
  transition: 0.5s;
  padding-left: 10px;
  
  color: gray;
  font-size: 20px;
  
  margin-top: 20px;
  box-shadow: 0 15px 5px -10px rgba(155, 155, 155, 1);
  
  :focus {
    outline: none;
    color: black;
    background-color: white;
    box-shadow: 0 15px 10px -10px rgba(155, 155, 155, 1);
  }
`




export const LoginInput = ({
  initialText,
  onChange = (e) => console.log(e.target.value),
    password=false
}) => {

  return(
      <StyledInput onInput={onChange} type={password ? 'password' : 'text'} placeholder={initialText}/>
  )
}