import React from "react";
import { PageWrapper} from "../components/PageWrapper/pageWrapper";
import { Header } from "../components/Header/header";
import {LoginInput} from "../components/LoginInput/LoginInput";
import {BlueButton} from "../components/BlueButton/blueButton";
import {Toast} from "../components/ToastNotifications/Toast";


export const AccessRequestPage = () => {
  const [email, setEmail] = React.useState();
  const [toasts, setToasts] = React.useState([<div />]);

  const handleAccessRequest = () => {
    setToasts(<Toast text={'Wysłano zapytanie'} key={email} type={'info'}/>)
  }

  return(
      <PageWrapper toasts={toasts}>
        <Header text={"Uzyskanie dostępu"} />
        <LoginInput initialText={'Adres e-mail'} onChange={e => setEmail(e.target.value)} />
        <BlueButton prompt={'Wyślij'} onClick={handleAccessRequest} />
      </PageWrapper>
  )
}