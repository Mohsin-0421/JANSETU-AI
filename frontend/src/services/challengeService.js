import api from "./api";

export const getChallenges = async () => {
  const response = await api.get("/challenges/");
  return response.data;
};

export const createChallenge = async (challengeData) => {
  const response = await api.post("/challenges/", challengeData);
  return response.data;
};