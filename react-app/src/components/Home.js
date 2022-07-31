import React, { useState } from "react";
import AssignmentForm from "./AssignmentForm";
import axios from "axios";

const Home = ({ history }) => {
  const [data, setData] = useState(null);
  const handleOnSubmit = async (data) => {
    await axios({
      method: "get",
      url: "http://localhost:8000/sales/",
      data: data,
    })
      .then((response) => {
          setData(response);
      })
      .catch((error) => {
        switch (error.response.status) {
          case 400:
            history.push("/");
            break;
          default:
            break;
        }
      });
  };

  return (
    <React.Fragment>
      <InputForm handleOnSubmit={handleOnSubmit} />
      <SalesTable data={data} />
    </React.Fragment>
  );
};

export default AddAssignment;
