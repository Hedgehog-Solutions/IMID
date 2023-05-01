import React from "react";
import { PageWrapper} from "../components/PageWrapper/pageWrapper";
import { Header } from "../components/Header/header";
import {LoginInput} from "../components/LoginInput/LoginInput";
import {BlueButton} from "../components/BlueButton/blueButton";


export const AccessRequestPage = () => {
  const [email, setEmail] = React.useState();

  const handleAccessRequest = () => {
    console.log('request for email', email)
  }

  return(
      <PageWrapper>
        <Header text={"Uzyskanie dostępu"} />
        <LoginInput initialText={'Adres e-mail'} onChange={e => setEmail(e.target.value)} />
        <BlueButton prompt={'Wyślij'} onClick={handleAccessRequest} />
      </PageWrapper>
  )
}