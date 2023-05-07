import React from "react";
import styled from "styled-components";
import {PageWrapper} from "../components/PageWrapper/pageWrapper";
import {DataTable} from "../components/DataTable/DataTable";
import {Toast} from "../components/ToastNotifications/Toast";
import {BlueButton} from "../components/BlueButton/blueButton";
import {Navigate} from "react-router-dom";

import { makeWord } from "../utils/mockData";

export const BrowseDataPage = () => {

  const [toasts, setToasts] = React.useState([<div />]);

  const [navToImport, setNavToImport] = React.useState(false);

  const handleDataExport = () => {
    setToasts(<Toast text={'Udało się wyeksportować dane!'} key={makeWord(5)} type={'success'}/>)
  }

  const handleDataImport = () => {
    setNavToImport(true)
  }
  return(
      <PageWrapper
          toasts={toasts}
          leftMenu={[
              <BlueButton onClick={handleDataExport} prompt={'eksportuj'}/>,
              <BlueButton onClick={handleDataImport} prompt={'importuj'}/>
          ]}
      >
        <DataTable />
        {navToImport && <Navigate to={'/new-data'}/>}
      </PageWrapper>
  )
}