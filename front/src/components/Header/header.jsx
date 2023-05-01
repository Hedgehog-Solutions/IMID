import React from "react";
import { H1 } from "../../utils/typography";

export const Header = ({text='Witaj!', fade=false}) => {
  const [visible, setVisible] = React.useState(!fade);

  React.useEffect(() => {
    !visible && setTimeout(() => setVisible(true), 200);
  }, [visible]);

  return (
      <H1 style={visible ? {opacity: 1} : {opacity: 0}}>
        {text}
      </H1>
  )
}