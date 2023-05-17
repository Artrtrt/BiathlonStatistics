import axios from "axios";
import { ResultUnit } from "@/module/model/app";

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

async function addSeason(title: string, year: string) {
  const bodyFormData = new FormData();
  bodyFormData.append('title', title);
  bodyFormData.append('year', year);
  try {
    await axios.post("http://127.0.0.1:8000/add_season/", bodyFormData);
  } catch (err) {
    throw new Error('Ошибка при добавлении сезона')
  }
}

async function addCompetition(seasonId: number, title: string, date: string) {
  const bodyFormData = new FormData();
  bodyFormData.append('title', title);
  bodyFormData.append('date', date);
  bodyFormData.append('season', seasonId.toString());
  try {
    await axios.post("http://127.0.0.1:8000/add_competition/", bodyFormData);
  } catch (err) {
    throw new Error('Ошибка при добавлении соревнования')
  }
}

async function addCategory(resultList: ResultUnit[], competitionId: number) {
  const payload = {
    resultList,
    competitionId
  }
  try {
    await axios({
      url: 'http://127.0.0.1:8000/add_category/',
      method: 'post',
      data: payload
    })
  } catch (err) {
    throw new Error('Ошибка при добавлении резульатов')
  }
}

async function deleteSeason(id: number) {
  try {
    await axios.delete(`http://127.0.0.1:8000/delete_season/${id}/`);
  } catch (err) {
    throw new Error('Ошибка при удалении сезона')
  }
}

async function deleteСompetition(id: number) {
  try {
    await axios.delete(`http://127.0.0.1:8000/delete_competition/${id}/`);
  } catch (err) {
    throw new Error('Ошибка при удалении соревнования')
  }
}

async function deleteCategory(compInd: number, category: string) {
  const payload = {
    compInd,
    category
  }
  try {
    await axios({
      url: 'http://127.0.0.1:8000/delete_category/',
      method: 'delete',
      data: payload
    })
  } catch (err) {
    throw new Error('Ошибка при удалении результата')
  }
}

async function updateSeason(id: number, title: string, year: string) {
  const bodyFormData = new FormData();
  bodyFormData.append('title', title);
  bodyFormData.append('year', year);
  try {
    await axios.patch(`http://127.0.0.1:8000/update_season/${id}/`, bodyFormData);
  } catch (err) {
    throw new Error('Ошибка при обновлении сезона')
  }
}

async function updateCompetition(id: number, title: string, date: string) {
  const bodyFormData = new FormData();
  bodyFormData.append('title', title);
  bodyFormData.append('date', date);
  console.log(id);
  console.log(title);
  console.log(date);
  try {
    await axios.patch(`http://127.0.0.1:8000/update_competition/${id}/`, bodyFormData);
  } catch (err) {
    throw new Error('Ошибка при обновлении соревнования')
  }
}

export { fetchSeasonList, fetchCompetitionList, fetchResultList, addSeason, addCompetition, addCategory, deleteSeason, deleteСompetition, deleteCategory, updateSeason, updateCompetition };