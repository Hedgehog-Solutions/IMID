import React from "react";
import styled from "styled-components";
import {colors} from "../../utils/colors";
import { P3 } from "../../utils/typography";

const Container = styled.div`
  
  display: flex;
  flex-direction: row;
  width: 100vw;
  height: 100vh;
  justify-content: space-evenly;
  
  .bar{
    background-color: ${colors.darkBlue};
    height: 100%;
    width: 15%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
  }
  
  .left{
    margin-left: 0;
  }
  
  .right{
    margin-right: 0;
  }
  
  .content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
`

export const PageWrapper = ({children}) => {
  return(
      <Container>
        <div className={'bar'} />
        <div className={'content'}>
          {children}
        </div>
        <div className={'bar'} >
          <P3 style={{color: colors.lightGray}}>
            2023 IMID x Hedgehog
          </P3>
        </div>
      </Container>
  )
}