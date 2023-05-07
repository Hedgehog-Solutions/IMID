import React from "react";
import styled from "styled-components";
import Dropzone from "react-dropzone";
import {colors} from "../../utils/colors";
import {P2} from "../../utils/typography";


const StyledDropzone = styled.div`
  width: 40%;
  height: 40%;
  
  border: 4px solid ${colors.darkBlue};
  
  border-radius: 30px;
  
  text-align: center;
  display: flex;
  
  align-items: center;
  justify-content: center;
  
  cursor: pointer;
  
  transition: 0.3s;
`


export const FileDropzone = ({callback = () => {}}) => {
  const [isDragging, setIsDragging] = React.useState(false);

  const handleDragStart = React.useCallback(() => {
    setIsDragging(true)
  }, [])

  const handleDragEnd = React.useCallback(() => {
    setIsDragging(false)
  }, [])

  const handleDrop = React.useCallback((acceptedFiles) => {
    callback(acceptedFiles);
    setIsDragging(false)
  })

  return(
      <Dropzone
          onDrop={handleDrop}
          onDragEnter={handleDragStart}
          onDragLeave={handleDragEnd}
      >
        {({getRootProps, getInputProps}) => (
              <StyledDropzone {...getRootProps()} style={!isDragging ? {width: '40%', height: '40%'} : {width: '35%', height: '35%'}}>
                <input {...getInputProps()} />
                <P2>Upuść pliki, lub kliknij, żeby wybrać</P2>
              </StyledDropzone>
        )}
      </Dropzone>
  )
}