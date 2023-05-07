import React from "react";
import styled from "styled-components";
import {P3, P2} from "../../utils/typography";


const StyledToast = styled.div`
  width: 90%;
  height: 60px;
  border: none;
  border-radius: 20px;
  
  transition: 0.5s;
  
  background-color: red;
  
  text-align: center;
  
  padding: 3px;
  
  margin-top: 10px;
  
  align-items: center;
  
  display: flex;
  flex-direction: column;
  
  justify-content: space-evenly;
`

const StyledToastBox = styled.div`
  width: 100%;
  height: 50%;
  
`

const toastColors = {
  'error': 'red',
  'success': 'lightGreen',
  'warn': 'yellow',
  'info': 'lightBlue'
}

const toastTitles = {
  'error': 'Błąd!',
  'success': 'Sukces!',
  'warn': 'Uwaga!',
  'info': ''
}

export const Toast = ({ type = 'error', text = '' }) => {

  const [currentState, setCurrentState] = React.useState('before');

  React.useEffect(() => {
    if (currentState === 'before') {
      setCurrentState('during')
    }
    else if (currentState === 'during') {
      setTimeout( () => setCurrentState('closing'), 1000)
    }
    else if (currentState === 'closing') {
      setTimeout(() => setCurrentState('closed'), 500)
    }
  })

  return(
      <>
        {currentState !== 'closed' &&
          <StyledToast style={{opacity: currentState === 'during' ? 1 : 0, backgroundColor: `${toastColors[type]}`}}>
            <P2 style={{margin: 0}}>
              {toastTitles[type]}
            </P2>
            <P3 style={{margin: 0}}>
              {text}
            </P3>
          </StyledToast>
        }
      </>
  )
}


export const ToastBox = () => {


}
