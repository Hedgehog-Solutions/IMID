import axios from "axios";


export const testHello = async (getter) => {

  try {
    const response = await axios.get('http://localhost:5000/hello');
    getter(response.data);
  } catch(error) {
    console.error(error);
  }
}

export const testDupa = async (getter) => {

  try {
    const response = await axios.get('http://localhost:5000/api/dupa', {withCredentials: true});
    getter(response.data);
  } catch(error) {
    console.error(error);
  }
}

