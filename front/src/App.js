import logo from './logo.svg';
import './App.css';

import { LoginPage } from "./pages/loginPage";

import {
  createBrowserRouter,
    createRoutesFromElements,
    Route,
    RouterProvider
} from "react-router-dom";
import {NewDataPage} from "./pages/newDataPage";
import {DashboardPage} from "./pages/dashboardPage";
import {AccessRequestPage} from "./pages/accessRequestPage";
import {BrowseDataPage} from "./pages/browseDataPage";

const router = createBrowserRouter(
    createRoutesFromElements([
        <Route path={"/"} element={<LoginPage />} />,
        <Route path={"/dashboard"} element={<DashboardPage />} />,
        <Route path={"/new-data"} element={<NewDataPage />} />,
        <Route path={"/access-request"} element={<AccessRequestPage />} />,
        <Route path={"browse-data"} element={<BrowseDataPage />} />
    ])
)

function App() {
  return (
      <RouterProvider router={router} />
  );
}

export default App;
