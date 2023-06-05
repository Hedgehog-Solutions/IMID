import React from "react";
import { PageWrapper } from "../components/PageWrapper/pageWrapper";
import { Header } from "../components/Header/header";
import {FileDropzone} from "../components/FileDropzone/FileDropzone";
import {Toast} from "../components/ToastNotifications/Toast";
import {BlueNavLink} from "../components/BlueButton/blueButton";



export const NewDataPage = () => {

  const [toasts, setToasts] = React.useState([<div />]);

  const handleDataDrop = (files) => {
    files.forEach(f => {
      if (f.path.match('^.*\\.(txt|TXT|csv|CSV|dat|DAT|tsc|TSV)$')) {
        console.log(f);
        setToasts(<Toast text={'Udało się dodać dane!'} key={'1'} type={'success'}/>)
      }
      else {
        setToasts(<Toast text={'Nieobsługiwany typ pliku!'} key={'2'} type={'error'}/>)
      }

    })
  }
  return (
      <PageWrapper
          toasts={toasts}
          leftMenu={[
              <BlueNavLink path={'/dashboard'} prompt={'cofnij'} />,
          ]}
      >
        <Header text={'Dodaj dane'} />
        <FileDropzone callback={handleDataDrop}/>
      </PageWrapper>
  )
}