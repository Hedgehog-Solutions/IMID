import React from "react";
import styled from "styled-components";
import {colors} from "../../utils/colors";
import { P3 } from "../../utils/typography";
import {Toast} from "../ToastNotifications/Toast";

const Container = styled.div`
  
  display: flex;
  flex-direction: row;
  width: 100vw;
  height: 100vh;
  justify-content: space-evenly;
  
  .bar{
    background-color: ${colors.darkBlue};
    height: 100%;
    width: 20%;

  }
  
  .left{
    margin-left: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .right{
    margin-right: 0;
    display: flex;
    flex-direction: column-reverse;
    justify-content: space-between;
    align-items: center;
  }
  
  .content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
`

export const PageWrapper = ({children, toasts, leftMenu = []}) => {
  return(
      <Container>
        <div className={'bar left'} >
          {leftMenu}
        </div>
        <div className={'content'}>
          {children}
        </div>
        <div className={'bar right'} >

          <P3 style={{color: colors.lightGray}}>
            2023 IMID x Hedgehog
          </P3>
          {toasts !== undefined && toasts}
        </div>
      </Container>
  )
}