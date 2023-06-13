import axios from "axios";


export const handleLogin = (login, password) => {
  return login === 'test' && password === 'test';
}

export const handleTrueLogin = async(login, password) => {
  axios.defaults.headers.post['Content-Type'] ='application/json';
  axios.defaults.withCredentials = true
  try {
    const response = await axios.post('http://localhost:5000/api/login', JSON.stringify({username: login, password}),  );
    console.log(response.status);
  } catch(error) {
    console.error(error);
  }
}


export const handleTrueLogout = async() => {
  try {
    const response = await axios.post('http://localhost:5000/api/logout');
    console.log(response.status);
  } catch(error) {
    console.error(error);
  }
}