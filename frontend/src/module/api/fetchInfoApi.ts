import axios from "axios";

async function fetchSeasonList() {
  try {
    const seasonList = await axios.get("http://127.0.0.1:8000/seasons/");
    return seasonList.data;
  } catch (err) {
    throw new Error('Ошибка при получении информации о сезонах')
  }
}

async function fetchCompetitionList() {
  try {
    const competitionList = await axios.get("http://127.0.0.1:8000/competitions/");
    return competitionList.data;
  } catch (err) {
    throw new Error('Ошибка при получении данных о соревнованиях')
  }
}

async function fetchResultList() {
  try {
    const resultList = await axios.get("http://127.0.0.1:8000/results/");
    return resultList.data;
  } catch (err) {
    throw new Error('Ошибка при получении данных о результатах')
  }
}

export { fetchSeasonList, fetchCompetitionList, fetchResultList };