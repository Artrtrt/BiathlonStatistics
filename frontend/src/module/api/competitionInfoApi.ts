import axios from "axios";
import { ResultUnit } from "@/module/model/app";

async function fetchSeasonList() {
  try {
    const seasonList = await axios.get("http://127.0.0.1:8000/seasons/");
    return seasonList.data;
  } catch (err) {
    throw new Error("Ошибка при получении информации о сезонах");
  }
}

async function fetchCompetitionList() {
  try {
    const competitionList = await axios.get(
      "http://127.0.0.1:8000/competitions/"
    );
    return competitionList.data;
  } catch (err) {
    throw new Error("Ошибка при получении данных о соревнованиях");
  }
}

async function fetchResultList() {
  try {
    const resultList = await axios.get("http://127.0.0.1:8000/results/");
    return resultList.data;
  } catch (err) {
    throw new Error("Ошибка при получении данных о результатах");
  }
}

async function addSeason(
  title: string,
  year: string,
  token: string
): Promise<number> {
  const bodyFormData = new FormData();
  bodyFormData.append("title", title);
  bodyFormData.append("year", year);
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/add_season/",
      bodyFormData,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response.data.id;
  } catch (err) {
    throw new Error("Ошибка при добавлении сезона");
  }
}

async function addCompetition(
  seasonId: number,
  title: string,
  date: string,
  token: string
): Promise<number> {
  const bodyFormData = new FormData();
  bodyFormData.append("title", title);
  bodyFormData.append("date", date);
  bodyFormData.append("season", seasonId.toString());
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/add_competition/",
      bodyFormData,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response.data.id;
  } catch (err) {
    throw new Error("Ошибка при добавлении соревнования");
  }
}

async function addCategory(
  resultList: ResultUnit[],
  competitionId: number,
  token: string
) {
  try {
    await axios.post(
      "http://127.0.0.1:8000/add_category/",
      {
        competition: competitionId,
        array: resultList,
      },
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
  } catch (err) {
    throw new Error("Ошибка при добавлении резульатов");
  }
}

async function deleteSeason(id: number, token: string) {
  try {
    await axios.delete(`http://127.0.0.1:8000/delete_season/${id}/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  } catch (err) {
    throw new Error("Ошибка при удалении сезона");
  }
}

async function deleteСompetition(id: number, token: string) {
  try {
    await axios.delete(`http://127.0.0.1:8000/delete_competition/${id}/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  } catch (err) {
    throw new Error("Ошибка при удалении соревнования");
  }
}

async function deleteCategory(compId: number, category: string, token: string) {
  const bodyFormData = new FormData();
  bodyFormData.append("competition_id", compId.toString());
  bodyFormData.append("category", category);
  try {
    await axios.post("http://127.0.0.1:8000/delete_category/", bodyFormData, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  } catch (err) {
    throw new Error("Ошибка при удалении результата");
  }
}

async function updateSeason(
  id: number,
  title: string,
  year: string,
  token: string
) {
  const bodyFormData = new FormData();
  bodyFormData.append("title", title);
  bodyFormData.append("year", year);
  try {
    await axios.patch(
      `http://127.0.0.1:8000/update_season/${id}/`,
      bodyFormData,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
  } catch (err) {
    throw new Error("Ошибка при обновлении сезона");
  }
}

async function updateCompetition(
  id: number,
  title: string,
  date: string,
  token: string
) {
  const bodyFormData = new FormData();
  bodyFormData.append("title", title);
  bodyFormData.append("date", date);
  try {
    await axios.patch(
      `http://127.0.0.1:8000/update_competition/${id}/`,
      bodyFormData,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
  } catch (err) {
    throw new Error("Ошибка при обновлении соревнования");
  }
}

export {
  fetchSeasonList,
  fetchCompetitionList,
  fetchResultList,
  addSeason,
  addCompetition,
  addCategory,
  deleteSeason,
  deleteСompetition,
  deleteCategory,
  updateSeason,
  updateCompetition,
};
