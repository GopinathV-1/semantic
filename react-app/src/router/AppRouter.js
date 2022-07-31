import React from "react";
import { useHistory } from "react-router";
import { BrowserRouter, Route } from "react-router-dom";
import Home from "../components/home";
import { CookiesProvider } from "react-cookie";

const AppRouter = () => {
  const history = useHistory();
  return (
    <CookiesProvider>
      <BrowserRouter>
        <div>
            <Route render={(props) => <Home {...props} />} path="/" />
        </div>
      </BrowserRouter>
    </CookiesProvider>
  );
};

export default AppRouter;
