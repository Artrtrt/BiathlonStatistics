import * as infoApi from "../api/competitionInfoApi";

const token = localStorage.getItem("auth_token") as string;

type SeasonUnit = {
  id: number;
  title: string;
  year: string;
  competitionList: CompetitionUnit[];
};

export type CompetitionUnit = {
  id: number;
  title: string;
  date: string;
  categoryList: { [category: string]: ResultUnit[] };
};

export type ResultUnit = {
  sportsman: string;
  country: string;
  category: string;
  goldMedals: number;
  silverMedals: number;
  bronzeMedals: number;
  points: number;
};

const data = {
  seasonList: [] as SeasonUnit[],
  loading: false,
};

async function MethodImportInfo() {
  data.loading = true;
  if (data.seasonList.length === 0) {
    const seasons = await infoApi.fetchSeasonList();
    const competitions = await infoApi.fetchCompetitionList();
    const results = await infoApi.fetchResultList();
    seasons.forEach((season: any, seasonIndex: number) => {
      const competitionList = [] as CompetitionUnit[];
      competitions.forEach((competition: any, competitionIndex: number) => {
        const categoryList = {} as { [category: string]: ResultUnit[] };
        results.forEach((result: any) => {
          if (result.competition === competition.id) {
            if (!categoryList[result.category]) {
              categoryList[result.category] = [];
            }
            categoryList[result.category].push({
              sportsman: result.sportsman,
              country: result.country,
              category: result.category,
              goldMedals: result.gold_medals,
              silverMedals: result.silver_medals,
              bronzeMedals: result.bronze_medals,
              points: result.points,
            });
          }
        });
        if (competition.season === season.id) {
          competitionList.push({
            id: competition.id,
            title: competition.title,
            date: competition.date,
            categoryList: categoryList,
          });
        }
      });
      competitionList.reverse();
      data.seasonList.push({
        id: season.id,
        title: season.title,
        year: season.year,
        competitionList: competitionList,
      });
    });
  }
  data.seasonList.reverse();
  data.loading = false;
}

function findCompetition(
  seasonId: number,
  competitionId: number
): CompetitionUnit | undefined {
  const season = data.seasonList.find((season) => season.id === seasonId);
  if (season) {
    const competition = season?.competitionList.find(
      (competition) => competition.id === competitionId
    );
    if (competition) return competition;
  }
  return undefined;
}

async function MethodAddSeason(title: string, year: string) {
  const id = await infoApi.addSeason(title, year, token);
  data.seasonList.unshift({ id, title, year, competitionList: [] });
}

async function MethodAddCompetition(
  seasonInd: number,
  title: string,
  date: string
) {
  const id = await infoApi.addCompetition(
    data.seasonList[seasonInd].id,
    title,
    date,
    token
  );
  data.seasonList[seasonInd].competitionList.unshift({
    id,
    title,
    date,
    categoryList: {},
  });
}

async function MethodAddCategory(
  seasonId: number,
  competitionId: number,
  category: string,
  resultList: ResultUnit[]
) {
  const competition = findCompetition(seasonId, competitionId);
  if (competition !== undefined) {
    competition.categoryList[category] = resultList;
  }
  await infoApi.addCategory(resultList, competitionId, token);
}

async function MethodDeleteSeason(ind: number) {
  const seasonList = data.seasonList;
  await infoApi.deleteSeason(seasonList[ind].id, token);
  if (ind === 0) {
    data.seasonList.shift();
  } else {
    data.seasonList.splice(ind, ind);
  }
}

async function MethodDeleteCompetition(seasonInd: number, compInd: number) {
  const competitionList = data.seasonList[seasonInd].competitionList;
  await infoApi.deleteСompetition(competitionList[compInd].id, token);
  if (compInd === 0) {
    competitionList.shift();
  } else {
    competitionList.splice(compInd, compInd);
  }
}

async function MethodDeleteCategory(
  seasonId: number,
  competitionId: number,
  category: string
) {
  await infoApi.deleteCategory(competitionId, category, token);
  const competition = findCompetition(seasonId, competitionId);
  if (competition !== undefined) {
    delete competition?.categoryList[category];
  }
}

async function MethodUpdateSeason(ind: number, title: string, year: string) {
  const season = data.seasonList[ind];
  season.title = title;
  season.year = year;
  await infoApi.updateSeason(season.id, title, year, token);
}

async function MethodUpdateCompetition(
  seasonInd: number,
  compInd: number,
  title: string,
  date: string
) {
  const competiton = data.seasonList[seasonInd].competitionList[compInd];
  competiton.title = title;
  competiton.date = date;
  await infoApi.updateCompetition(competiton.id, title, date, token);
}

const method = {
  import: MethodImportInfo,
  addSeason: MethodAddSeason,
  addCompetition: MethodAddCompetition,
  addCategory: MethodAddCategory,
  deleteSeason: MethodDeleteSeason,
  deleteCompetition: MethodDeleteCompetition,
  deleteCategory: MethodDeleteCategory,
  updateSeason: MethodUpdateSeason,
  updateCompetition: MethodUpdateCompetition,
};

export { data, method };
