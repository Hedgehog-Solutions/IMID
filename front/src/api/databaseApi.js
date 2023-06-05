import axios from "axios";


export const browseDataApi = async (getter) => {

  try {
    const response = await axios.get('http://localhost:5000/api/data');
    getter(response.data);
  } catch(error) {
    console.error(error);
  }
}