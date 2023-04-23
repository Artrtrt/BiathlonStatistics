<template>
  <div style="height: 100%">
    <i-container class="_margin-bottom-1 _padding-bottom-1">
      <div id="title" class="_padding-top-1 _margin-bottom-1" style="text-align: center;">
        <a>{{ competition.title }}</a>
      </div>
      <div style="background-color: #e8eeffc2; border-radius: 10px;" class="_padding-1">
        <div v-for="(resultList, category) in competition.categoryList" :key="category">
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

export default Vue.extend({
  name: "CompetitionPage",
  data() {
    return {
      model,

      competition: {} as any,
    };
  },
  methods: {
  },
  beforeMount() {
    const temp = this.$route.path.split('/')[2];
    if (temp !== undefined) {
      const [season, competition] = temp.split('.');
      this.competition = model.data.app.seasonList[parseInt(season)].competitionList[parseInt(competition)];
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