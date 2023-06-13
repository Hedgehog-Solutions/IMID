import axios from "axios";


export const testHello = async (getter) => {

  try {
    const response = await axios.get('http://localhost:5000/hello');
    getter(response.data);
  } catch(error) {
    console.error(error);
  }
}

