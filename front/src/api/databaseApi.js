import axios from "axios";
import * as fs from "fs";
import * as path from "path";



export const browseDataApi = async (getter, versionId) => {

  try {
    const response = await axios.get(`http://localhost:5000/api/data/${versionId}`);
    getter(response.data);
  } catch(error) {
    console.error(error);
  }
}

export const getVersionsApi = async (getter) => {

  try {
    const response = await axios.get('http://localhost:5000/api/versions');
    getter(response.data);
  } catch(error) {
    console.log(error);
  }
}

export const getDownloadFile = async(id) => {

  try {
    axios
        .get(`http://localhost:5000/api/export/${id}`, { responseType: 'stream' })
        .then(async resp => {
          resp.data.pipe(fs.createWriteStream(`./downloads/${id}.tsv`));
        });
  } catch(error) {
    console.log(error);
  }
}

export const postUploadFile = async(file) => {
  const url = 'http://localhost:5000/api/upload';
  const filePath = path.resolve(file);
  fs.readFile(filePath, async (error, data) => {
    if (error) {
      console.log(error);
      return;
    }
    const formData = new FormData();
    formData.append('file', data, { filepath: filePath, contentType: 'text/plain' });
    axios
        .post(url, formData, { headers: formData.getHeaders() })
        .then(resp => {
          console.log('File uploaded successfully.');
        });
  });
}