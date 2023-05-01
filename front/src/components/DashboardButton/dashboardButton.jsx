import React from "react";
import styled from "styled-components";
import {NavLink} from "react-router-dom";
import {Header} from "../Header/header";

const StyledDiv = styled.div`
  width: 100%;
  height: 100%;
  
  padding-left: 30px;
  align-items: center;
  justify-content: flex-start;
  display: flex;
  transition: 0.5s;
  
  :hover{
    padding-left: 45px;
  }
`

export const DashboardButton = ({path, prompt}) => {
  return(
      <NavLink to={path} style={{width: '100%', height: 150, textDecoration: "none", color: "black"}}>
        <StyledDiv >
          <Header text={prompt} />
        </StyledDiv>
      </NavLink>
  )
}