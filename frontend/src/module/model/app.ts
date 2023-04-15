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
  categotiesList: CategotyUnit[];
};

type CategotyUnit = {
  title: string;
  resultList: ResultUnit[];
};

export type ResultUnit = {
  sportsman: string;
  country: string;
  goldMedals: number;
  silverMedals: number;
  bronzeMedals: number;
  points: number;
};

const data = {
  seasonList: [] as SeasonUnit[],
};

async function MethodImportInfo() {
  console.log('aaa');
}

const method = {
  import: MethodImportInfo,
};

export { SetModel, data, method };
