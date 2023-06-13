import React from "react";
import styled from "styled-components";
import {PageWrapper} from "../components/PageWrapper/pageWrapper";
import {DataTable} from "../components/DataTable/DataTable";
import {Toast} from "../components/ToastNotifications/Toast";
import {BlueButton, BlueNavLink} from "../components/BlueButton/blueButton";
import {Navigate} from "react-router-dom";

import { makeWord } from "../utils/mockData";
import {DataTableFiltered} from "../components/DataTable/DataTableFiltered";
import {VersionSelect} from "../components/VersionSelect/VersionSelect";
import {getVersionsApi} from "../api/databaseApi";



export const BrowseDataPage = () => {

  const [toasts, setToasts] = React.useState([<div />]);

  const [navToImport, setNavToImport] = React.useState(false);

  const [currentVersion, setCurrentVersion] = React.useState('0');

  const [versions, setVersions] = React.useState([])

  const tableRef = React.useRef(null);

  const handleDataExport = () => {
    setToasts(<Toast text={'Udało się wyeksportować dane!'} key={makeWord(5)} type={'success'}/>)
    tableRef.current !== null && tableRef.current.download();

  }

  React.useEffect(() => {
    versions === [] && getVersionsApi(setVersions);
  })

  const handleVersionChange = (e) => {
    setCurrentVersion(e.target.value);
    tableRef.current !== null && tableRef.current.setData(e.target.value);
  }

  const handleDataImport = () => {
    setNavToImport(true)
  }
  return(
      <PageWrapper
          toasts={toasts}
          leftMenu={[
            <BlueButton onClick={handleDataExport} prompt={'eksportuj'}/>,
            <BlueButton onClick={handleDataImport} prompt={'importuj'}/>,
            <BlueNavLink path={'/dashboard'} prompt={'cofnij'} />,
            <VersionSelect onChange={handleVersionChange} data={versions} />
          ]}
      >
        <DataTableFiltered ref={tableRef}/>
        {navToImport && <Navigate to={'/new-data'}/>}
      </PageWrapper>
  )
}