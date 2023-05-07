import React from "react";
import { Header} from "../components/Header/header";
import {PageWrapper} from "../components/PageWrapper/pageWrapper";
import {NavLink} from "react-router-dom";
import {DashboardButton} from "../components/DashboardButton/dashboardButton";


export const DashboardPage = () => {
  return(
      <PageWrapper>
        <Header text={'Dashboard'} />
        <DashboardButton path={'/new-data'} prompt={'Dodaj dane'} />
        <DashboardButton path={'/browse-data'} prompt={'Przeglądaj dane'} />
      </PageWrapper>
  )
}