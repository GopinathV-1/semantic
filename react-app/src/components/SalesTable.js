import React, { Component } from "react";
import ReactTable from "react-table";
import "react-table/react-table.css";

class SalesTable = (data) {
  render() {
    const columns = [
      {
        Header: "Drug Classification",
        accessor: "name",
      },
      {
        Header: "ATC Classification",
        accessor: "atc_name",
      },
      {
        Header: "Sales <year>",
        accessor: "sales_current_year",
      },
      {
        Header: "Sales <prev year>",
        accessor: "sales_previous_year",
      },
    ];
    return (
      <div>
        <ReactTable
          data={data}
          columns={columns}
          defaultPageSize={2}
          pageSizeOptions={[2, 4, 6]}
        />
      </div>
    );
  }
}
export default SalesTable;
