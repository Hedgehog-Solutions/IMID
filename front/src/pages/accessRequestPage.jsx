import React from "react";
import { PageWrapper} from "../components/PageWrapper/pageWrapper";
import { Header } from "../components/Header/header";
import {LoginInput} from "../components/LoginInput/LoginInput";
import {BlueButton} from "../components/BlueButton/blueButton";
import {Toast} from "../components/ToastNotifications/Toast";
import {Navigate} from "react-router-dom";


export const AccessRequestPage = () => {
  const [email, setEmail] = React.useState();
  const [toasts, setToasts] = React.useState([<div />]);

  const [logout, setLogout] = React.useState(false);

  const handleAccessRequest = () => {
    setToasts(<Toast text={'Wysłano zapytanie'} key={email} type={'info'}/>)
  }

  const handleLogout = () => {
    setLogout(true)
  }

  return(
      <PageWrapper toasts={toasts}
                   leftMenu={[
                     <BlueButton onClick={handleLogout} prompt={'Cofnij'} />
                   ]}>
        {logout && <Navigate exact to={"/"} />}
        <Header text={"Uzyskanie dostępu"} />
        <LoginInput initialText={'Adres e-mail'} onChange={e => setEmail(e.target.value)} />
        <BlueButton prompt={'Wyślij'} onClick={handleAccessRequest} />
      </PageWrapper>
  )
}