import React from "react";
import styled from "styled-components";





export const VersionSelect = ({onChange, data}) => {

  const makeOptions = (d) => {
    let options = [];
    for (let el in d) {
      options.push(
          <option value={d[el].id}> {d[el].from_date} </option>
      )
    }

    return options
  }


  return(
    <select onChange={(e) => onChange(e)} name={'Wersje'} id={'versions'} style={{marginTop: 20}}>
      {makeOptions(data)}
    </select>
  )
}