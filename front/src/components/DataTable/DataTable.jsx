import React from 'react'
import styled from 'styled-components'
import { useTable } from 'react-table'

import makeData from "../../utils/mockData";
const Styles = styled.div`
  max-height: 100vh;
  padding: 1rem;

  overflow: auto;
  table {
    border-spacing: 0;
    border: 1px solid black;


    tr {
      :last-child {
        td {
          border-bottom: 0;
        }
      }
    }

    th,
    td {
      margin: 0;
      padding: 0.5rem;
      border-bottom: 1px solid black;
      border-right: 1px solid black;

      :last-child {
        border-right: 0;
      }
    }
  }
`

const testFilter = (row, columnId, value, addMeta) => {
  console.log(row, columnId, addMeta);
  return row.getValue(columnId).match(value);
}

function Table({ columns, data }) {

  const [columnFilters, setColumnFilters] = React.useState([{firstName: 'asd'}]);
  // Use the state and functions returned from useTable to build your UI
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable({
    columns,
    data,
    state: {
      columnFilters,
    },
    onColumnFiltersChange: setColumnFilters,
  })

  // Render the UI for your table
  return (
      <table {...getTableProps()}>
        <thead>
        {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(header => (
                  <th {...header.getHeaderProps()}>{header.render('Header')}
                    {header.getCanFilter ? (
                        <FilterInput header={header.id} />
                    ) : null}
                  </th>

              ))}
            </tr>
        ))}
        </thead>
        <tbody {...getTableBodyProps()}>
        {rows.map((row, i) => {
          prepareRow(row)
          return (
              <tr {...row.getRowProps()}>
                {row.cells.map(cell => {
                  return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                })}
              </tr>
          )
        })}
        </tbody>
      </table>
  )
}

const FilterInput = ({header}) => {

  return(
      <input onChange={e => console.log(e.target.value, header)} placeholder={"Szukaj..."}/>
  )
}

export const DataTable = () => {
  const columns = React.useMemo(
      () => [
            {
              Header: 'First Name',
              accessor: 'firstName',
              filterFn: 'default',
              canFilter: true,
            },
            {
              Header: 'Last Name',
              accessor: 'lastName',
            },
            {
              Header: 'Age',
              accessor: 'age',
            },
            {
              Header: 'Visits',
              accessor: 'visits',
            },
            {
              Header: 'Status',
              accessor: 'status',
            },
            {
              Header: 'Profile Progress',
              accessor: 'progress',
            },
      ],
      []
  )

  const data = React.useMemo(() => makeData(20), [])

  return (
      <Styles>
        <Table columns={columns} data={data} />
      </Styles>
  )
}