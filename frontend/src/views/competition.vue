<template>
  <div style="height: 100%">
    <i-container class="_margin-bottom-1 _padding-bottom-1">
      <div id="title" class="_padding-top-1 _margin-bottom-1" style="text-align: center;">
        <a>{{ competition.title }}</a>
      </div>
      <i-button v-if="isAdmin" @click="uploadFile" class="button-confirm _margin-bottom-1">Добавить
        таблицу</i-button>
      <div
        v-if="Object.keys(model.data.app.seasonList[seasonIndex].competitionList[competitionIndex].categoryList).length !== 0"
        style="background-color: #e8eeffc2; border-radius: 10px;" class="_padding-1">
        <div v-for="(resultList, category) in competition.categoryList" :key="category">
          <i-button v-if="isAdmin" @click="deleteCategory(category)" class="_float-right button-danger">Удалить</i-button>
          <div class="category-title _margin-bottom-1 _margin-left-1">{{ category }}</div>
          <div class="_margin-bottom-1">
            <i-table hover class="table">
              <thead>
                <tr>
                  <th scope="row">#</th>
                  <th>Атлет</th>
                  <th>Страна</th>
                  <th>Золото</th>
                  <th>Серебро</th>
                  <th>Бронза</th>
                  <th>Очки</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(result, index) in resultList" :key="index">
                  <td scope="row" class="bg-td">{{ index + 1 }}</td>
                  <td class="bg-td">{{ result.sportsman }}</td>
                  <td class="bg-td">{{ result.country }}</td>
                  <td class="bg-gold">{{ result.goldMedals }}</td>
                  <td class="bg-silver">{{ result.silverMedals }}</td>
                  <td class="bg-bronze">{{ result.bronzeMedals }}</td>
                  <td class="bg-td">{{ result.points }}</td>
                </tr>
              </tbody>
            </i-table>
          </div>
        </div>
      </div>
    </i-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";
import { ResultUnit } from "@/module/model/app";

export default Vue.extend({
  name: "CompetitionPage",
  data() {
    return {
      model,

      seasonIndex: 0,
      competitionIndex: 0,
      isAdmin: model.data.auth.isAdmin,
      competition: {} as any,
      errMessage: '',
    };
  },
  methods: {
    deleteCategory(category: any) {
      delete model.data.app.seasonList[this.seasonIndex].competitionList[this.competitionIndex].categoryList[category];
      this.$forceUpdate();
    },
    addCategory(category: string, content: string) {
      const categoryList = model.data.app.seasonList[this.seasonIndex].competitionList[this.competitionIndex].categoryList
      if (categoryList[category]) {
        alert('Такая категория уже добавлена') // eslint-disable-line
        return;
      }
      this.errMessage = '';
      const rows = content.split('\n');
      const resultList = [] as ResultUnit[];
      rows.forEach((row: string, index: number) => {
        if (row.length !== 0) {
          if (!row.match(('[а-яА-Я]* [а-яА-Я]*;[а-яА-Я]*;\\d+;\\d+;\\d+;\\d+'))) {
            this.errMessage += `Ошибка в строке: ${index + 1}\n`
            return
          }
          const result = row.split(';');
          resultList.push({
            sportsman: result[0],
            country: result[1],
            category: category,
            goldMedals: parseInt(result[2]),
            silverMedals: parseInt(result[3]),
            bronzeMedals: parseInt(result[4]),
            points: parseInt(result[5]),
          })
        }
      });
      if (this.errMessage !== '') {
        alert(this.errMessage) // eslint-disable-line
      }
      categoryList[category] = resultList;
      this.$forceUpdate();
    },
    uploadFile() {
      const input = document.createElement('input'); // eslint-disable-line
      input.type = 'file';

      let vue = this; // eslint-disable-line
      input.onchange = (event: Event) => {
        const element = event.target as HTMLInputElement; // eslint-disable-line

        if (!element.files?.length) {
          return;
        }

        const file = element.files[0];
        const reader = new FileReader(); // eslint-disable-line
        reader.onload = async function (e: any) {
          if (file.type !== 'text/csv') {
            alert('Должен быть формат csv') // eslint-disable-line
            return
          }
          const category = file.name.split('.csv')[0];
          vue.addCategory(category, e.target.result)
        };
        reader.readAsText(file, 'CP1251');
      };
      input.click();
    },
  },
  beforeMount() {
    const temp = this.$route.path.split('/')[2];
    if (temp !== undefined) {
      const [season, competition] = temp.split('.');
      this.seasonIndex = parseInt(season);
      this.competitionIndex = parseInt(competition);
      this.competition = model.data.app.seasonList[this.seasonIndex].competitionList[this.competitionIndex];
    } else {
      this.$router.replace(`/competition/0.0`);
      this.competition = model.data.app.seasonList[0].competitionList[0];
    }
  }
});
</script>

<style scoped>
#title {
  color: #233567;
  font-size: 40px;
}

.category-title {
  color: #233567;
  font-size: 25px;
}

.table {
  text-align: center;
}

.bg-td {
  background-color: #e8eeffc2 !important;
}

.table th {
  background-color: #bcc9e2 !important;
}
</style>