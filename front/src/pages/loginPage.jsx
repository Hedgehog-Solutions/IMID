import React from "react";
import styled from "styled-components";
import { Header } from "../components/Header/header";

import { PageWrapper } from "../components/PageWrapper/pageWrapper";
import {LoginInput} from "../components/LoginInput/LoginInput";
import {handleLogin, handleTrueLogin} from "../api/authApi";
import {BlueButton} from "../components/BlueButton/blueButton";
import {Redirect, Navigate, NavLink} from "react-router-dom";
import {P3} from "../utils/typography";
import {Toast} from "../components/ToastNotifications/Toast";
import {testDupa} from "../api/testApi";


export const LoginPage = () => {
  const [login, setLogin] = React.useState('a');
  const [password, setPassword] = React.useState('b');

  const [logged, setLogged] = React.useState(false)
  const [toasts, setToasts] = React.useState([<div />]);

  const handleLoginAttempt = () => {
    const result = handleLogin(login, password);

    handleTrueLogin(login, password).then(() => testDupa((e) => console.log(e)));



    if (result) {
      setLogged(true);
    }
    else {
      setToasts(<Toast text={'błędne dane logowania!'} key={login + password} type={'error'}/>)
    }
  }
  return (
      <PageWrapper toasts={toasts}>
        <Header text={'Witaj!'} fade={true} />
        <LoginInput initialText={'login'} onChange={e => setLogin(e.target.value)}/>
        <LoginInput password={true} initialText={'hasło'} onChange={e => setPassword(e.target.value)}/>
        <BlueButton prompt={"Zaloguj"} onClick={handleLoginAttempt} />
        {logged && <Navigate to={"/dashboard"} />}
        <NavLink to={"/access-request"}>
          <P3 style={{marginTop: 50, color: 'black'}}>
            Poproś o dostęp
          </P3>
        </NavLink>
      </PageWrapper>
  )
}