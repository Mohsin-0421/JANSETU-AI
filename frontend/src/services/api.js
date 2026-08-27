import axios from "axios";

const api = axios.create({
  baseURL: "https://kbcn7c2s-8000.inc1.devtunnels.ms/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;