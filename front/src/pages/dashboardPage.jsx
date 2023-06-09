import React from "react";
import { Header} from "../components/Header/header";
import {PageWrapper} from "../components/PageWrapper/pageWrapper";
import {Navigate, NavLink} from "react-router-dom";
import {DashboardButton} from "../components/DashboardButton/dashboardButton";
import {testDupa, testHello} from "../api/testApi";

import axios from "axios";
import {handleTrueLogout} from "../api/authApi";
import {BlueButton} from "../components/BlueButton/blueButton";


export const DashboardPage = () => {

  const [headerText, setHeaderText] = React.useState('Witaj!');

  const [logout, setLogout] = React.useState(false);

  const handleLogout = () => {
    handleTrueLogout().then();

    setLogout(true);
  }

  React.useEffect(() => {
    testHello(setHeaderText).then();
  })

  return(
      <PageWrapper
        leftMenu={[
            <BlueButton onClick={handleLogout} prompt={'Wyloguj'} />
        ]}
      >
        {logout && <Navigate exact to={"/"} />}
        <Header text={headerText} />
        <DashboardButton path={'/new-data'} prompt={'Dodaj dane'} />
        <DashboardButton path={'/browse-data'} prompt={'Przeglądaj dane'} />
      </PageWrapper>
  )
}