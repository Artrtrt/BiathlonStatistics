import axios from "axios";

let model: any = {};

function SetModel(input: any) {
  model = input;
}

type SeasonUnit = {
  title: string;
  year: string;
  competitionList: CompetitionUnit[];
};

type CompetitionUnit = {
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
};

async function MethodImportInfo() {
  if (data.seasonList.length === 0) {
    const seasons = await axios.get("http://127.0.0.1:8000/seasons/");
    const competitions = await axios.get("http://127.0.0.1:8000/competitions/");
    const results = await axios.get("http://127.0.0.1:8000/results/");
    seasons.data.forEach((season: any, seasonIndex: number) => {
      const competitionList = [] as CompetitionUnit[];
      competitions.data.forEach(
        (competition: any, competitionIndex: number) => {
          const categoryList = {} as { [category: string]: ResultUnit[] };
          results.data.forEach((result: any) => {
            if (result.competition === competitionIndex + 1) {
              if (categoryList[result.category]) {
                categoryList[result.category].push({
                  sportsman: result.sportsman,
                  country: result.country,
                  category: result.category,
                  goldMedals: result.gold_medals,
                  silverMedals: result.silver_medals,
                  bronzeMedals: result.bronze_medals,
                  points: result.points,
                });
              } else {
                categoryList[result.category] = [];
              }
            }
          });
          if (competition.season === seasonIndex + 1) {
            competitionList.push({
              title: competition.title,
              date: competition.date,
              categoryList: categoryList,
            });
          }
        }
      );
      data.seasonList.push({
        title: season.title,
        year: season.year,
        competitionList: competitionList,
      });
    });
  }
  data.seasonList.reverse();
}
async function MethodExportInfo() {
  console.log('aaa');
}

const method = {
  import: MethodImportInfo,
  export: MethodExportInfo,
};

export { SetModel, data, method };
