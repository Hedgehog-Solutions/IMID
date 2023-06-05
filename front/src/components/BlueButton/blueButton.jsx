import React from "react";
import styled from "styled-components";
import {colors} from "../../utils/colors";
import {P3} from "../../utils/typography";
import {NavLink} from "react-router-dom";

const StyledBlueButton = styled.button`
  width: 100px;
  height: 30px;
  border: none;
  border-radius: 10px;
  background-color: ${colors.lightBlue};
  cursor: pointer;
  margin-top: 20px;
  opacity: 0.7;
  
  transition: 0.5s;
  
  :hover{
    color: black;
    opacity: 1;
  }
`

export const BlueButton = ({prompt, onClick}) => {

  return(
      <StyledBlueButton onClick={onClick}>
        <P3 style={{margin: 0, fontWeight: 400}}>
          {prompt}
        </P3>
      </StyledBlueButton>
  )
}

export const BlueNavLink = ({prompt, path}) => {
  return(
      <NavLink to={path} >
        <StyledBlueButton >
          <P3 style={{margin: 0, fontWeight: 400}}>
            {prompt}
          </P3>
        </StyledBlueButton>
      </NavLink>
  )
}